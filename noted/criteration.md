### Komponen Sistem



1. **Web Crawler (Scraper)**



   Mengumpulkan berita terkait baja dari web.

   - **Alat**: BeautifulSoup, Scrapy (Pustaka Python)

   - **Tujuan**: Mengumpulkan data halaman web yang berisi berita baja



2. **Database**



   Menyimpan berita yang dikumpulkan.

   - **Alat**: MySQL, PostgreSQL atau basis data NoSQL (seperti MongoDB)

   - **Tujuan**: Menyimpan dan mengelola data berita



3. **Penyaringan dan Analisis Berita**



   Menyaring berita terkait baja dari data yang dikumpulkan.

   - **Alat**: Pustaka NLP (Natural Language Processing, seperti NLTK, spaCy)

   - **Tujuan**: Menganalisis data teks untuk mengidentifikasi berita terkait baja



4. **Sistem Ringkasan**



   Meringkas berita yang telah disaring.

   - **Alat**: Algoritma ringkasan teks (seperti BERT, GPT-3) atau pustaka ringkasan berita sederhana (seperti sumy, Gensim)

   - **Tujuan**: Meringkas berita panjang menjadi ringkasan singkat



5. **Sistem Distribusi**



   Mengirimkan ringkasan berita melalui email atau ponsel.

   - **Alat**: Server email (SMTP), API SMS (seperti Twilio)

   - **Tujuan**: Mendistibusikan ringkasan berita kepada pengguna



### Prosedur



1. **Daftar Sumber Berita**



   - Mengumpulkan daftar sumber berita seperti situs web, halaman beranda TV, halaman beranda perusahaan.



2. **Pengaturan Web Crawler**



   - Menggunakan alat seperti Scrapy untuk mengumpulkan data dari sumber yang ditentukan secara berkala (misalnya, setiap hari, setiap jam).

   - Menyaring data teks yang dibutuhkan dengan mengatur tag HTML, nama kelas, dan filter lainnya.



3. **Penyimpanan Data**



   - Mem-parsing data yang dikumpulkan menjadi bentuk teks dan menyimpannya dalam database.



4. **Penyaringan Berita**



   - Menggunakan teknologi NLP untuk mengidentifikasi berita yang berhubungan dengan baja menggunakan kata kunci (misalnya, "baja", "steel", "metalurgi").

   - Memberi tag atau menandai berita yang telah disaring.



5. **Ringkasan Berita**



   - Meneruskan berita terkait baja yang telah diidentifikasi melalui algoritma ringkasan untuk menghasilkan ringkasan singkat dan padat.



6. **Pengaturan Distribusi Otomatis**



   - Mengatur sistem distribusi email dan SMS. Menggunakan server SMTP untuk mengirim email dan API seperti Twilio untuk mengirim SMS.



7. **Distribusi Periodik**



   - Mengatur jadwal untuk mendistribusikan ringkasan berita (misalnya, setiap pagi jam 8).

   - Mengirimkan ringkasan berita melalui email dan SMS secara otomatis sesuai jadwal.
