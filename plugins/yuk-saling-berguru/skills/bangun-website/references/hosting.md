# Memilih Hosting dan Domain

Dibaca bersama `pilihan-teknologi.md` saat memilih teknologi dan tempat tayang (sebelum blueprint disetujui), dan di Tahap 7 dan 8. `pilihan-teknologi.md` berisi pertanyaan untuk artist, tingkat web, dan tabel rekomendasi. File ini berisi syarat dan cara kerja tiap penyedia. Untuk web artist atau studio yang menjual karya, komisi, produk, atau jasa. Isinya dicek ke situs resmi dan sumber lain pada 17 November 2026. Syarat, batas, dan harga penyedia sering berubah, jadi sebelum menyarankan satu penyedia, cek ulang syarat resminya (pakai pencarian web kalau tersedia). Jangan menyebut harga dari ingatan. Minta artist melihat harga di situs penjualnya.

## Empat aturan memilih
1. **Bisa dipindah.** Berkas web harus bisa dibawa ke penyedia lain tanpa mengubah alamat web. Itu berlaku kalau webnya statis dan domainnya milik artist.
2. **Bisa dikerjakan Claude Code.** Penayangan lewat Git atau perintah dari penyedia lebih mudah daripada unggah manual. Login dan pembayaran tetap dikerjakan artist, dan Claude tidak menangani password atau token.
3. **Syaratnya mengizinkan web yang menerima order.** Tolak layanan yang melarang pemakaian komersial.
4. **Leluasa untuk fitur dan akses Claude Code.** Penyedia punya perintah baris atau penayangan lewat Git, plus fungsi sisi server untuk form dan data kecil. Dengan begitu Claude bisa menayangkan dan menambah fitur sendiri setelah artist login. Unggah manual lewat panel membatasi itu.

## Pilihan tempat tayang
Untuk peserta Yuk Saling Berguru, tawarkan tiga pilihan ini dalam satu tabel. Artist yang memutuskan, dan boleh memutuskan nanti di tahap Tayang.

| Pilihan | Cocok untuk | Untungnya | Yang perlu diterima |
|---|---|---|---|
| **Cloudflare Pages** | Web HTML biasa seperti hasil kelas | Gratis, HTTPS otomatis, alamat `nama.pages.dev` langsung jadi, domain sendiri bisa menyusul. Claude Code bisa mengurus dari awal sampai tayang | Butuh akun GitHub dan akun Cloudflare. Belum termasuk email dengan nama domain |
| **Rumahweb** | Artist yang butuh email dengan nama domain sendiri, atau lebih nyaman dengan penyedia lokal | Bayar dalam rupiah, dukungan berbahasa Indonesia, domain dan email dalam satu tempat | Berbayar. Cek apakah paketnya menyediakan akses SSH supaya Claude Code bisa ikut mengurus |
| **VPS Hostinger** | Artist atau studio yang ingin satu server untuk beberapa web, atau berencana punya fitur yang butuh server sendiri | Akses penuh lewat SSH, jadi Claude Code bisa mengurus server dan web dari awal sampai tayang. Satu server bisa menampung beberapa web | Berbayar. Pemilik bertanggung jawab atas keamanan, pembaruan, dan cadangan server. Saat dipilih, jalankan bagian Khusus VPS di `keamanan.md` sebelum web tayang |

Penyedia lain di tabel Urutan pilihan di bawah hanya dibahas kalau artist menanyakannya atau sudah punya hosting sendiri. Kalau artist memilih VPS, ikuti bagian Khusus VPS di `keamanan.md`.

## Urutan pilihan

Tabel ini daftar penyedia yang layak, diurutkan dari akses Claude Code yang paling leluasa. Ini bukan urutan bawaan. Rekomendasi untuk satu artist mengikuti jawabannya, dengan tabel Rekomendasi di `pilihan-teknologi.md`.

