# Cek keterpisahan brand

Setiap brand berdiri sendiri. Web yang diam-diam terhubung dengan web, akun, atau pemilik lain membuat brand mudah tertukar, kurang dipercaya pembeli, dan lebih gampang ditiru. Lapisan ini mengecek apakah ada jejak yang mengaitkan web ini dengan brand lain atau dengan data pribadi pemiliknya.

Jalankan otomatis untuk setiap web milik brand, artist, atau studio. Hasilnya dilaporkan apa adanya. Keputusan mana yang perlu dipisah tetap di pemilik brand, karena sebagian brand memang sengaja terbuka menyebut induk studionya.

## Yang dicek

| No | Bagian | Yang dicari | Cara mengecek |
|---|---|---|---|
| 1 | Footer, ToS, FAQ, halaman Tentang | Nama orang, alamat, nomor WhatsApp, atau email yang juga dipakai brand lain. Nama studio induk yang tidak dimaksudkan tampil | Baca semua halaman. Cari email dan nomor di kode |
| 2 | Kode HTML | Komentar di kode, `meta name="author"`, `meta name="generator"`, nama folder atau path yang menyebut brand lain | Buka sumber halaman atau file di folder proyek |
| 3 | File di web | Data tersembunyi di gambar (EXIF: lokasi, kamera, nama pembuat, software) dan properti PDF (author, creator) | Di folder proyek: `exiftool` kalau ada, atau baca properti file. Dari link live: unduh beberapa gambar dan PDF lalu periksa |
| 4 | Kode analitik dan verifikasi | ID Google Analytics, Google Tag Manager, Meta Pixel, dan `google-site-verification` yang sama dengan web lain. Satu ID yang sama cukup untuk mengaitkan dua web | Cari `G-`, `GTM-`, `fbq(`, `google-site-verification` di kode. Bandingkan dengan web lain milik pemilik yang sama kalau pengguna menyebutnya |
| 5 | Domain | Privasi data pemilik domain (WHOIS) aktif. Riwayat WHOIS lama tersimpan di layanan histori walau sekarang sudah diprivasi | Cek WHOIS sekarang. Riwayat lama dicek pemilik di layanan histori WHOIS, lalu dilaporkan sebagai "perlu dicek pemilik" |
| 6 | Server dan IP | Web langsung mengarah ke IP server tanpa proxy, atau satu IP dipakai beberapa web brand berbeda | Di Claude Code: `dig +short NAMADOMAIN` lalu lihat apakah IP-nya milik Cloudflare atau penyedia hosting bersama. Cek reverse IP dilakukan pemilik di layanan reverse IP |
| 7 | Nameserver | Beberapa domain brand berbeda memakai pasangan nameserver Cloudflare yang sama, tanda dikelola dari satu akun | `dig +short NS NAMADOMAIN`, bandingkan dengan domain lain yang disebut pengguna |
| 8 | Sertifikat SSL | Nama subdomain yang menyebut studio atau induknya. Satu sertifikat berisi beberapa domain brand berbeda | `curl -s "https://crt.sh/?q=NAMADOMAIN&output=json"` lalu baca kolom `name_value` |
| 9 | Alamat sementara hosting | Alamat seperti `namaproyek.pages.dev` atau `namaproyek.netlify.app` masih tayang, atau nama proyeknya mengikuti pola yang sama dengan web lain | Coba buka alamat sementara. Kalau masih tayang, alihkan ke domain utama |
| 10 | Link keluar | Link ke akun media sosial, Linktree, Discord, atau toko yang juga dipakai brand lain atau akun pribadi pemilik | Daftar semua link keluar di web |
| 11 | Gambar | Avatar, banner, logo, atau karya yang juga tampil di akun lain milik pemilik | Tanyakan ke pemilik, atau sarankan ia mencoba pencarian gambar terbalik |
| 12 | Jalur bayar | Nama yang muncul di PayPal, Wise, rekening bank, QRIS, atau e-wallet di halaman order | Baca halaman order dan instruksi bayar. Ingatkan bahwa nama pemilik rekening terlihat oleh pembeli |
| 13 | Arsip publik | Versi lama web yang menampilkan data yang kini sudah dihapus | Cek arsip web publik (Wayback Machine) untuk domain ini. Salinan arsip tidak bisa dijamin terhapus |

## Cara melaporkan

Di bagian Lapisan tambahan, tulis satu tabel singkat:

| No | Bagian | Temuan | Jenis |
|---|---|---|---|

- Jenis: **Fakta** (terlihat langsung di web atau hasil perintah) atau **Perlu dicek pemilik** (butuh akses ke akun atau layanan yang tidak bisa dibuka Claude).
- Temuan yang perlu diperbaiki masuk Daftar perbaikan. Jejak yang mengaitkan ke data pribadi pemilik atau ke brand lain yang tidak dimaksudkan tampil diberi tingkat **Penting**.
- Butir yang berhubungan dengan akun (WHOIS, registrar, hosting, Cloudflare, analitik) ditulis sebagai langkah untuk pemilik, karena login dikerjakan pemilik sendiri.
- Kalau web memang sengaja terbuka menyebut induk studionya, cukup catat "Disengaja menurut pemilik" dan jangan dijadikan temuan.

Pengaturan hosting dan server yang memisahkan brand ada di skill bangun-website-code, `references/hosting.md`, bagian Kalau punya atau berencana punya beberapa web dan VPS bersama untuk beberapa brand.
