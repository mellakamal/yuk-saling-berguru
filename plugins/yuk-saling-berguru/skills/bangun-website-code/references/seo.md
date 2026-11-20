# SEO untuk Web Buatan Non-Programmer

Dipakai di Tahap 6 dan Tahap 9. Untuk web artist, kerjakan juga bagian Khusus web artist di akhir file ini. SEO tidak menjamin posisi di Google. Halaman baru butuh hari sampai minggu untuk terindeks dan beberapa bulan untuk naik. Jangan menjanjikan peringkat.

## Kata kunci (dikerjakan saat menyusun blueprint)
1. Tanya kata yang diketik calon klien di Google, misalnya "commission VTuber model" atau "custom character illustration". Tanya area layanan hanya kalau brand melayani klien lokal.
2. Beri satu kata kunci utama dan satu sampai dua pendukung per halaman. Satu halaman, satu topik.
3. Pakai bahasa calon klien, bukan istilah internal. Tulis di kolom Kata kunci pada tabel Halaman di `BLUEPRINT.md`.
4. Teks halaman ditulis untuk manusia. Jangan mengulang kata kunci berlebihan.

## Tahap 6: dikerjakan di kode
Kerjakan per halaman, lalu tampilkan hasilnya dalam satu tabel (halaman, judul, deskripsi, kata kunci) agar artist bisa mengoreksi.

1. Judul halaman unik, sekitar 50 sampai 60 karakter, kata kunci halaman di depan, nama brand di belakang.
2. Deskripsi unik, sekitar 140 sampai 160 karakter, ditulis sebagai ajakan yang jujur sesuai isi halaman.
3. Satu H1 per halaman, lalu H2 dan H3 berurutan. Alamat halaman pendek, huruf kecil, dipisah tanda hubung.
4. Gambar pratinjau saat link dibagikan (1200 x 630), judul dan deskripsi pratinjau, dan favicon.
5. Teks alternatif yang menjelaskan isi tiap gambar, nama file gambar yang bermakna, foto diperkecil, format ringan seperti WebP, dan gambar di bawah layar dimuat belakangan.
6. Atribut bahasa halaman (lang) yang benar, tautan canonical, dan tautan antarhalaman dengan teks yang jelas, bukan "klik di sini".
7. Berkas `sitemap.xml` dan `robots.txt`. Tag noindex hanya boleh ada di halaman 404. Di halaman lain, hapus kalau tertinggal.
8. Data terstruktur schema.org yang sesuai (Organization, atau Person untuk artist solo), hanya berisi data yang ada di blueprint. Jangan menambah rating, ulasan, atau alamat karangan.
9. Halaman 404 yang ramah.
10. Jalankan skrip pengecek pada folder yang tayang: `python3 -I <folder skill>/references/cek-seo.py site`. Jangan jalankan pada folder proyek, karena `desain-kasar.html` dan file di `bahan/` ikut terperiksa. Skrip memeriksa panjang judul dan deskripsi, judul atau deskripsi kembar, satu H1, canonical, lang, viewport, gambar pratinjau, alt gambar, tautan rusak, noindex, dan isi sitemap. Perbaiki sampai hasilnya LOLOS. Jangan menebak panjang teks. Kalau skrip tidak bisa dijalankan, katakan jujur dan hitung panjangnya dengan cara lain.
11. Laporan kecepatan dengan Lighthouse kalau terpasang, skor sebelum dan sesudah. Kalau tidak bisa dijalankan, katakan jujur dan lewati.

Selama domain belum ada, alamat di sitemap, canonical, dan gambar pratinjau memakai alamat sementara hosting. Kalau web belum pernah tayang, alamat sementara belum diketahui (di Cloudflare bentuknya bergantung nama proyek). Pakai satu alamat contoh yang dicatat di CLAUDE.md, lalu ganti di semua halaman setelah penayangan pertama. Perbarui ke domain final di Tahap 8, dan alihkan alamat sementara ke domain baru.

## Tahap 9: daftar ke Google
Dikerjakan setelah web tayang di alamat finalnya.

