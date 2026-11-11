# News Data Collection Strategy

## Prioritas sumber
1. **Existing data source** - pilihan pertama jika perusahaan sudah memiliki feed, database, API, atau pipeline pengumpulan berita. Integrasikan output-nya dan hindari pengambilan ganda.
2. **RSS feed** - sesuai untuk sumber yang menyediakan feed publik dan struktur relatif konsisten. Perlu penjadwalan, parsing, retry, dan pemeriksaan perubahan format.
3. **News API** - gunakan hanya dengan lisensi, rate limit, dan hak penggunaan konten yang jelas. Simpan metadata serta URL sumber.
4. **Excel/CSV import** - jalur transisi dan fallback untuk data historis atau sumber manual. Terapkan template dan validasi sebelum masuk canonical store.

## Pola ingestion
- Mulai dengan batch terjadwal (misalnya setiap 15-60 menit sebagai nilai awal untuk pilot, bukan SLA final).
- Catat `collected_at`, sumber, request/job ID, status, dan error.
- Terapkan idempotency menggunakan source ID atau fingerprint.
- Pisahkan raw payload dari data yang sudah dinormalisasi.
- Terapkan retry terbatas dan dead-letter/quarantine untuk data gagal.

## Kriteria pemilihan konektor
Akses resmi, cakupan media, kelengkapan metadata, konsistensi timestamp, biaya, rate limit, lisensi, duplikasi, stabilitas, serta dukungan pagination/incremental sync.

## Hal yang perlu dikonfirmasi
Sumber aktual yang dipakai saat ini, hak akses/API, volume dan frekuensi, field yang tersedia, aturan retensi, dan apakah konten penuh artikel boleh diproses atau hanya metadata/snippet.
