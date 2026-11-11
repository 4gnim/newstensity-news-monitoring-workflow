# Proposed AI-Powered News Monitoring Workflow

Diagram sumber: [`../diagrams/workflow.mmd`](../diagrams/workflow.mmd).

| Tahap | Input | Aktivitas | Output | Kontrol utama |
|---|---|---|---|---|
| 1. News Data Collection | Existing source, RSS/API, Excel/CSV | Ambil data melalui adapter, simpan raw payload, catat waktu & asal | Raw article records | Rate limit, akses resmi, retry, source provenance |
| 2. Automated Data Processing | Raw records | Schema mapping, cleaning, validation, normalization, deduplication | Canonical article records | Required fields, timestamp, fingerprint, quarantine |
| 3. Issue Detection & Topic Clustering | Canonical title/body | Keyword extraction, NER, semantic similarity, clustering | Issue/cluster ID, entities, keywords | Threshold, cluster inspection, analyst mapping |
| 4. AI Sentiment Analysis | Article text + target issue/entity | Classify positive/negative/neutral and confidence | Label, score, model version | Evaluation per class, confidence threshold, review queue |
| 5. News Analytics | Enriched articles | Aggregate by time, sentiment, issue, and source | Metrics and trends | Define denominator, dedupe policy, late-arriving data |
| 6. Dashboard & Automated Report | Aggregates + article references | Visualize, filter, export, notify by configured rules | Analyst-facing insights | Link back to source, alert thresholds, access control |
| Human-in-the-loop | Review queue | Verify uncertain, ambiguous, sensitive cases | Corrected labels and issue mappings | Audit trail and reviewer guidance |

## Urutan eksekusi
Tahap 1-2 menyiapkan data yang dapat dipercaya. Tahap 3-4 menambahkan interpretasi AI. Tahap 5-6 menerjemahkan hasil menjadi informasi operasional. Human review melintasi tahap 3-4 dan menjadi masukan evaluasi.

## Mode pemrosesan
Batch terjadwal direkomendasikan untuk MVP karena lebih sederhana untuk integrasi, observabilitas, dan pengendalian biaya. Incremental/near-real-time dapat dipertimbangkan ketika sumber mendukung webhook/stream dan analis memang membutuhkan pembaruan berlatensi rendah.
