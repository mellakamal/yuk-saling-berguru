# Pengetahuan: Web brand

Dibaca saat mengerjakan Langkah 5, jalur cepat web, atau kapan pun artist bertanya soal web, halaman satu lembar, domain, atau hosting. Harga alat dan aturan platform per November 2026, cek ulang sebelum disampaikan.

## Dua tahap web

Web dibangun dalam dua tahap, supaya artist cepat punya portofolio tanpa menunggu web lengkap:

| Tahap | Alat | Hasil | Kapan selesai |
|---|---|---|---|
| 1. Web pertama | Carrd | Satu halaman berisi karya, harga, ToS singkat, dan tombol order | Bisa dalam satu sore |
| 2. Web sendiri | Claude Code | Web beberapa halaman dengan domain sendiri | Setelah Langkah 7, atau saat artist siap |

Tahap 1 selalu dikerjakan dulu kalau brand belum punya web. Tahap 2 ditawarkan, tidak dipaksakan. Banyak artist komisi cukup dengan Carrd selamanya.

## Tahap 1. Carrd

### Paket

| Paket | Biaya kira-kira | Yang didapat | Cocok untuk |
|---|---|---|---|
| Free | Gratis | Alamat namabrand.carrd.co, ada badge Carrd, tanpa form, tanpa embed, tanpa domain sendiri | Mulai hari ini |
| Pro Standard | Sekitar $19 per tahun | Domain sendiri, form, embed, Google Analytics, pengaturan meta | Brand yang mau alamat sendiri dan mengukur kunjungan |

Ada juga Pro Lite dan Pro Plus. Sumber berbeda soal fitur Pro Lite, jadi cek halaman harga Carrd sebelum menyarankannya.

Paket gratis sudah cukup untuk mulai. Form order tetap bisa jalan: buat Google Form (Langkah 7), lalu pasang sebagai tombol link di Carrd. Tidak perlu form bawaan Carrd.

### Susunan satu halaman

Urutan dari atas ke bawah:
1. **Layar pertama:** nama brand, kalimat positioning satu baris, satu karya atau video terbaik, dan tombol utama ("Order now" atau "See prices").
2. **Karya:** 6 sampai 9 karya Tampil, utamakan video atau GIF pendek.
3. **Layanan dan harga:** tiap layanan dengan harga mulai dan isi paket.
4. **Cara order:** 3 langkah singkat, lalu tombol ke form, platform order, Discord, atau WhatsApp.
5. **ToS singkat:** 5 sampai 8 poin. Kalau panjang, link ke halaman ToS penuh (halaman Carrd kedua, atau Google Doc publik dari akun Google brand itu sendiri, karena dokumen publik menampilkan nama dan foto akun pemiliknya).
6. **FAQ:** 4 sampai 6 pertanyaan.
7. **Akun resmi:** daftar semua akun resmi, berguna kalau ada akun palsu (lihat bangkit-lagi.md).

### Cara memandu

Claude tidak bisa masuk ke akun Carrd artist. Jadi:
1. Tulis semua teks per bagian di dokumen teks siap tempel di folder Brand Hub.
2. Siapkan daftar file karya yang dipakai, urut sesuai susunan.
3. Tawarkan dua atau tiga template Carrd yang sederhana dan berbeda gaya, lalu artist memilih. Ganti huruf, warna, jarak, dan urutan bagian sesuai brand supaya halaman tidak terlihat seperti template yang sama dengan web lain.
4. Pandu satu bagian sekali jalan. Kalau letak menu tidak jelas, minta screenshot.
5. Sebelum terbit, minta artist membuka halaman di HP dan mengecek ceklis di bawah.

Pembuatan akun Carrd dan pembayaran Pro dilakukan artist sendiri. Claude tidak mengetik password dan tidak membayar.

## Tahap 2. Web sendiri dengan Claude Code

### Kapan ditawarkan

