# Persiapan Lingkungan dan Spesifikasi Hardware

Perangkat Keras
CPU: Intel Core i7 atau AMD Ryzen 7
GPU: NVIDIA GTX 1080 Ti atau lebih tinggi (jika menggunakan model berbasis deep learning seperti BERT atau GPT-3)
RAM: Minimal 16 GB (32 GB direkomendasikan)
Storage: SSD dengan minimal 500 GB ruang kosong

Perangkat Lunak
Sistem Operasi: Linux (Ubuntu) atau Windows 10/11
Python: Versi 3.8 atau lebih tinggi
Perpustakaan Python: transformers, nltk, sumy, torch, tensorflow, openai (untuk GPT-3), dll.

# AI Summary Core
1. Metode Abstraktif (Seperti BERT dan GPT-3)

Data Kebutuhan
Ukuran Teks: Bisa menangani teks panjang, tetapi optimal untuk paragraf hingga beberapa halaman.
Volume Data: Beberapa ribu hingga puluhan ribu dokumen untuk pelatihan model dari awal, namun jika menggunakan model pre-trained, beberapa dokumen per eksperimen sudah cukup.
Contoh Data: Artikel berita, makalah akademik, laporan bisnis.

Contoh Penggunaan
Ringkasan artikel berita: 1-2 halaman per artikel, 100-500 artikel.
Ringkasan laporan bisnis: 10-50 halaman per laporan, 10-100 laporan.

2. Metode Ekstraktif (Seperti Sumy dan Gensim)

Data Kebutuhan
Ukuran Teks: Efektif untuk dokumen pendek hingga menengah (beberapa paragraf hingga beberapa halaman).
Volume Data: Ratusan hingga ribuan dokumen untuk mencapai performa yang baik.
Contoh Data: Blog posts, laporan teknis, buku putih.

Contoh Penggunaan
Ringkasan blog posts: 1-3 halaman per post, 100-300 posts.
Ringkasan laporan teknis: 5-20 halaman per laporan, 50-200 laporan.

3. Metode Statistik (Seperti Gensim dengan LSA)

Data Kebutuhan
Ukuran Teks: Optimal untuk dokumen menengah hingga panjang.
Volume Data: Beberapa ratus hingga beberapa ribu dokumen untuk hasil yang baik.
Contoh Data: Buku, disertasi, laporan tahunan.

Contoh Penggunaan
Ringkasan buku: 200-400 halaman per buku, 20-50 buku.
Ringkasan disertasi: 100-300 halaman per disertasi, 50-100 disertasi.
Faktor yang Perlu Dipertimbangkan
Kompleksitas Teks: Teks dengan kalimat kompleks dan banyak informasi membutuhkan lebih banyak data untuk ringkasan yang akurat.
Ketersediaan Data: Akses ke dataset publik seperti CNN/DailyMail, PubMed, atau dataset berita lainnya bisa sangat membantu.
Kualitas Data: Data berkualitas tinggi dengan anotasi yang baik akan memberikan hasil yang lebih baik dibandingkan data mentah.

Contoh Dataset untuk Pelatihan dan Evaluasi
CNN/DailyMail: Digunakan secara luas untuk pelatihan dan evaluasi model ringkasan.
XSum: Dataset yang terdiri dari artikel berita dan ringkasan singkat.
PubMed: Artikel ilmiah dengan abstrak yang bisa digunakan untuk pelatihan model ringkasan medis.

Kebutuhan Penyimpanan Data
Dataset Kecil: 1-10 GB untuk teks pendek dan jumlah dokumen yang terbatas.
Dataset Sedang: 10-50 GB untuk teks menengah dan jumlah dokumen yang lebih banyak.
Dataset Besar: 50 GB atau lebih untuk teks panjang dan jumlah dokumen yang sangat banyak.