# Evaluation Strategy

| Komponen | Metrik | Cara evaluasi |
|---|---|---|
| Data ingestion | Ingestion success rate, completeness, freshness, retry rate | Bandingkan jumlah record sumber vs diterima; pantau timestamp |
| Data quality | Required-field pass rate, invalid timestamp rate | Rule-based checks dan audit sampel |
| Deduplication | Precision/recall/F1 pasangan duplikat | Label pasangan exact dan near-duplicate oleh reviewer |
| Issue detection | Cluster purity, NMI/ARI (bila ada label), analyst usefulness | Sampel cluster, konsistensi cluster lintas waktu, review analis |
| Sentiment | Macro-F1, precision/recall per kelas, confusion matrix | Test set berlabel dan dipisah secara temporal/sumber |
| Operations | Processing latency, throughput, failure rate | Log per batch dan per tahap |
| Business | Waktu analis per monitoring cycle, jumlah langkah manual, time-to-detect | Baseline sebelum pilot vs sesudah pilot |

## Guardrails evaluasi
- Jangan memakai accuracy saja ketika distribusi kelas tidak seimbang.
- Hindari data leakage: artikel sindikasi/duplikat harus dipertimbangkan ketika split data.
- Laporkan performa per sumber dan per topik jika jumlah sampel memungkinkan.
- Nilai model pada periode waktu yang berbeda dari data pelatihan.
- Dokumentasikan definisi label dan adjudication antar anotator.
- Dataset sintetis pada repository ini tidak dapat dipakai untuk klaim kualitas model.
