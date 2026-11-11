# Implementation Status

Dokumen ini memisahkan komponen yang benar-benar tersedia dalam repository dari komponen yang masih berupa rancangan.

| Komponen | Status | Bukti / batasan |
|---|---|---|
| Problem statement dan solusi | Dibuat | Dokumen `docs/` |
| Workflow, architecture, data flow | Dibuat | Diagram Mermaid di `diagrams/` dan diagram pada deck |
| Dataset berita 500 artikel | Dibuat (sintetis) | `data/sample_news.csv`; bukan data aktual |
| Cleaning, validasi dasar, exact dedup | Demo berjalan | `src/data_processing.py`; belum near-duplicate produksi |
| Keyword extraction, entity rules, TF-IDF + KMeans | Demo berjalan | `src/issue_detection.py`; hasil cluster perlu interpretasi analis |
| Sentiment lexicon baseline | Demo berjalan | `src/sentiment_analysis.py`; bukan model terlatih, tidak ada klaim akurasi |
| Dashboard Streamlit | Kode demo tersedia | `dashboard/app.py`; membutuhkan instalasi `requirements.txt`; belum runtime-tested pada environment build ini karena Streamlit tidak terpasang |
| Ingestion RSS / News API / existing system | Rancangan saja | Menunggu akses, skema, hak penggunaan, dan API resmi |
| Model pretrained sentiment / embeddings produksi | Rekomendasi saja | Menunggu dataset berlabel dan benchmark |
| Database, scheduler, authentication, API production | Tidak dibuat | Di luar scope technical demonstration |
| Human review queue production | Rancangan saja | Alur dan field audit didokumentasikan, UI operasional belum dibangun |

Pengujian yang dijalankan pada build: 5 unit test lulus, Python source berhasil dikompilasi, demonstrasi pipeline menghasilkan 500 record unik dari 501 input (1 exact duplicate dihapus).
