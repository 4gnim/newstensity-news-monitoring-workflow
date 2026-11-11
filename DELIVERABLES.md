# Deliverables & Verification

## Main deliverables

- `docs/Newstensity_AI_Powered_News_Monitoring_Workflow_Proposal.pptx` - presentasi 19 slide.
- `docs/Newstensity_AI_Powered_News_Monitoring_Workflow_Proposal.pdf` - PDF dari presentasi.
- `docs/` - dokumentasi teknis: problem statement, solusi, workflow, arsitektur, strategi ingestion dan processing, issue detection, sentiment analysis, analytics, human-in-the-loop, technology stack, evaluasi, roadmap, asumsi, dan status implementasi.
- `diagrams/` - sumber diagram Mermaid yang dapat diedit untuk workflow, architecture, dan data flow.
- `data/sample_news.csv` - 500 artikel sintetis untuk demonstrasi.
- `src/` - demonstrasi lokal untuk data processing, issue detection, dan baseline sentiment berbasis leksikon.
- `dashboard/app.py` - dashboard demonstrasi menggunakan Streamlit.
- `notebooks/workflow-demonstration.ipynb` - notebook walkthrough.
- `tests/` - unit test dasar untuk fungsi pipeline.

## Verification performed

- Presentasi terdiri dari 19 slide; PDF telah dirender untuk pemeriksaan visual.
- `python -m py_compile src/*.py dashboard/app.py` berhasil.
- `python -m unittest discover -s tests -v`: 5 test berhasil.
- `python src/run_demo.py`: 501 baris input (500 artikel sintetis + 1 duplikat uji) menjadi 500 baris unik.
- Baseline sentimen menghasilkan 120 Positif, 230 Negatif, dan 150 Netral pada dataset sintetis yang labelnya dikontrol.
- Dashboard Streamlit berhasil dijalankan secara lokal setelah dependensi pada `requirements.txt` dipasang. Deployment online belum dilakukan.

## Limitations

- Dataset, identitas penerbit, dan URL bersifat sintetis.
- Sentiment analysis menggunakan baseline kata kunci, bukan model terlatih dan belum divalidasi pada berita nyata.
- Issue clustering menggunakan TF-IDF + KMeans sebagai baseline demonstrasi; label cluster perlu ditafsirkan oleh analis.
- Belum tersedia konektor RSS/API langsung, crawler, database produksi, scheduler, autentikasi, atau integrasi dengan sistem internal Newstensity.

## Dashboard data-flow note

- Dashboard memvisualisasikan label simulasi dari `data/sample_news.csv`.
- Demo CLI di `src/run_demo.py` menjalankan pipeline terpisah dan menulis hasil ke `data/demo_processed_output.csv`.
- Kedua jalur tersebut belum dihubungkan. Karena itu, grafik dashboard tidak boleh disebut sebagai prediksi model live atau hasil monitoring berita aktual.
