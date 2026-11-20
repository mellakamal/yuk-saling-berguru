# Memilih Teknologi dan Tempat Tayang

Dibaca bersama `hosting.md` sebelum blueprint disetujui: di Tahap 3 skill chat, atau di Pemetaan skill Code. Dibaca lagi di Tahap 7 kalau pilihan di blueprint masih "belum ditentukan".

Tujuannya artist memilih sendiri jenis web dan hosting sesuai kebutuhannya, dengan rekomendasi dari Claude. Jangan menulis jenis web atau hosting di blueprint tanpa menanyakannya. Jangan menganggap satu penyedia sebagai pilihan bawaan sebelum artist menjawab.

## Langkah memilih
1. Ajukan pertanyaan di bawah dalam satu daftar bernomor, dengan keterangan singkat di tiap nomor. Lewati yang sudah terjawab di bahan, Brand Hub, atau obrolan sebelumnya.
2. Dari jawabannya, tentukan tingkat web (bagian Empat tingkat web) dan sebutkan ke artist dalam satu kalimat dengan analogi rumah, misalnya "Kebutuhanmu cukup tingkat 2: rumah jadi dengan loket titipan untuk form order." Kalau ternyata artist butuh tingkat yang lebih tinggi dari dugaannya, atau lebih rendah, jelaskan bedanya. Lalu tentukan hosting (bagian Rekomendasi). Beri paling banyak dua pilihan, masing-masing dengan untung dan ruginya, lalu sarankan satu.
3. Jelaskan dua arti "bebas" (bagian Dua arti bebas), karena artist sering memilih hosting berdasarkan kata itu.
4. Artist yang memutuskan. Tulis tingkat web, hosting, dan alasannya di bagian 8 dan Catatan keputusan blueprint.
5. Kalau artist belum yakin, tulis "belum ditentukan, condong ke [rekomendasi]". Pembangunan di laptop tetap jalan karena web statis bisa ditaruh di hosting mana saja. Keputusan final paling lambat di awal Tahap 7. Selama belum diputuskan, Claude Code tidak membuat file pengaturan hosting.

## Pertanyaan
Buka daftar pertanyaan dengan satu kalimat seperti ini, supaya artist tahu kenapa ditanya: "Dua pertanyaan pertama menentukan apakah web kamu cukup statis (isinya diganti lewat Claude) atau perlu bagian yang dinamis (panel admin, form yang menyimpan data, status slot komisi). Sisanya untuk memilih hosting."

1. **Yang mengganti isi web nanti.** Lewat Claude Code (cukup minta, Claude yang mengubah), atau kamu sendiri lewat panel admin tanpa membuka Claude? *Untuk apa ditanya:* kalau mau panel admin sendiri, web butuh CMS, dan itu memengaruhi pilihan hosting.
2. **Fitur selain portofolio.** Pilih yang dibutuhkan: form order, form dengan unggah file referensi, status slot komisi (open atau closed, antrean), katalog produk, login klien, pembayaran langsung di web. *Untuk apa ditanya:* fitur ini yang menentukan web tetap statis, perlu layanan tambahan, atau perlu bagian dinamis.
3. **Hosting yang sudah dimiliki.** Sudah punya hosting atau VPS? Kalau sudah, apakah ada akses SSH (jalur masuk ke server lewat terminal)? Boleh jawab belum tahu.
4. **Email nama domain.** Butuh kotak email sendiri seperti hello@namabrand.com, atau cukup email yang diteruskan ke Gmail?
5. **Cara bayar dan bantuan.** Lebih nyaman bayar dalam rupiah dan dibantu CS berbahasa Indonesia?
6. **Video portofolio.** Ada video karya? Boleh ditaruh di YouTube atau Vimeo lalu disematkan?
7. **Rencana ke depan.** Berencana punya beberapa web, misalnya web studio dan web per brand? Siapa yang merawat?
8. **Anggaran per bulan** untuk hosting, boleh nol.

## Arti "web dinamis"
Kalau artist menyebut web dinamis, tanyakan maksudnya dengan pertanyaan nomor 1 dan 2. Kalau artist tidak menyebutnya, tabel ini tetap dipakai untuk membaca jawaban nomor 1 dan 2. Biasanya yang dimaksud salah satu dari ini, dan sebagian besar tidak butuh server sendiri:

| Yang dimaksud artist | Jalan keluarnya | Tingkat |
|---|---|---|
| Mengganti karya, teks, dan harga sendiri | Lewat Claude Code, atau panel admin dari CMS berbasis Git | 1 atau 2 |
| Status slot komisi | Satu baris teks yang diganti lewat Claude Code, atau dibaca dari Google Sheet | 1 atau 2 |
| Form order, termasuk unggah file | Layanan form (Tally, Google Forms, Formspree). Cek apakah layanan itu mendukung unggah file dan berapa batasnya | 2 |
| Form yang datanya disimpan sendiri | Fungsi sisi server dari penyedia hosting, atau skrip PHP kecil di shared hosting | 3 |
| Login klien, dashboard, database besar | Di luar fokus skill ini | 4 |
| Pembayaran langsung di web | Tautkan ke platform jadi (Ko-fi, Gumroad, Lynk.id, Etsy, VGen) | 2 |

## Empat tingkat web
1. **Statis.** Rumah jadi, isinya tidak berubah sendiri. HTML dan CSS biasa, atau Astro kalau halamannya banyak. Order lewat Discord, WhatsApp, DM, atau platform. Ini titik awal semua web di kelas, termasuk web pertama yang dibangun dari BLUEPRINT.md.
2. **Statis dengan layanan.** Tetap rumah jadi, tapi ada loket titipan milik pihak lain: layanan form, data dari Google Sheet, link ke toko, atau panel admin dari CMS berbasis Git (misalnya Decap CMS atau Pages CMS, cek dokumentasi terbarunya). CMS berbasis Git butuh hosting yang menayangkan langsung dari GitHub (Cloudflare atau Netlify). Di shared hosting tanpa penayangan lewat Git, perubahan dari panel admin tidak otomatis tayang.
3. **Dinamis ringan.** Rumah dengan satu ruang kerja kecil. Fungsi sisi server untuk menerima form, menyimpan data kecil, atau perlindungan spam: fungsi Cloudflare atau Netlify, atau skrip PHP kecil di shared hosting atau VPS. Kunci rahasia disimpan di pengaturan hosting atau `.env` yang masuk `.gitignore`. Setiap fitur yang menyimpan data dicatat di blueprint.
4. **Aplikasi dengan login, database, atau pembayaran sendiri.** Rumah dengan gudang dan kunci pintu. Di luar fokus skill ini. Sampaikan jujur bahwa butuh lebih banyak tahap, ada risiko keamanan data, dan sebaiknya ada orang yang bisa dimintai tolong. Tawarkan versi tingkat 1 sampai 3 dulu, dengan pembayaran dan antrean lewat platform jadi.

Kalau ragu di antara dua tingkat, pilih yang lebih rendah. Naik tingkat nanti tidak perlu membangun ulang.

**WordPress tidak ditawarkan di skill ini**, termasuk pemasangan sekali klik di shared hosting. Kalau artist menanyakannya, jelaskan singkat alasannya sekali: plugin dan tema harus rutin diperbarui, sering jadi sasaran retas, Claude Code lebih sulit merawatnya, dan isinya tidak mudah dibawa pindah. Kalau yang dicari panel admin, tawarkan tingkat 2 dengan CMS berbasis Git. Kalau artist tetap memilih WordPress atau pembuat web lain, hormati pilihannya dan bantu: pandu pemasangan, tema, dan plugin yang aman, ingatkan pembaruan rutin dan cadangan, lalu catat keputusannya di BLUEPRINT.md. Alur desain kasar dan BLUEPRINT.md tetap dipakai sebagai denah. Pembuat web tertutup (Wix, Framer, Squarespace) juga tidak ditawarkan karena file webnya tidak bisa dibawa pindah, dengan aturan yang sama kalau artist tetap memilihnya.

## Dua arti bebas
- **Bebas untuk artist:** punya kotak email domain, bayar rupiah, dibantu CS berbahasa Indonesia, bisa menaruh video atau skrip PHP di hosting.
- **Bebas untuk Claude Code:** Claude bisa menayangkan, memasang domain, dan menambah fitur sendiri setelah artist login, tanpa artist harus klik di panel.

