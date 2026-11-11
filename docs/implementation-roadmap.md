# Implementation Roadmap

Estimasi berikut bersifat indikatif untuk diskusi awal; durasi aktual bergantung pada ukuran tim, akses data, dan integrasi yang tersedia.

| Fase | Fokus | Aktivitas | Kriteria keluar |
|---|---|---|---|
| 0. Discovery | Validasi kebutuhan & existing system | Inventarisasi sumber, skema, API, volume, use case analis, definisi sentimen, akses/lisensi | Gap dan data contract disetujui |
| 1. Data foundation | Ingestion + quality | Adapter ke satu sumber yang sah, raw/staging, validasi, normalisasi, dedup exact | Data lineage dan quality report tersedia |
| 2. NLP pilot | Issue + sentiment baseline | Labeling guideline, baseline NER/embedding/clustering/sentimen, review queue | Evaluasi offline dan review analis selesai |
| 3. Analyst pilot | Analytics + dashboard | KPI, filter, sumber artikel, laporan, alert sederhana | Analis dapat menyelesaikan use case dengan waktu terukur |
| 4. Hardening | Reliability & governance | Monitoring, retry, access control, audit, drift checks, model versioning | Persetujuan operasional dan security |

## MVP recommendation
Batasi pilot pada satu sumber data dan satu use case isu. Mulai dari batch, ukur baseline waktu kerja analis, lalu perluas sumber/topik setelah kualitas dan manfaatnya terbukti.