- Karya dan layanan sudah terlalu banyak untuk satu halaman.
- Brand butuh katalog produk, blog, atau dua bahasa.
- Brand ingin domain sendiri dan kendali penuh atas tampilan.
- Langkah 7 sudah selesai, jadi harga, ToS, dan form sudah pasti.

### Anggap artist bukan programmer

Artist tidak perlu bisa coding. Claude Code yang menulis kode, menjalankan perintah, dan memasang web. Artist cukup membaca, menyetujui, dan melihat hasilnya. Sampaikan ini sejak awal supaya artist tidak takut.

### Serahkan pembangunan ke skill bangun-website

Pembangunan web sendiri dipandu dua skill. **bangun-website-code** dipakai di dalam Claude Code dan membangun web langsung di folder proyek. **bangun-website** dipakai di chat tanpa akses folder, menyusun blueprint lalu memberi prompt bertahap untuk Claude Code. Tugasmu di Brand Hub menyiapkan bahannya, supaya skill itu tidak perlu menanyakan ulang hal yang sudah ada.

1. **Tulis dokumen Bahan Web** di folder Brand Hub. Isinya diambil dari Profil Brand, Bank Karya, Daftar Harga, ToS, dan Paket Jalur Order:
   - Tujuan web, pembeli utama, dan satu tindakan utama yang diharapkan
   - Bahasa publik
   - Halaman dan isi tiap halaman (lihat Langkah 5)
   - Positioning, bio, warna, huruf, dan contoh gaya dari Profil Brand
   - Daftar file karya dan urutannya
   - Harga, ToS, dan FAQ yang sudah disetujui
   - Link order, form, Discord, WhatsApp, dan akun resmi
   - Alamat Carrd yang sudah aktif, kalau ada
2. **Arahkan artist ke skill yang sesuai.** Kalau artist memakai Claude Code, minta ia membuka folder kosong untuk web itu dan mengetik: "bikin website untuk brand [nama], bahannya ada di dokumen Bahan Web", lalu menempelkan link dokumennya. Skill bangun-website-code menyusun blueprint dan membangunnya langsung. Kalau artist hanya memakai chat, minta ia mengetik kalimat yang sama di chat baru, dan skill bangun-website menyusun blueprint lalu memberi prompt bertahap untuk Claude Code.
3. **Setelah web tayang**, kembali ke Brand Hub: ganti semua link di bio dan Carrd ke web baru, lalu catat link web, hosting, penjual domain, dan letak folder proyek di Profil Brand. Carrd boleh tetap ada sebagai cadangan atau dialihkan. Jangan simpan password di Brand Hub.

Kalau kedua skill itu tidak terpasang, pandu sendiri dengan urutan yang sama: blueprint dari Bahan Web, persiapan akun GitHub dan hosting, lalu satu prompt Claude Code per tahap sampai tayang. Ikuti aturan tiga file di bawah.

### Tiga file pegangan proyek

Setiap proyek web di Claude Code wajib punya tiga file ini di folder utama, dibuat di tahap pertama:

| File | Untuk siapa | Isi |
|---|---|---|
| README.md | Artist dan siapa pun yang melanjutkan | Web ini apa, alamatnya, cara melihat pratinjau, cara menerbitkan ulang, cara mengganti teks, foto, dan harga, hosting dan domain yang dipakai (tanpa password) |
| CLAUDE.md | Claude Code di sesi berikutnya | Konteks brand (positioning, Bahasa publik, warna, huruf, suara), teknologi, susunan folder, aturan kerja, dan aturan memperbarui ketiga file ini |
| BLUEPRINT.md | Pegangan isi | Tujuan, halaman dan isi tiap halaman, fitur, keputusan beserta alasannya, dan bagian Catatan perubahan bertanggal |