Urutan keleluasaan Claude Code untuk web seperti ini: VPS (paling leluasa, tapi artist merawat server), Cloudflare atau Netlify (sangat leluasa, tanpa server), shared hosting dengan SSH (hampir sama, tapi domain dan fitur lebih banyak lewat panel), lalu shared hosting tanpa SSH (Claude menyiapkan folder, artist mengunggah lewat File Manager). Kenyamanan Claude bukan alasan utama memilih. Yang menentukan kebutuhan artist.

## Rekomendasi
Pakai urutan ini. Berhenti di baris pertama yang cocok, lalu beri satu pilihan kedua yang masuk akal.

| Kalau | Sarankan | Catatan |
|---|---|---|
| Sudah punya VPS atau hosting dengan SSH dan mau mengurusnya | Pakai yang sudah ada | Ikuti bagian VPS dan SSH di `hosting.md` |
| Butuh panel admin sendiri (tingkat 2 dengan CMS) | Cloudflare atau Netlify | Kalau juga butuh kotak email domain, email diurus di layanan email terpisah |
| Butuh kotak email domain, bayar rupiah, atau CS lokal | Shared hosting yang menyediakan SSH (contoh untuk dibandingkan: Rumahweb, Niagahoster, Hostinger) | Tanyakan ke CS apakah paketnya punya SSH. Tanpa SSH, artist mengunggah sendiri lewat File Manager |
| Berencana punya beberapa web dan mau merawat server | VPS | Kalau tidak mau merawat server, satu akun Cloudflare dengan satu proyek per web. Kalau tiap web ingin berdiri sendiri, baca bagian beberapa web di `hosting.md` dulu |
| Selain itu | Cloudflare, dengan Netlify sebagai cadangan | Gratis, tanpa server. Video disematkan dari YouTube atau Vimeo |

Sebelum menyarankan penyedia, cek ulang syarat resminya sesuai aturan di `hosting.md`. Jangan menyebut harga dari ingatan.

## Pengaruh pilihan ke tahap kerja
| Hosting | Yang berubah |
|---|---|
| Cloudflare | File pengaturan penayangan (misalnya `wrangler.jsonc`) dibuat di Tahap 7. Video wajib disematkan dari YouTube atau Vimeo. Email hanya penerusan ke Gmail |
| Netlify | Penayangan dari GitHub atau perintah Netlify. Gambar dan video besar memakan kuota kredit |
| Shared hosting | `.htaccess` untuk HTTPS, halaman 404, dan alamat tanpa `.html`. Video boleh di folder web kalau syarat paket mengizinkan dan sudah dikompres. Skrip PHP kecil bisa dipakai untuk tingkat 3 |
| VPS | Konfigurasi server web (Nginx, Caddy, atau Apache), SSL, dan pengguna deploy. Semua tingkat 1 sampai 3 bisa |

Halaman pertama di Tahap 1 selalu HTML dan CSS biasa tanpa pengaturan hosting, apa pun pilihannya.

## Istilah yang dijelaskan ke artist
| Istilah | Analogi |
|---|---|
| Domain | Alamat rumah |
| Hosting | Tanah tempat rumah berdiri |
| DNS | Papan petunjuk yang mengarahkan alamat ke rumah yang benar |
| Repository (repo) di GitHub | Lemari arsip semua file web, lengkap dengan riwayat perubahan |
| Commit | Menyimpan progres dengan catatan, seperti menandai halaman buku |
| Deploy | Membuka pintu rumah untuk tamu |
| Pratinjau (preview) | Melihat rumah sebelum dibuka untuk umum |
| SSH | Pintu belakang khusus tukang untuk masuk ke server |
| CMS | Panel untuk mengganti isi rumah tanpa memanggil tukang |
| Database | Gudang tempat menyimpan data |
| Kunci API | Kunci gudang, tidak boleh diberikan ke siapa pun |

## Biaya yang perlu disampaikan
- Hosting: Cloudflare dan Netlify punya paket gratis dengan batas yang bisa berubah. Shared hosting dan VPS berbayar, cek harga perpanjangannya juga.
- Domain: berbayar per tahun, harganya bergantung ekstensi (.com, .id, dan lainnya).
- Claude Code: mengikuti paket langganan Claude artist.

Jangan menyebut angka harga dari ingatan. Kalau artist bertanya, cari harga terbaru atau minta ia mengecek di situs penjualnya.
