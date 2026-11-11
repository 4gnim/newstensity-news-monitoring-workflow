"""Jalankan demonstrasi pipeline pada data sintetis lokal."""
from pathlib import Path
import pandas as pd
from data_processing import process_news
from issue_detection import enrich_issues, extract_keywords
from sentiment_analysis import analyze_sentiment

ROOT = Path(__file__).resolve().parents[1]

def main():
    raw = pd.read_csv(ROOT / "data" / "sample_news.csv")
    # Tambahkan satu baris duplikat untuk menguji fungsi deduplikasi.
    demo_input = pd.concat([raw, raw.iloc[[0]]], ignore_index=True)
    clean, stats = process_news(demo_input)
    enriched = enrich_issues(clean)
    predictions = pd.DataFrame(analyze_sentiment(enriched["text_normalized"].tolist()))
    enriched = pd.concat([enriched.reset_index(drop=True), predictions], axis=1)
    print("=== DEMO WORKFLOW NEWSTENSITY (DATA SINTETIS) ===")
    print("Processing:", stats)
    print("Predicted sentiment baseline:")
    print(enriched["sentiment_predicted"].value_counts().to_string())
    print("Top keywords:", extract_keywords(enriched["text_normalized"].tolist(), 12))
    print("Contoh output:")
    cols = ["article_id", "source", "title", "entities", "cluster_id_baseline", "sentiment_predicted"]
    print(enriched[cols].head(5).to_string(index=False))
    out = ROOT / "data" / "demo_processed_output.csv"
    enriched.to_csv(out, index=False)
    print(f"Output disimpan ke: {out.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
