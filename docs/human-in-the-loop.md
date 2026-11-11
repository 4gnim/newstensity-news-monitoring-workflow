# Human-in-the-Loop

## Kapan perlu review
- Confidence di bawah threshold yang ditentukan dari validasi.
- Artikel membahas lebih dari satu isu atau beberapa entitas.
- Artikel berupa opini, satire, kutipan berlapis, atau judul clickbait.
- Isu sensitif/berdampak tinggi atau terdapat konflik antarindikator model.
- Cluster baru, cluster pecah/bergabung, atau perubahan volume yang tidak biasa.

## Mekanisme review
1. Tampilkan artikel, sumber, konteks isu, prediksi, confidence, dan alasan masuk antrean.
2. Analis mengonfirmasi/mengoreksi label dan menambahkan catatan singkat.
3. Simpan reviewer, waktu, nilai awal, nilai koreksi, serta versi model.
4. Masukkan koreksi ke dataset evaluasi setelah pemeriksaan kualitas; jangan otomatis melatih ulang tanpa kurasi.

## Prinsip
Human review bukan sekadar fallback. Ia adalah mekanisme kontrol kualitas dan sumber data evaluasi. Keputusan final tetap mempertimbangkan konteks dan kebijakan editorial/bisnis perusahaan.