Aturannya:
- **Setiap selesai mengubah kode, ketiga file diperbarui**, lalu progres disimpan (commit). Ingatkan artist di akhir setiap sesi dengan kalimat siap tempel: "Sebelum selesai, perbarui README.md, CLAUDE.md, dan Catatan perubahan di BLUEPRINT.md sesuai perubahan hari ini, lalu commit."
- Kalau brand sudah punya web di Claude Code tapi ketiga file belum ada, buat dulu dari kode yang ada sebelum mengerjakan perbaikan apa pun.
- Di awal setiap sesi baru, Claude Code membaca CLAUDE.md dan BLUEPRINT.md dulu.
- Tidak ada password, token, atau kunci API di ketiga file ini.

### Memilih hosting dan domain

Ringkasannya di sini. Detail, kriteria, dan aturan Tahap 7 ada di references/hosting.md pada skill bangun-website-code atau bangun-website. Syarat dan paket penyedia sering berubah, jadi cek ulang sebelum menyarankan, dan jangan menyebut harga dari ingatan.

Aturan memilih: web harus bisa dipindah, bisa dikerjakan Claude Code, dan syaratnya mengizinkan web yang menerima order.

| Urutan | Pilihan | Catatan |
|---|---|---|
| 0 | VPS atau hosting dengan SSH yang sudah dimiliki artist | Akses Claude paling leluasa lewat kunci SSH dan pengguna deploy tanpa hak root. Artist tetap mengurus pembaruan, firewall, dan cadangan |
| 1 | Cloudflare, paket gratis | Default untuk web statis yang dikerjakan Claude Code. Video portofolio disematkan dari YouTube atau Vimeo, karena paket gratis tidak mendukung berkas besar |
| 2 | Netlify, paket gratis | Cadangan. Situs berhenti sementara kalau kredit bulanan habis |
| 3 | Shared hosting berbayar | Untuk artist yang butuh email dengan nama domain, ingin bayar dalam rupiah, atau butuh dukungan lokal. Unggah manual lewat File Manager |
| Ditolak | Vercel Hobby, GitHub Pages, pembuat web tertutup, VPS baru khusus satu web | Vercel Hobby hanya nonkomersial, GitHub Pages tidak untuk usaha online, pembuat web tertutup sulit dibawa pindah, dan VPS baru butuh perawatan yang berlebihan untuk satu portofolio |

Hal yang perlu disampaikan ke artist:
- Kalau studio berencana punya beberapa web, pilih hosting yang bisa dikelola sekalian (satu VPS atau satu akun), lalu catat web mana ada di hosting mana. Kalau tiap web ingin berdiri sendiri, baca dulu bagian beberapa web di referensi hosting skill bangun-website.
- Carrd tetap jalur web pertama di Brand Hub. Aturan di atas berlaku untuk web sendiri.
- Domain didaftarkan atas nama artist sebagai pemilik brand. Domain .id lewat registrar terakreditasi PANDI.
- Tanyakan harga perpanjangan, bukan hanya harga promo tahun pertama.
- Simpan satu salinan folder web di komputer dan di repo GitHub sebagai arsip.
- Pendaftaran akun, login, dan pembayaran dikerjakan artist sendiri.

## Isi yang menjual

- **Layar pertama menentukan.** Pengunjung harus langsung tahu: ini jasa apa, untuk siapa, dan bagaimana memesan.
- **Satu tombol utama** per halaman. Tombol lain dibuat lebih kecil.
- **Harga terlihat.** Harga mulai lebih baik daripada "DM for price", karena pembeli tidak perlu bertanya dulu.
- **Bukti di dekat tombol:** ulasan, jumlah klien, atau logo klien kalau diizinkan.
- **Karya ditampilkan besar**, tidak dalam grid kecil yang padat.
- Teks mengikuti rumus di otak-marketing.md dan contoh di contoh.md.

## Teknis dasar