| Urutan | Pilihan | Cocok untuk | Catatan |
|---|---|---|---|
| 0 | **VPS atau hosting dengan akses SSH yang sudah dimiliki artist** (misalnya Hostinger KVM, atau paket Rumahweb yang menyediakan SSH) | Artist yang sudah membayar dan terbiasa mengurusnya, atau punya beberapa web di satu server | Akses Claude paling leluasa. Lihat bagian VPS dan SSH di bawah |
| 1 | **Cloudflare** (Pages atau Workers Static Assets), paket gratis | Web portofolio statis yang ingin dikerjakan Claude Code dari awal sampai tayang | Lihat bagian Cloudflare di bawah. Syarat paket gratis bisa berubah |
| 2 | **Netlify**, paket gratis | Cadangan kalau Cloudflare tidak cocok | Memakai sistem kredit bulanan. Situs berhenti sementara kalau kredit habis |
| 3 | **Shared hosting berbayar** (penyedia lokal atau global) | Artist yang butuh email dengan nama domain sendiri, ingin bayar dalam rupiah, atau butuh dukungan berbahasa Indonesia, dan menerima akses Claude yang terbatas | Unggah manual lewat File Manager, karena FTP butuh password yang tidak boleh ditangani Claude. Fitur sisi server bergantung paket. Kalau paketnya menyediakan SSH, Claude bisa menayangkan lewat kunci SSH yang dibuat artist |
| Opsional | **Vercel Pro** (berbayar) | Artist yang ingin alur Git yang paling mulus dan tidak keberatan biaya dalam dolar per anggota | Hanya Pro. Cek harga terbaru di halaman harga Vercel |

Yang ditolak untuk web yang menerima order:
- **Vercel Hobby.** Hanya untuk pemakaian pribadi nonkomersial menurut kebijakan Vercel. Web yang mempromosikan jasa dihitung komersial.
- **GitHub Pages.** GitHub menyatakan Pages tidak dimaksudkan sebagai hosting gratis untuk usaha online. Boleh untuk portofolio pribadi tanpa order.
- **Pembuat web tertutup** (Wix, Framer, Squarespace, dan sejenisnya) sebagai tempat web sendiri. Berkas tidak bisa dibawa pindah.
- **WordPress**, termasuk pemasangan sekali klik di shared hosting. Tidak ditawarkan di skill ini, tetapi dibantu kalau artist tetap memilihnya. Alasan dan caranya ada di `pilihan-teknologi.md`.
- **VPS yang dibeli baru khusus untuk satu web portofolio** tidak disarankan kalau artist hanya butuh satu web sederhana, karena pemilik harus mengurus pembaruan, keamanan, dan cadangan server. Kalau artist memilih VPS Hostinger dari tiga pilihan di atas setelah paham konsekuensinya, hormati pilihannya dan jalankan bagian Khusus VPS di `keamanan.md`.

Carrd sebagai web pertama tetap mengikuti jalur Brand Hub dan tidak dibahas di sini.

## Cloudflare
Dicek pada 17 November 2026:
- Permintaan ke berkas statis gratis dan tidak dibatasi.
- Batas paket gratis Pages: 500 build per bulan, satu build sekaligus, 20.000 berkas per situs, 25 MiB per berkas, 100 domain per proyek.
- Cloudflare sedang menggabungkan Pages ke Workers Static Assets dan mengarahkan proyek baru ke sana. Cek dokumentasi Cloudflare untuk jalur yang direkomendasikan saat itu, dan pilih yang itu.
- **Video dan berkas besar.** Syarat layanan Cloudflare tidak mendukung penayangan video atau berkas non-HTML yang besar lewat paket gratis. Untuk portofolio, taruh video di YouTube atau Vimeo lalu sematkan, dan kompres gambar. Jangan menaruh video portofolio langsung di folder web.
- **Pemakaian komersial.** Halaman batas Pages tidak menyebut larangan komersial, dan sumber pihak ketiga menyatakan diizinkan di paket gratis. Meski begitu, baca Terms of Use Cloudflare dulu sebelum menyarankan, dan sampaikan ke artist bahwa itu syarat yang bisa berubah.
- **Email.** Cloudflare tidak menyediakan kotak email. Yang ada penerusan email dari domain sendiri ke Gmail atau kotak email lain. Artist yang butuh kotak email sungguhan perlu layanan email terpisah atau shared hosting.
- Login ke akun Cloudflare dikerjakan artist lewat browser. Jangan menyimpan token di repo, README, atau CLAUDE.md.

