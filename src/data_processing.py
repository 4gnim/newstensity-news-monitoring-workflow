"""Pembersihan, validasi, normalisasi, dan deduplikasi data berita.

Modul ini sengaja berfokus pada data lokal/hasil ekspor. Konektor ke sistem internal,
RSS, atau News API berada di luar scope demonstrasi dan harus mengikuti akses resmi.
"""
from __future__ import annotations
import hashlib
import re
from typing import Iterable
import pandas as pd

REQUIRED_COLUMNS = ["article_id", "source", "published_at", "title", "body"]

def normalize_text(value: object) -> str:
    """Normalisasi teks ringan tanpa mengubah makna atau melakukan stemming."""
    if pd.isna(value):
        return ""
    text = str(value).lower().strip()
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()

def fingerprint(title: object, body: object) -> str:
    """Hash konten untuk mendeteksi duplikasi identik setelah normalisasi."""
    canonical = normalize_text(title) + " | " + normalize_text(body)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

def validate_schema(df: pd.DataFrame) -> list[str]:
    """Mengembalikan daftar masalah skema; daftar kosong berarti lolos pemeriksaan dasar."""
    problems = [f"Kolom wajib tidak tersedia: {c}" for c in REQUIRED_COLUMNS if c not in df.columns]
    if not problems:
        for col in ["article_id", "source", "title", "body"]:
            if df[col].isna().any():
                problems.append(f"Kolom {col} memiliki nilai kosong")
    return problems

def process_news(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Bersihkan dan deduplikasi berita berdasarkan fingerprint judul + isi.

    Penghapusan duplikat dilakukan konservatif pada konten identik. Near-duplicate
    berbasis similarity perlu threshold dan pemeriksaan sampel sebelum produksi.
    """
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Kolom wajib tidak tersedia: {missing}")
    work = df.copy()
    before = len(work)
    work["title"] = work["title"].fillna("").astype(str).str.strip()
    work["body"] = work["body"].fillna("").astype(str).str.strip()
    work["source"] = work["source"].fillna("unknown").astype(str).str.strip()
    work["published_at"] = pd.to_datetime(work["published_at"], errors="coerce", utc=True)
    invalid_date = int(work["published_at"].isna().sum())
    work["text_normalized"] = (work["title"].map(normalize_text) + " " + work["body"].map(normalize_text)).str.strip()
    work["content_fingerprint"] = [fingerprint(t, b) for t, b in zip(work["title"], work["body"])]
    work = work[work["title"].ne("") & work["body"].ne("")].copy()
    work = work.sort_values(["published_at", "article_id"], na_position="last")
    deduped = work.drop_duplicates(subset=["content_fingerprint"], keep="first").copy()
    stats = {
        "input_rows": before,
        "invalid_published_at": invalid_date,
        "removed_empty_content": before - int((df["title"].fillna("").astype(str).str.strip().ne("") & df["body"].fillna("").astype(str).str.strip().ne("")).sum()),
        "duplicate_rows_removed": len(work) - len(deduped),
        "output_rows": len(deduped),
    }
    return deduped.reset_index(drop=True), stats
