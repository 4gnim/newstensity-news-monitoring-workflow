# System Architecture

Diagram sumber: [`../diagrams/architecture.mmd`](../diagrams/architecture.mmd).

## Lapisan arsitektur
1. **Input sources:** existing Newstensity data, RSS/News API, dan import Excel/CSV. Urutan ini bukan klaim bahwa sumber-sumber tersebut sudah tersedia; semuanya opsi yang harus diverifikasi.
2. **Integration layer:** source adapters, scheduled/incremental jobs, dan schema mapping. Adapter menjaga format sumber terpisah dari model data kanonis.
3. **Processing & AI layer:** validasi, normalisasi, fingerprint/dedup, entity & keyword extraction, semantic similarity/topic clustering, dan sentiment classifier.
4. **Storage & analytics:** raw/staging, canonical articles, enrichment, serta agregat analitik. Teknologi penyimpanan mengikuti platform perusahaan yang tersedia.
5. **Analyst layer:** dashboard, report/alerts, dan human review queue.

## Data contract kanonis (usulan)
| Field | Tujuan |
|---|---|
| article_id | ID internal yang stabil |
| source, source_url | Provenance dan rujukan ke sumber |
| published_at, collected_at | Waktu terbit dan waktu ingestion |
| title, body, language | Konten dan bahasa |
| content_fingerprint, duplicate_of | Deduplication dan relasi duplikat |
| entities, keywords | Hasil ekstraksi NLP |
| issue_id, cluster_id | Pengelompokan isu |
| sentiment_label, sentiment_score | Hasil sentimen |
| model_version, processed_at | Reproducibility |
| review_status, reviewer_label | Quality control dan feedback |

## Pemisahan data
- Raw/staging mempertahankan payload asli untuk audit dan reprocessing.
- Canonical store berisi satu representasi artikel setelah normalisasi dan dedup policy.
- Enrichment store menyimpan hasil NLP secara versioned agar perubahan model tidak menimpa histori.
- Analytics store menyimpan agregat yang dapat dihitung ulang dari enrichment.

## Deployment yang disarankan
Mulai dari worker batch dan database/storage yang telah disetujui perusahaan. Dashboard mengakses agregat dan daftar artikel melalui service/API internal yang tersedia. FastAPI dapat ditambahkan hanya jika dibutuhkan sebagai boundary integrasi baru. Tidak ada asumsi cloud vendor, database, atau sistem internal tertentu.