## Akses Claude Code dan fitur tambahan
Supaya Claude bisa bekerja leluasa tanpa menyentuh rahasia:
- **Login.** Artist menjalankan sendiri perintah login penyedia di terminalnya (misalnya `wrangler login` untuk Cloudflare), yang membuka browser. Alternatifnya membuat API token dengan izin sekecil mungkin, hanya untuk proyek ini, lalu menyimpannya di variabel lingkungan komputernya. Claude tidak mengetik, membaca, atau menyimpan token, dan token tidak boleh masuk repo, README, atau CLAUDE.md.
- **Setelah login,** Claude boleh menjalankan perintah penayangan, membuat proyek, memasang domain, dan mengecek alamat sementara. Sebelum perintah yang mengubah akun (hapus proyek, ganti DNS, ubah paket), Claude menunjukkan perintahnya dan menunggu persetujuan artist.
- **Fitur yang bisa ditambah tanpa pindah penyedia** (cek dokumentasi Cloudflare untuk nama dan batas terbaru): fungsi sisi server untuk menerima form, penyimpanan data kecil, perlindungan spam di form (Turnstile), dan penerusan email dari domain sendiri. Netlify punya padanan untuk form dan fungsi.
- **Batas.** Login anggota dan database besar tetap tingkat lanjut (lihat pilihan-teknologi.md). Setiap fitur yang menyimpan data dicatat di `BLUEPRINT.md`, dan kodenya diarsipkan di GitHub.