1. Artist: buka Google Search Console dengan akun Google sendiri, pilih Add property. Jenis Domain diverifikasi lewat DNS, jenis URL prefix lewat tag atau berkas.
2. Claude: kalau artist memilih URL prefix, pasang tag atau berkas verifikasi di web. Cek `sitemap.xml` bisa dibuka, `robots.txt` tidak memblokir halaman penting, dan tidak ada noindex. Laporkan hasilnya.
3. Artist: di Search Console buka menu Sitemaps, masukkan alamat sitemap, klik Submit. Buka URL Inspection, tempel alamat beranda, klik Request indexing.
4. Artist, khusus brand yang punya studio atau area layanan lokal: buat atau klaim Google Business Profile dengan data yang sama persis dengan web, lalu pasang link web di profil itu.
5. Opsional: impor web ke Bing Webmaster Tools dari akun Search Console.
6. Claude menulis daftar periksa pengecekan ulang di `README.md`. Setelah 3 sampai 7 hari, periksa menu Pages (halaman terindeks atau tidak, dan alasannya). Setelah 2 sampai 4 minggu, periksa menu Performance (klik, tayangan, kata yang membawa pengunjung). Terindeks tidak berarti langsung di halaman pertama.

## Khusus web artist
Dikerjakan di Tahap 6 bersama daftar di atas. Untuk artist, Google Images sering jadi pintu masuk klien, jadi gambar diperlakukan sebagai isi utama.

1. **Galeri terbaca Google.** Setiap karya memakai tag `img` di HTML dengan `src` asli, alt yang menjelaskan isi karya, dan keterangan singkat di dekatnya. Google tidak mengindeks gambar latar CSS. Lightbox dan filter boleh memakai JavaScript, tetapi gambarnya sudah ada di HTML sejak halaman dimuat. Gambar pertama di layar tidak dimuat belakangan.
2. **Sitemap gambar.** Tambahkan `image:image` di `sitemap.xml` untuk karya di halaman Portfolio dan Beranda.
3. **Karya unggulan punya keterangan sendiri.** Minimal judul, jenis karya, dan satu kalimat cerita di dekat gambar. Kalau karya atau seri cukup banyak, buat halaman per seri (misalnya `portfolio/vtuber-3d.html`) dengan judul dan deskripsi sendiri.
4. **Nama artist melekat di gambar.** Tambahkan data terstruktur `ImageObject` untuk karya unggulan dengan `creator`, `creditText`, dan `copyrightNotice`. Kalau artist punya halaman aturan pemakaian karya (misalnya di ToS), isi `license` dan `acquireLicensePage` dengan alamat itu. Jangan mengarang lisensi yang tidak ada.
5. **Identitas artist.** Halaman Tentang berisi cerita singkat, gaya karya, dan pengalaman nyata dari bahan. Data `Person` atau `Organization` memakai `sameAs` berisi semua akun resmi artist (media sosial, VGen, Skeb, ArtStation, toko), sama persis dengan link di web dan bio. Nama brand ditulis sama di semua tempat.
6. **Crawler AI sesuai pilihan artist** di bagian 8 blueprint. Googlebot tidak pernah diblokir karena dipakai Google Search dan AI Overviews.
   - Izinkan pencarian AI tapi tolak pelatihan (saran untuk kebanyakan artist): di `robots.txt` blokir `GPTBot`, `ClaudeBot`, `CCBot`, `Google-Extended`, dan `Applebot-Extended`. Biarkan `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, dan `Bingbot`.
   - Tolak semua crawler AI: blokir juga crawler pencarian AI di atas. Akibatnya web tidak muncul di jawaban ChatGPT, Claude, atau Perplexity.
   - Izinkan semua: tidak ada aturan khusus.
   Jelaskan ke artist bahwa `robots.txt` adalah permintaan, bukan kunci. Crawler yang tidak patuh tetap bisa mengambil gambar, jadi watermark dan ukuran gambar web dari `keamanan.md` tetap berguna. Cek nama crawler terbaru di dokumentasi tiap perusahaan sebelum menulis.
7. **Web dua bahasa.** Kalau ada versi EN dan ID, tiap versi punya alamat sendiri (misalnya `/` dan `/id/`), tag `hreflang` yang saling menunjuk ditambah `x-default`, dan `lang` yang benar di tiap halaman. Jangan mengganti bahasa hanya dengan JavaScript di alamat yang sama.
8. **Video demo.** Untuk VTuber dan Live2D, sematkan video dari YouTube dengan judul dan deskripsi yang memuat kata kunci, dan tambahkan data terstruktur `VideoObject` (nama, deskripsi, gambar mini, tanggal unggah).
9. **Ukur hasil.** Search Console untuk data dari Google. Kalau artist ingin tahu jumlah pengunjung, tawarkan analitik yang ringan dan ramah privasi seperti Cloudflare Web Analytics, dan sebut di kalimat data pada halaman. Peringkat web global seperti Alexa sudah ditutup sejak Mei 2022. Pengganti untuk mengintip web lain adalah perkiraan dari Semrush, Ahrefs, atau Similarweb, bukan data pasti.
