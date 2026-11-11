# Automated Data Processing

## Tahapan
1. **Schema mapping:** memetakan variasi field sumber ke skema kanonis.
2. **Validation:** cek field wajib, URL, format tanggal, bahasa, dan konten kosong. Record bermasalah dikarantina, bukan dibuang tanpa jejak.
3. **Cleaning:** trim, normalisasi whitespace, parsing tanggal/timezone, dan normalisasi encoding. Jangan menghapus tanda baca/angka secara agresif jika dapat mengubah arti judul.
4. **Deduplication:** exact duplicate memakai source ID/fingerprint; near-duplicate menggunakan similarity judul/isi sebagai kandidat untuk dicek dengan threshold terkalibrasi.
5. **Normalization:** samakan nama media, zona waktu, format bahasa, dan kategori sumber.
6. **Audit metadata:** simpan alasan validasi, fingerprint, duplikat asal, waktu proses, dan versi pipeline.

## Kebijakan deduplikasi
Satu artikel yang sama dapat disalin atau diperbarui oleh sumber berbeda. Karena itu, jangan menghapus semua artikel dengan judul mirip secara otomatis. Exact duplicate dapat digabung sesuai kebijakan; near-duplicate perlu mempertahankan relasi antarartikel dan diputuskan berdasarkan use case monitoring.

## Demonstrasi repository
`src/data_processing.py` mengimplementasikan normalisasi ringan, parsing timestamp, fingerprint judul+isi, dan penghapusan exact duplicate. Ini tidak mencakup near-duplicate production-grade, crawling, atau quality rules perusahaan.
