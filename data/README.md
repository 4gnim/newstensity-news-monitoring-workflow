# Dataset README

`sample_news.csv` berisi 500 baris artikel sintetis untuk demo. Semua judul dan isi diawali/ditandai SIMULASI; nama media dan URL `.example` fiktif.

Kolom penting: `article_id`, `source`, `source_url`, `published_at`, `collected_at`, `title`, `body`, `language`, `issue_group_simulation`, `sentiment_simulation`, `is_simulation`.

Distribusi label kontrol: Positif 120, Negatif 230, Netral 150. Kolom `_simulation` bukan prediksi model dan tidak boleh dipakai untuk klaim performa.
