# AI Sentiment Analysis

## Definisi operasional
Klasifikasi positif, negatif, dan netral dilakukan terhadap **nada/framing pemberitaan** mengenai isu atau entitas target yang dipilih. Ini tidak mengukur sikap seluruh masyarakat, tingkat dukungan politik, atau opini publik.

## Strategi model
1. Tetapkan unit analisis: keseluruhan artikel, judul, paragraf, atau artikel terhadap entitas target.
2. Susun pedoman anotasi dan contoh borderline untuk tiga label.
3. Buat dataset berlabel yang representatif dan pisahkan train/validation/test berdasarkan waktu atau sumber untuk mengurangi leakage.
4. Mulai dari baseline sederhana (lexicon atau model pretrained yang sesuai) dan bandingkan dengan model bahasa Indonesia/multibahasa yang diuji pada data internal.
5. Evaluasi macro-F1 dan precision/recall per kelas; periksa confusion matrix dan sampel salah klasifikasi.
6. Atur confidence threshold dan review queue. Hindari mengeluarkan label pasti ketika confidence rendah.

## Baseline dalam repository
`src/sentiment_analysis.py` memakai daftar kata positif/negatif transparan. Ia berguna untuk memperlihatkan interface input-output dan alur agregasi, tetapi tidak memahami negasi, sarkasme, konteks kutipan, intensitas, atau target sentimen. Tidak ada klaim akurasi.

## Hal sensitif
- Kutipan dari narasumber dapat berlawanan dengan framing penulis.
- Artikel dapat netral secara keseluruhan tetapi mengutip pendapat negatif/positif.
- Label harus menjelaskan apakah sentimen ditujukan pada isu, tokoh, kebijakan, atau pihak tertentu.
- Model tidak boleh digunakan sebagai satu-satunya dasar keputusan reputasi atau penilaian individu.
