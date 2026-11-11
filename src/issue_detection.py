"""Baseline issue detection: keyword features + TF-IDF clustering.

Ini adalah baseline demonstrasi, bukan konfigurasi produksi. Untuk produksi,
validasi embedding multibahasa/Indonesia dan algoritma clustering pada data berlabel.
"""
from __future__ import annotations
import re
from collections import Counter
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

STOPWORDS = {"yang", "dan", "di", "ke", "dari", "untuk", "dengan", "pada", "dalam", "atau", "ini", "itu", "sebagai", "oleh", "dalam", "terkait", "sejumlah", "pihak", "artikel", "simulasi"}
ENTITY_PATTERNS = {
    "Gibran": r"\bgibran\b",
    "Wakil Presiden": r"\bwakil presiden\b",
    "DPR": r"\bdpr\b",
    "Mahkamah Konstitusi": r"\bmahkamah konstitusi\b",
}

def extract_keywords(texts: list[str], top_n: int = 10) -> list[tuple[str, int]]:
    tokens=[]
    for text in texts:
        tokens.extend(t for t in re.findall(r"\b[a-zA-ZÀ-ÿ]{3,}\b", str(text).lower()) if t not in STOPWORDS)
    return Counter(tokens).most_common(top_n)

def extract_entities(text: str) -> list[str]:
    value = str(text).lower()
    return [entity for entity, pattern in ENTITY_PATTERNS.items() if re.search(pattern, value)]

def cluster_articles(texts: list[str], n_clusters: int = 4, random_state: int = 42) -> list[int]:
    """Kembalikan ID cluster; makna cluster perlu ditinjau dari kata kunci/sampel."""
    if len(texts) < 2:
        return [0] * len(texts)
    k = max(2, min(n_clusters, len(texts)))
    vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 2), min_df=1)
    matrix = vectorizer.fit_transform(texts)
    model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    return model.fit_predict(matrix).tolist()

def enrich_issues(df: pd.DataFrame, text_column: str = "text_normalized") -> pd.DataFrame:
    result = df.copy()
    texts = result[text_column].fillna("").astype(str).tolist()
    result["entities"] = [", ".join(extract_entities(t)) for t in texts]
    result["cluster_id_baseline"] = cluster_articles(texts)
    return result
