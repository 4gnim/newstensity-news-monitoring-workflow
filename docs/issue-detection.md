# Issue Detection & Topic Clustering

## Tujuan
Mengelompokkan artikel yang membahas isu atau subtopik serupa meskipun judul dan redaksinya berbeda. Issue detection bukan sekadar pencarian satu keyword: konteks, entitas, dan kemiripan semantik perlu dipertimbangkan.

## Pipeline yang diusulkan
1. **Keyword extraction:** memberi sinyal istilah dominan dan membantu analis memahami isi cluster.
2. **Named Entity Recognition (NER):** mendeteksi tokoh, lembaga, lokasi, dan organisasi yang muncul dalam artikel.
3. **Semantic representation:** mengubah teks menjadi embedding untuk mengukur kedekatan makna; pilihan model embedding bahasa Indonesia/multibahasa perlu diuji pada korpus perusahaan.
4. **Clustering:** kelompokkan artikel berdasarkan kemiripan; opsi awal dapat berupa threshold similarity atau HDBSCAN pada embedding. KMeans/TF-IDF bisa menjadi baseline jika jumlah cluster awal diketahui.
5. **Cluster labeling:** beri nama isu berdasarkan kata kunci dan contoh artikel; analis mengonfirmasi label.
6. **Temporal tracking:** hubungkan cluster lintas waktu agar isu yang berkembang dapat dipantau.

## Baseline demonstrasi
`src/issue_detection.py` menggunakan TF-IDF n-gram + KMeans serta dictionary entity sederhana. Cluster ID bersifat arbitrer, bukan label isu final. Kode ini menunjukkan pola teknis, bukan validasi kualitas clustering bahasa Indonesia.

## Risiko dan kontrol
- Satu artikel dapat memuat beberapa isu; pertimbangkan multi-label atau segmentasi per paragraf jika dibutuhkan.
- Isu berbeda dapat berbagi entitas/keyword; jangan menyamakan co-occurrence dengan kesamaan topik.
- Cluster dapat berubah ketika volume/data window berubah; simpan versi model dan strategi penautan cluster.
- Artikel sensitif dan nama entitas perlu review.