## VPS dan SSH
Daftar alat keamanan VPS dan urutan pemasangannya ada di bagian Khusus VPS di `keamanan.md`.
Berlaku untuk server yang sudah dimiliki artist. Contoh: Hostinger KVM 2 (root penuh, SSH, Docker, cadangan mingguan menurut halaman Hostinger per 17 November 2026). Paket shared Rumahweb tertentu menyebut SSH, tapi tidak semua paket, jadi cek paket yang dipakai.
- **Akses.** Artist membuat pasangan kunci SSH sendiri, memasang kunci publik di server, dan Claude memakai kunci itu dari komputer artist. Jangan memakai password root dan jangan menempelkannya di chat, prompt, atau file.
- **Pengguna khusus.** Buat pengguna deploy tanpa hak root yang hanya memegang folder web ini. Claude bekerja lewat pengguna itu. Perintah dengan hak root (pasang paket, ubah firewall, ubah layanan) ditunjukkan dulu dan dijalankan setelah artist setuju.
- **Penayangan.** Web statis disalin ke folder web yang dilayani Nginx, Caddy, atau Apache. Satu server bisa melayani beberapa domain. Pasang SSL gratis (Let's Encrypt) dan pembaruan otomatisnya.
- **Perawatan yang tetap jadi tugas artist.** Pembaruan sistem, firewall (buka hanya port 22, 80, 443), cadangan di luar server selain cadangan bawaan, dan memantau masa aktif langganan. Claude boleh menyiapkan skripnya, tapi artist yang menyetujui dan mengecek.
- **Tetap bisa dipindah.** Isi web tetap disimpan di GitHub dan folder web statis bisa disalin ke penyedia mana pun.
- **Catatan.** Satu server untuk banyak web berarti kalau server bermasalah, semua web ikut turun. Karya dan data penting jangan hanya ada di server.

## Kalau punya atau berencana punya beberapa web
Studio sering menambah web baru (web per brand, per proyek, atau per kampanye). Tanyakan rencananya saat menyusun blueprint, lalu pilih hosting yang bisa dikelola sekalian:
- **Satu VPS atau hosting dengan SSH.** Pilihan paling praktis. Satu server melayani banyak domain, satu pengguna deploy per web, dan semua web dirawat di satu tempat. Cocok kalau artist sudah punya server. Risikonya, server bermasalah berarti semua web turun, jadi cadangan di luar server wajib.
- **Satu akun Cloudflare.** Satu proyek per web, semua dalam satu akun dan satu login. Tidak ada server yang diurus, tapi mengikuti syarat dan batas paket gratisnya, jadi cek batas jumlah proyek dan build di dokumentasi.
- **Shared hosting dengan banyak domain.** Cek apakah paketnya mengizinkan lebih dari satu situs. Paket terkecil sering hanya satu situs.
- **Nama proyek di hosting.** Di Cloudflare dan penyedia sejenis, nama proyek menjadi bagian dari alamat sementara (misalnya `namaproyek.pages.dev`) yang bisa dilihat publik. Pilih nama dari brand itu sendiri, jangan memakai pola yang sama untuk semua web (misalnya selalu diawali `web-`). Setelah domain sendiri aktif, alihkan alamat sementara ke domain itu supaya tidak ada dua alamat yang tayang.
- **Kalau tiap web ingin berdiri sendiri.** Beberapa web di satu server memakai alamat IP yang sama, dan siapa pun bisa mengecek domain apa saja yang ada di satu IP. Kalau brand-brand itu memang ingin tampil terpisah, sampaikan pilihan ini ke artist: tiap web di akun hosting sendiri, atau penyedia yang menayangkan web lewat jaringan bersama (misalnya Cloudflare) sehingga IP-nya tidak menunjuk ke satu server milik studio. Keputusannya di artist.
- **Jejak teknis lain yang perlu dipisah kalau web ingin berdiri sendiri:** satu sertifikat SSL per domain (jangan menggabungkan beberapa domain dalam satu sertifikat, karena daftar domain di sertifikat tercatat publik), kode analitik terpisah per web, perlindungan privasi data pemilik domain dinyalakan di registrar, dan email kontak di web memakai email brand itu sendiri.
- Satu repo GitHub per web dengan penamaan seragam, dan satu daftar di `README.md` studio yang mencatat web mana ada di hosting mana (tanpa password dan token).
- Domain tiap web tetap atas nama pemilik brand dan bisa diarahkan ke hosting yang sama.

## Netlify
Paket gratis memakai sistem kredit bulanan, dan bandwidth dihitung sebagai kredit. Sumber pihak ketiga menyebut pemakaian komersial diizinkan di paket gratis, tapi cek syarat resminya sebelum menyarankan. Situs berhenti sementara kalau kredit habis, jadi web yang ramai atau penuh gambar besar bisa terkena.

## Shared hosting berbayar
Berkas web statis cukup disalin ke folder web di server, jadi bisa dipindah ke penyedia mana pun dengan menyalin folder yang sama. Kriteria memilih:
- Panel standar (cPanel atau setara) dengan File Manager, supaya artist memegang berkasnya.
- SSL gratis termasuk, dan email dengan nama domain sendiri (misalnya hello@namabrand.com).
- Cadangan otomatis dengan cara memulihkan yang jelas, dan dukungan pelanggan berbahasa Indonesia kalau perlu.
- Lokasi server dekat pasar utama, dan tidak ada aturan yang melarang web komersial.
- Harga perpanjangan jelas, karena harga promo tahun pertama bisa berbeda.
- Bisa upgrade paket tanpa memindahkan web.
- Untuk web statis di server Apache atau LiteSpeed, siapkan `.htaccess` untuk memaksa HTTPS, menampilkan halaman 404, dan membuka alamat tanpa `.html` (misalnya `/prices` untuk `prices.html`).
- Shared hosting umumnya menjalankan PHP, jadi tingkat 3 (dinamis ringan) bisa memakai skrip PHP kecil, misalnya penerima form yang mengirim email. Kunci rahasia disimpan di luar folder web atau di pengaturan panel, tidak di repo.

Contoh penyedia yang umum dibandingkan di Indonesia: Rumahweb, Niagahoster, Hostinger. Ini contoh untuk dibandingkan, bukan rekomendasi pasti.

## Domain
- Domain .id hanya bisa didaftarkan lewat registrar yang terakreditasi PANDI. Pilih registrar dari daftar resmi di pandi.id.
- Beberapa ekstensi (.id, .my.id, .biz.id) tidak butuh dokumen khusus menurut salah satu registrar. Ekstensi seperti web.id, .sch.id, .or.id, dan .ac.id butuh dokumen. Verifikasi dokumen oleh registrar biasanya 1 sampai 3 hari kerja. Cek syarat terbaru di registrar yang dipilih.
- Untuk brand yang melayani pasar global, .com biasanya lebih dikenal pembeli luar negeri. Pilihan akhirnya di artist.
- Domain didaftarkan atas nama pemilik brand, bukan atas nama pembuat web atau penyedia hosting. Domain milik artist adalah yang membuat web bisa pindah hosting tanpa ganti alamat.
- Tanyakan harga perpanjangan.

## Aturan di Tahap 7
1. Pakai hosting yang tertulis di bagian 8 blueprint. Kalau masih "belum ditentukan", jalankan dulu langkah memilih di `pilihan-teknologi.md`: pertanyaan untuk artist, paling banyak dua pilihan dengan untung rugi, satu rekomendasi, dan penjelasan dua arti "bebas". Tidak ada penyedia bawaan. Artist yang memutuskan.
2. Kalau artist sudah punya VPS atau hosting dengan SSH dan mau mengurusnya, rekomendasikan itu. Kalau artist butuh kotak email domain atau dukungan lokal, rekomendasikan shared hosting yang menyediakan SSH dan sampaikan bahwa tanpa SSH akses Claude lebih terbatas. Kalau artist butuh panel admin dari CMS berbasis Git, rekomendasikan Cloudflare atau Netlify. Kalau berencana punya beberapa web, utamakan hosting yang bisa dikelola sekalian (bagian Kalau punya atau berencana punya beberapa web).
3. Cek ulang syarat resmi penyedia yang dipilih. Tulis pilihan, alasan, dan tanggal pengecekan di Catatan keputusan `BLUEPRINT.md`, dan nama hosting serta domain (tanpa password dan token) di `README.md`.
4. Artist membuat akun, login, dan membayar sendiri. Claude tidak mengetik atau menyimpan password dan token.
5. VPS atau hosting dengan SSH: ikuti bagian VPS dan SSH. Artist menyiapkan kunci SSH dan pengguna deploy, Claude menyalin hasil build dan mengecek HTTPS.
6. Hosting berbasis Git (Cloudflare, Netlify): artist login sendiri dengan cara di bagian Akses Claude Code, lalu Claude menghubungkan repo GitHub ke penyedia atau menjalankan perintah penayangannya, dan mengecek alamat sementara dari penyedia.
7. Shared hosting tanpa SSH: siapkan folder siap unggah dari hasil build, berikut `.htaccess` untuk HTTPS dan halaman 404 kalau servernya Apache, lalu pandu artist mengunggah isinya lewat File Manager.
8. Simpan satu salinan folder web di komputer dan di repo GitHub sebagai arsip. Itu yang membuat web mudah dipindah.
9. Setelah tayang, cek: web terbuka lewat HTTPS dari HP lain, tidak ada peringatan keamanan, halaman 404 tampil, video tampil (tersemat dari YouTube atau Vimeo, atau dari folder web di shared hosting dan VPS), dan email domain bisa dipakai kalau paketnya menyediakan.
10. Yang ditayangkan hanya folder `site/`. `bahan/`, `desain-kasar.html`, dan file pegangan tidak ikut tayang.
