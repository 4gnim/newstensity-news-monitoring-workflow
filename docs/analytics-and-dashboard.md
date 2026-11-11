# News Analytics & Dashboard Concept

## KPI dan visualisasi
- **News volume:** jumlah artikel unik per jam/hari dan perubahan terhadap periode pembanding.
- **Sentiment distribution:** proporsi label pada artikel yang lolos dedup dan memiliki label. Selalu tampilkan denominator dan artikel yang belum dianalisis.
- **Sentiment trend:** tren jumlah/proporsi sentimen per waktu; hindari membandingkan proporsi tanpa memperhatikan volume.
- **Media distribution:** volume artikel per media/sumber.
- **Most discussed issues:** isu/cluster dengan volume tertinggi dan laju pertumbuhan.
- **Review queue:** artikel ber-confidence rendah, entitas ambigu, atau isu sensitif.

## Interaksi dashboard
Filter tanggal, media, isu, entitas, dan sentimen; buka artikel sumber; lihat contoh artikel per cluster; ekspor ringkasan; dan atur alert berdasarkan threshold volume/perubahan yang disepakati.

## Dashboard demo
`dashboard/app.py` memakai Streamlit dan Plotly. Ia menampilkan 500 record sintetis, label simulasi, filter, dan visualisasi. Kolom label simulasi digunakan secara eksplisit sebagai data ilustrasi, bukan hasil prediksi model.
