# Technology Stack (Proposed)

| Layer | Opsi teknologi | Alasan | Catatan keputusan |
|---|---|---|---|
| Data ingestion | Existing connector, Python adapters, RSS parser, API client | Integrasi sumber secara modular | Prioritaskan konektor internal; library spesifik dipilih setelah inventarisasi |
| Data processing | Python, pandas, Pydantic | Ekosistem data, transformasi, validasi skema | Demonstrasi memakai pandas; validasi produksi dapat memakai Pydantic |
| Storage | Database/data lake yang sudah disetujui perusahaan; PostgreSQL sebagai opsi | Memisahkan raw, canonical, enrichment, aggregate | Jangan memilih database baru sebelum tahu platform yang tersedia |
| NLP / features | spaCy atau library NER Indonesia; TF-IDF baseline | Ekstraksi entitas dan fitur teks | Uji model pada bahasa, domain, dan ejaan data aktual |
| Semantic similarity | Sentence Transformers / embedding service yang disetujui | Mengukur kemiripan makna | Evaluasi kualitas, biaya, latency, dan kebijakan data |
| Topic clustering | scikit-learn baseline; HDBSCAN/BERTopic sebagai opsi | Mengelompokkan artikel | Pilih berdasarkan stabilitas cluster dan kebutuhan label |
| Sentiment | Pretrained Indonesian/multilingual model yang tervalidasi | Mengurangi kebutuhan training dari nol | Bandingkan macro-F1 dan per-class metrics sebelum dipilih |
| Orchestration | Scheduler/job runner yang sudah ada; cron/Celery sebagai opsi | Batch processing dan retry | Belum dibutuhkan untuk demonstrasi lokal |
| API integration | Existing API; FastAPI bila perlu service baru | Boundary integrasi yang jelas | Hindari backend tambahan jika sistem saat ini sudah menyediakan API |
| Dashboard | Existing analyst UI; Streamlit untuk prototype | Validasi kebutuhan tampilan dengan cepat | Streamlit di repo hanya demo |
| Observability | Structured logs + metrics + job status | Menemukan kegagalan data/model | Retention dan akses mengikuti kebijakan perusahaan |

## Prinsip pemilihan
Teknologi final ditentukan setelah konfirmasi akses, lisensi konten, volume, SLA, kemampuan tim, infrastruktur, dan kebijakan keamanan data. Daftar di atas adalah opsi rancangan, bukan klaim bahwa Newstensity memakai teknologi tersebut.
