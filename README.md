# Newstensity News Monitoring Workflow

**Rancangan workflow AI untuk otomatisasi pengolahan dan monitoring pemberitaan**

> **Status:** solution design + demonstrasi teknis terbatas. Bukan implementasi produksi dan bukan representasi arsitektur internal Newstensity.

## Ringkasan

Repository ini menerjemahkan kebutuhan yang muncul dalam wawancara menjadi workflow yang menghubungkan pengumpulan data berita, pemrosesan otomatis, deteksi isu, analisis sentimen, analitik, serta dashboard untuk analis. Prinsip desain utamanya adalah **integration-first**: integrasikan sumber data dan kapabilitas yang sudah tersedia sebelum mempertimbangkan crawler atau platform baru.

## Struktur repository

```text
newstensity-news-monitoring-workflow/
├── README.md
├── DELIVERABLES.md
├── LICENSE
├── requirements.txt
│
├── docs/
│   ├── problem-statement.md
│   ├── proposed-solution.md
│   ├── workflow.md
│   ├── system-architecture.md
│   ├── data-collection-strategy.md
│   ├── automated-processing.md
│   ├── issue-detection.md
│   ├── sentiment-analysis.md
│   ├── analytics-and-dashboard.md
│   ├── human-in-the-loop.md
│   ├── technology-stack.md
│   ├── evaluation-strategy.md
│   ├── implementation-roadmap.md
│   ├── assumptions-and-questions.md
│   ├── implementation-status.md
│   ├── Newstensity_AI_Powered_News_Monitoring_Workflow_Proposal.pptx
│   └── Newstensity_AI_Powered_News_Monitoring_Workflow_Proposal.pdf
│
├── diagrams/
│   ├── workflow.mmd
│   ├── architecture.mmd
│   └── data-flow.mmd
│
├── data/
│   ├── README.md
│   ├── sample_news.csv
│   └── demo_processed_output.csv
│
├── notebooks/
│   └── workflow-demonstration.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── issue_detection.py
│   ├── sentiment_analysis.py
│   └── run_demo.py
│
├── dashboard/
│   └── app.py
│
└── tests/
    └── test_pipeline.py
```

## Isi repository

- `docs/` - problem statement, rancangan solusi, strategi teknis, evaluasi, roadmap, asumsi, dan status implementasi.
- `diagrams/` - diagram Mermaid untuk workflow, arsitektur, dan aliran data.
- `data/sample_news.csv` - 500 artikel sintetis untuk demo; bukan berita aktual.
- `src/` - demonstrasi validasi/normalisasi/deduplikasi, ekstraksi entitas sederhana, clustering TF-IDF + KMeans, dan baseline sentimen leksikon.
- `dashboard/app.py` - dashboard Streamlit berbasis dataset simulasi.
- `notebooks/workflow-demonstration.ipynb` - notebook walkthrough.
- `tests/` - pengujian dasar untuk data processing dan sentiment baseline.
- `docs/Newstensity_AI_Powered_News_Monitoring_Workflow_Proposal.pptx` dan `docs/Newstensity_AI_Powered_News_Monitoring_Workflow_Proposal.pdf` - deck utama.

## Cara menjalankan demonstrasi

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/run_demo.py
streamlit run dashboard/app.py
```

Jalankan unit test dari root repository:

```bash
python -m unittest discover -s tests -v
```

## Batasan yang perlu dipahami

1. Seluruh isi `sample_news.csv` dibuat secara sintetis. Nama sumber dan URL `.example` juga fiktif.
2. Kolom `sentiment_simulation` dan `issue_group_simulation` merupakan label kontrol untuk visualisasi, bukan label hasil inferensi.
3. `sentiment_analysis.py` adalah baseline leksikon yang transparan untuk demonstrasi, bukan model AI terlatih dan tidak memiliki klaim akurasi.
4. `issue_detection.py` menjalankan baseline TF-IDF + KMeans. Cluster ID tidak memiliki makna tetap dan harus ditafsirkan dari sampel artikel/kata kunci.
5. Tidak ada konektor API/RSS, crawler, autentikasi, database produksi, scheduler produksi, atau integrasi ke sistem internal perusahaan di repository ini.
6. Sentimen berita menggambarkan nada/framing artikel yang dianalisis, bukan opini atau preferensi masyarakat.
7. Dashboard membaca data simulasi secara langsung. Pipeline pada `src/run_demo.py` merupakan demonstrasi terpisah dan belum terhubung otomatis ke dashboard.

## Prinsip rancangan

- Pertahankan sistem internal yang sudah berjalan; tambahkan adapter atau tahap enrichment hanya jika terdapat gap yang terverifikasi.
- Pisahkan data mentah, data kanonis, hasil enrichment, dan agregat analitik.
- Simpan jejak sumber, waktu pengambilan, versi model, confidence, serta status review.
- Gunakan human-in-the-loop untuk prediksi ber-confidence rendah, artikel ambigu, dan isu sensitif.
- Mulai dari batch terjadwal; tingkatkan ke near-real-time hanya jika kebutuhan bisnis dan kapasitas sumber mendukung.

## Navigasi dokumen

Mulai dari `docs/problem-statement.md`, lanjutkan ke `docs/proposed-solution.md`, `docs/workflow.md`, dan `docs/system-architecture.md`. Untuk memahami batas komponen yang sudah dibuat dan yang masih konseptual, baca `docs/implementation-status.md`. Ringkasan isi dan verifikasi tersedia di `DELIVERABLES.md`.