| Hal | Patokan |
|---|---|
| Tampilan HP | Dicek pertama. Sebagian besar pengunjung datang dari media sosial lewat HP |
| Ukuran gambar | Lebar sekitar 1600 sampai 2000 piksel, format WebP atau JPG terkompresi |
| Video | Klip pendek tanpa suara yang berputar, atau link ke YouTube kalau panjang |
| Judul halaman | Nama brand dan jasa utama dengan kata yang dicari pembeli niche itu. Polanya nama brand lalu jenis karya, misalnya studio fiktif ilustrasi buku anak menulis nama studionya diikuti "picture book illustration". Kalimatnya disusun dari kata kunci brand sendiri, tidak disalin dari contoh |
| Deskripsi halaman | Satu atau dua kalimat yang muncul di hasil Google |
| Gambar pratinjau link | Sekitar 1200 x 630 piksel, muncul saat link dibagikan |
| Teks alternatif gambar | Deskripsi singkat tiap karya |
| Pengukuran | Google Analytics, Plausible, atau statistik bawaan hosting. Di Carrd perlu Pro Standard |

## SEO dasar

Tujuannya web ditemukan calon klien yang mencari jasa seperti milikmu.

1. **Kata kunci.** Tanyakan artist: kalau klien mencari jasamu di Google, apa yang diketik? Pakai kalimat klien, bukan istilah internal. Satu halaman satu topik.
2. **Judul dan deskripsi tiap halaman.** Judul sekitar 50 sampai 60 karakter, kata kunci di depan, nama brand di belakang. Deskripsi sekitar 140 sampai 160 karakter, jujur sesuai isi halaman.
3. **Satu judul utama per halaman**, lalu subjudul berurutan. Alamat halaman pendek dan huruf kecil.
4. **Teks alternatif** yang menjelaskan isi tiap gambar karya, dan nama file gambar yang bermakna.
5. **Sitemap dan Google Search Console** untuk web sendiri. Artist mendaftar dengan akun Google-nya, mengirim sitemap, lalu meminta beranda diindeks. Claude Code menyiapkan sitemap dan tag verifikasinya.
6. **Google Business Profile** hanya kalau brand punya lokasi atau area layanan lokal. Datanya harus sama persis dengan web.
7. **Carrd.** Pengaturan meta termasuk fitur Pro Standard menurut tabel paket di atas, jadi di paket Free judul dan deskripsi tampil seadanya. Cek halaman harga Carrd.
8. **Jujur soal hasil.** Halaman baru butuh hari sampai minggu untuk terindeks dan beberapa bulan untuk naik. Peringkat tidak bisa dijanjikan. Pengecekan ulang: setelah 3 sampai 7 hari lihat menu Pages di Search Console, setelah 2 sampai 4 minggu lihat menu Performance.

## Ceklis sebelum terbit

1. Dibuka di HP: tidak ada teks terpotong, tombol mudah ditekan.
2. Semua tombol dan link dicoba satu per satu.
3. Form order dicoba sampai jawabannya masuk ke Brand Hub.
4. Harga dan ToS sama persis dengan tab Daftar Harga.
5. Tidak ada klaim yang belum dikonfirmasi artist.
6. Daftar akun resmi lengkap.
7. Link web dipasang di bio semua kanal, kecuali profil Fiverr dan Upwork.
8. Tiap halaman punya judul dan deskripsi sendiri, dan pratinjau link dicoba dengan membagikan link ke chat pribadi.

## Aturan platform

- Jangan pasang link web, form, atau kontak lain di profil dan pesan Fiverr atau Upwork.
- Web untuk pembeli dari luar platform. Pembeli yang datang dari platform dilayani di platform.

## Bahasa

Ikuti Bahasa publik di Profil Brand. Pasar global memakai bahasa Inggris. Pasar lokal memakai bahasa Indonesia. Pasar campuran memakai dua bahasa: di Carrd cukup dengan bagian singkat berbahasa Indonesia untuk klien lokal dan tombol WhatsApp, di web sendiri bisa dengan tombol ganti bahasa.
