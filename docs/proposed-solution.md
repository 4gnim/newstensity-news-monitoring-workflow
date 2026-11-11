# Proposed Solution

## Arah solusi
Menerapkan **AI-powered news monitoring workflow** sebagai lapisan pengolahan dan enrichment yang dapat diintegrasikan dengan data source yang sudah tersedia. Solusi dirancang modular sehingga ingestion, quality checks, issue detection, sentiment classification, dan analytics dapat dipakai sebagian atau seluruhnya sesuai gap sistem saat ini.

## Prinsip desain
- **Integration-first:** inventarisasi API, database, export, atau pipeline internal sebelum membangun pengumpulan data baru.
- **Modular:** setiap tahap memiliki input/output dan dapat dievaluasi terpisah.
- **Traceable:** simpan URL/sumber, waktu publikasi dan pengambilan, fingerprint, versi model, confidence, dan status review.
- **Human-in-the-loop:** hasil yang ambigu atau berisiko ditinjau analis.
- **Incremental delivery:** mulai dari batch dan baseline, lalu tingkatkan berdasarkan hasil pilot.

## Alur yang diusulkan
1. **News Data Collection** - adapter ke existing data source sebagai pilihan pertama; RSS/API/Excel import sebagai alternatif.
2. **Automated Data Processing** - validasi skema, normalisasi, pemeriksaan tanggal/konten, deduplikasi exact match dan kandidat near-duplicate.
3. **Issue Detection & Topic Clustering** - keyword extraction dan NER untuk sinyal; semantic similarity dan clustering untuk mengelompokkan artikel.
4. **AI Sentiment Analysis** - klasifikasi positif/negatif/netral pada unit analisis yang disepakati (artikel atau artikel terhadap entitas/isu).
5. **News Analytics** - volume, distribusi/tren sentimen, sebaran media, dan isu yang paling banyak dibahas.
6. **Dashboard & Automated Report** - filter, daftar artikel, visualisasi, ekspor, dan alert berbasis ambang.
7. **Human review** - verifikasi, koreksi, serta feedback untuk evaluasi berkala.

## Output minimum untuk analis
- Ringkasan isu dan volume artikel menurut waktu.
- Distribusi sentimen dengan tautan ke artikel sumber.
- Tren perubahan sentimen dan media yang paling aktif.
- Kelompok artikel serupa beserta contoh judul/entitas.
- Indikator data belum valid, duplikat, dan hasil yang menunggu review.

## Keputusan yang belum boleh diasumsikan
Sumber data resmi, volume harian, SLA, skema data internal, definisi sentimen, bahasa/campuran bahasa, target deployment, mekanisme alert, dan hak akses harus dikonfirmasi dengan pemilik sistem.
