"""Sentiment baseline transparan berbasis leksikon untuk demonstrasi.

PENTING: aturan kata ini bukan model terlatih dan tidak layak dipakai sebagai
penilaian produksi. Sentimen berita mengukur framing/nada artikel, bukan opini publik.
"""
from __future__ import annotations
POSITIVE = {"apresiasi", "dukungan", "optimisme", "optimistis", "harapan", "solusi", "konstruktif", "transparan", "positif", "kepercayaan", "membantu", "perbaikan"}
NEGATIVE = {"kritik", "polemik", "kekhawatiran", "kontroversi", "penolakan", "ketegangan", "kecemasan", "bermasalah", "keras", "negatif"}

def predict_sentiment(text: str) -> dict:
    tokens = set(str(text).lower().split())
    pos = sum(1 for word in POSITIVE if word in tokens)
    neg = sum(1 for word in NEGATIVE if word in tokens)
    total = pos + neg
    if pos > neg:
        label = "Positif"
    elif neg > pos:
        label = "Negatif"
    else:
        label = "Netral"
    confidence = abs(pos-neg) / max(total, 1)  # margin leksikon, bukan probabilitas terkalibrasi
    return {"sentiment_predicted": label, "lexicon_margin": round(float(confidence), 3), "positive_cue_count": pos, "negative_cue_count": neg}

def analyze_sentiment(texts: list[str]) -> list[dict]:
    return [predict_sentiment(text) for text in texts]
