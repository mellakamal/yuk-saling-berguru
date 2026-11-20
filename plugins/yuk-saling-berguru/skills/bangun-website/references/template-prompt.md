# Template Prompt untuk Claude Code

Setiap prompt mengikuti susunan ini. Isi bagian dalam kurung siku dari blueprint. Tulis dalam bahasa Indonesia, kecuali pengguna meminta lain.

## Susunan baku

```
Aku sedang membangun website [nama] dan aku bukan programmer. Tolong pandu aku pelan-pelan dan jelaskan setiap langkah dengan bahasa sehari-hari.

Baca dulu CLAUDE.md dan BLUEPRINT.md sebelum mulai. Sekarang kita mengerjakan Tahap [nomor]: [nama tahap].

Yang perlu dikerjakan di tahap ini:
1. ...
2. ...
3. ...

Aturan:
- Kerjakan hanya tahap ini. Jangan mengerjakan tahap berikutnya.
- Kalau ada pilihan atau ada yang kurang jelas, tanya aku dulu dengan pilihan yang sederhana.
- Kalau butuh login, akun, atau kunci rahasia, berhenti dan jelaskan apa yang harus aku lakukan sendiri. Jangan minta aku menempelkan password atau kunci di chat.
- Setelah selesai, tunjukkan pratinjau yang bisa aku buka.
- Sebelum commit, perbarui README.md, CLAUDE.md, dan Catatan perubahan di BLUEPRINT.md sesuai perubahan di tahap ini. Lalu simpan progres dengan commit berpesan jelas.

Di akhir, tuliskan ringkasan pendek:
- Apa yang sudah dibuat
- Cara aku mengecek hasilnya
- Apa yang masih kurang atau perlu keputusanku
```

## Isi khusus per tahap

**Tahap 1, menyiapkan proyek dan semua halaman.** Tidak perlu prompt panjang. Pengguna cukup mengetik `Baca BLUEPRINT.md lalu bangun websitenya` di Claude Code, karena semua petunjuk sudah ada di bagian 0 `BLUEPRINT.md`. GitHub baru disambungkan menjelang Tayang.

**Tahap 2, merapikan tampilan.** Sebut warna, huruf, dan kesan dari blueprint, serta koreksi pengguna dari pratinjau Tahap 1. Halaman di luar standar ditambahkan di sini. Pratinjau dibuka di browser.

**Tahap 3, isi halaman.** Sebut lokasi folder bahan. Minta karya Tampil dipasang besar dengan urutan terbaik di atas, harga, ToS, dan FAQ dipakai persis seperti bahan, foto diperkecil ukurannya agar ringan, dan bagian yang belum ada bahannya ditandai "belum ada", tidak diisi karangan. Klaim kemampuan, jumlah klien, dan testimoni hanya dipakai kalau pengguna yang memberikannya.

**Tahap 4, fitur.** Satu fitur per prompt kalau fiturnya rumit. Sebut tingkat web dari bagian 8 blueprint. Fitur yang butuh tingkat lebih tinggi (misalnya form yang datanya disimpan sendiri) dibahas dulu dengan pengguna di chat. Untuk form order, sebut layanan form yang dipilih (Google Form, Tally, atau Formspree) dan minta jawabannya dicoba sampai masuk. Minta Claude Code menjelaskan cara mencoba fiturnya.

**Tahap 5, rapi di HP.** Minta pengecekan di ukuran layar HP, tablet, dan laptop, lalu perbaiki yang terpotong atau terlalu kecil.

**Tahap 6, SEO dasar dan kecepatan.** Sebut kata kunci tiap halaman dari tabel Halaman di blueprint dan alamat sementara hosting. Minta Claude Code mengerjakan dan melaporkan per halaman:
1. Judul halaman unik, sekitar 50 sampai 60 karakter, kata kunci halaman di depan dan nama brand di belakang.
2. Deskripsi unik, sekitar 140 sampai 160 karakter, ditulis sebagai ajakan yang jujur sesuai isi halaman.
3. Satu H1 per halaman, lalu H2 dan H3 berurutan. Alamat halaman (URL) pendek, huruf kecil, dipisah tanda hubung.
4. Gambar pratinjau saat link dibagikan (ukuran 1200 x 630), judul dan deskripsi pratinjau, dan favicon.
5. Teks alternatif yang menjelaskan isi tiap gambar, nama file gambar yang bermakna, foto diperkecil dan memakai format ringan seperti WebP, serta pemuatan gambar tertunda untuk gambar di bawah layar.
6. Atribut bahasa halaman (lang) yang benar, tautan canonical tiap halaman, dan tautan antarhalaman dengan teks yang jelas (bukan "klik di sini").
7. Berkas sitemap.xml dan robots.txt, dan pastikan tidak ada tag noindex yang tertinggal.
8. Data terstruktur schema.org yang sesuai jenis web (Organization, atau Person untuk artist solo), hanya berisi data yang sudah ada di blueprint. Dilarang menambah rating, ulasan, atau alamat karangan.
9. Halaman 404 yang ramah, dan laporan kecepatan (misalnya Lighthouse) dengan skor sebelum dan sesudah perbaikan.
Minta daftar halaman beserta judul dan deskripsinya ditampilkan dalam tabel supaya pengguna bisa mengoreksi.

