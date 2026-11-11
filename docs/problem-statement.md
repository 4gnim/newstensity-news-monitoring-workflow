# Problem Statement

## Konteks
Berdasarkan rangkuman kebutuhan wawancara, pengelolaan dan pengolahan data berita masih melibatkan spreadsheet seperti Excel. Pada saat volume berita meningkat, pekerjaan manual berpotensi menambah beban operasional untuk memeriksa format, menghapus duplikasi, menemukan artikel terkait, dan menyusun ringkasan perkembangan isu.

## Rumusan masalah
**Bagaimana merancang workflow berbasis AI yang dapat mengotomatisasi pengumpulan dan pengolahan data berita, mengidentifikasi isu yang sedang berkembang, serta menganalisis sentimen pemberitaan sehingga proses monitoring Newstensity menjadi lebih efisien?**

## Kebutuhan bisnis yang diturunkan
1. Mengurangi pekerjaan input dan pengolahan data berulang.
2. Menjaga format dan kualitas data berita agar konsisten.
3. Mengidentifikasi artikel yang membahas isu serupa walau judul/redaksinya berbeda.
4. Mengelompokkan nada pemberitaan menjadi positif, negatif, atau netral.
5. Menyediakan ringkasan volume, distribusi sentimen, tren waktu, sumber media, dan isu yang banyak dibahas.
6. Menyediakan ruang verifikasi analis untuk hasil ambigu atau sensitif.

## Batas interpretasi
Sentimen artikel tidak sama dengan opini masyarakat. Satu artikel dapat memiliki kutipan dari beberapa pihak dengan pandangan berbeda; karena itu unit analisis, definisi label, dan konteks target (isu/entitas) harus disepakati sebelum penerapan.

## Bukan tujuan proyek
Membangun ulang platform Newstensity, membuat crawler multi-sumber lengkap, melatih model dari nol, membuat AI Agent, atau mengklaim integrasi dengan sistem internal yang belum diperiksa.
