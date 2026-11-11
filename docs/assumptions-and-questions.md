# Assumptions & Open Questions

## Asumsi sementara
1. Newstensity memiliki atau dapat menyediakan data berita melalui export, API, database, atau mekanisme resmi lain. Ini perlu diverifikasi.
2. Artikel dapat diproses setidaknya pada level metadata dan teks yang diizinkan. Hak penggunaan konten belum diketahui.
3. Monitoring isu dilakukan oleh analis yang membutuhkan daftar artikel, tren, dan filter.
4. Batch processing dapat diterima sebagai titik awal; kebutuhan latency belum ditentukan.
5. Bahasa utama dan variasi bahasa artikel perlu dipastikan dari data aktual.

## Pertanyaan untuk user / pemilik sistem
- Sumber berita apa yang sudah digunakan saat ini? Apakah tersedia API, database view, export, atau message queue?
- Field apa saja yang tersedia (judul, isi, URL, media, tanggal terbit, kategori, author, bahasa)?
- Berapa volume berita per hari dan berapa lama data perlu disimpan?
- Apakah analisis sentimen dilakukan pada keseluruhan artikel atau terhadap entitas/isu tertentu?
- Bagaimana pedoman label positif, negatif, dan netral saat artikel memuat kutipan yang berlawanan?
- Apakah ada dataset label historis dan contoh hasil analisis analis?
- Bagaimana analis saat ini mendefinisikan isu viral dan kapan alert perlu dikirim?
- Siapa yang boleh melihat teks penuh, ekspor, dan hasil analisis?
- Infrastruktur, database, dashboard, scheduler, dan standar security apa yang sudah tersedia?
- Bagaimana keberhasilan pilot diukur: waktu kerja, coverage berita, kualitas cluster, atau kualitas sentimen?

## Hal yang tidak diasumsikan
Dokumen ini tidak mengasumsikan arsitektur, vendor cloud, database, kemampuan crawler, model, ataupun dashboard internal Newstensity. Semua keputusan tersebut menunggu konfirmasi.