**Tahap 7, tayang.** Sebut hosting yang tertulis di bagian 8 blueprint. Kalau masih "belum ditentukan", pandu pengguna memilih dulu di chat dengan `references/pilihan-teknologi.md`, perbarui blueprint, baru beri prompt. Minta Claude Code hanya menayangkan folder `site/`. Untuk Cloudflare atau Netlify, minta Claude Code menghubungkan repo GitHub atau menjalankan perintah penayangan setelah pengguna login sendiri. Untuk shared hosting, minta folder siap unggah dari hasil build berikut `.htaccess` untuk HTTPS dan halaman 404 kalau servernya Apache, lalu memandu pengguna mengunggahnya lewat File Manager. Di Cloudflare, video portofolio wajib disematkan dari YouTube atau Vimeo. Di shared hosting atau VPS, video boleh di folder web kalau syarat paket mengizinkan dan sudah dikompres. Bagian login di situs hosting dikerjakan pengguna sendiri. Minta link web yang sudah tayang.

**Tahap 8, domain.** Minta langkah mengatur DNS yang tinggal diikuti, sesuai penjual domain pengguna. Ingatkan bahwa perubahan DNS bisa butuh waktu beberapa jam. Minta Claude Code memperbarui alamat di sitemap.xml, robots.txt, tautan canonical, dan gambar pratinjau ke domain final, serta mengalihkan alamat sementara hosting ke domain baru.

**Tahap 9, daftar ke Google dan cek indeks.** Dikerjakan setelah web tayang di alamat finalnya. Pembagian kerjanya:
1. Pengguna: buka Google Search Console dengan akun Google sendiri, pilih Add property, lalu pilih jenis Domain (verifikasi lewat DNS) atau URL prefix (verifikasi lewat tag atau berkas). Chat ini memandu klik demi klik.
2. Claude Code: pasang tag atau berkas verifikasi di web kalau pengguna memilih URL prefix, pastikan alamat sitemap.xml bisa dibuka, robots.txt tidak memblokir halaman penting, dan tidak ada noindex. Minta hasilnya dilaporkan.
3. Pengguna: di Search Console, buka menu Sitemaps, masukkan alamat sitemap, lalu klik Submit. Buka URL Inspection, tempel alamat beranda, dan klik Request indexing.
4. Pengguna, khusus brand yang punya studio atau area layanan lokal: buat atau klaim Google Business Profile dengan data yang sama persis dengan web (nama, alamat, nomor, jam buka), lalu pasang link web di profil itu.
5. Opsional: impor web ke Bing Webmaster Tools dari akun Search Console.
Minta Claude Code membuat daftar periksa pengecekan ulang di `README.md`, lalu bawa hasilnya ke chat: setelah 3 sampai 7 hari periksa menu Pages (halaman terindeks atau tidak, dan alasannya), setelah 2 sampai 4 minggu periksa menu Performance (klik, tayangan, kata yang membawa pengunjung). Ingatkan bahwa terindeks tidak berarti langsung muncul di halaman pertama.

**Tahap 10, panduan merawat.** Minta dilengkapi bagian Cara merawat di `README.md` berisi cara mengganti teks, foto, dan harga dengan meminta tolong Claude Code, beserta contoh prompt singkatnya. Tambahkan aturan setiap menambah halaman baru: judul, deskripsi, kata kunci, teks alternatif gambar, dan entri sitemap wajib diisi, lalu minta pengindeksan ulang di Search Console.

## Prompt perbaikan

```
Di Tahap [nomor] muncul masalah berikut:
[tempel pesan error atau jelaskan yang terlihat]

Tolong jelaskan dulu penyebabnya dengan bahasa sehari-hari, lalu perbaiki. Jangan mengubah bagian lain yang sudah berjalan. Setelah beres, tunjukkan cara aku mengecek bahwa masalahnya hilang. Catat perbaikannya di Catatan perubahan BLUEPRINT.md, perbarui README.md dan CLAUDE.md kalau ada yang berubah, lalu commit.
```
