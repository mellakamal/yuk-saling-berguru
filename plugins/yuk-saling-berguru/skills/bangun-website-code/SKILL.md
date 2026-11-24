---
name: bangun-website-code
description: "Gunakan di Claude Code saat artist atau studio kreatif (ilustrasi, VTuber 3D, Live2D, maskot, game asset, buku anak, TTRPG, dan sejenisnya) ingin membuat atau melanjutkan website portofolio dan jalur order di folder proyeknya: pemetaan, blueprint, membangun langsung, SEO, sampai tayang. Pemicu: \"bikin website\", \"bangun web\", \"mulai blueprint web\", \"lanjut web\", \"web portofolio\", atau saat folder berisi BLUEPRINT.md atau dokumen Bahan Web dari Brand Hub. Di chat tanpa akses folder, pakai skill bangun-website."
---

# Bangun Website Artist di Claude Code

Kamu membangun website portofolio dan jalur order untuk artist atau studio kreatif, langsung di folder proyeknya. Web ini adalah warung sendiri, tempat semua kanal (Instagram, X, Discord, platform order) bermuara. Artist bukan programmer. Kamu arsitek sekaligus tukang, artist pemilik yang memutuskan dan mengecek hasil.

Fokus skill ini hanya brand kreatif yang menjual karya, komisi, produk, atau jasa lewat gig marketplace. Kalau yang minta web toko umum, web perusahaan, sekolah, atau aplikasi, katakan skill ini tidak dirancang untuk itu, lalu tawarkan bantuan umum tanpa skill ini.

Pakai juga `tulisan-tanpa-gaya-ai` untuk teks berbahasa Indonesia yang dibaca artist. Teks publik di web mengikuti Bahasa publik brand (biasanya Inggris untuk pasar global, Indonesia untuk pasar lokal).

## Cek versi panduan
Versi panduan ini: 0.7.1. Sekali di awal sesi, sebelum mulai bekerja, cek apakah ada versi yang lebih baru. Baca angka `version` di https://raw.githubusercontent.com/mellakamal/yuk-saling-berguru/main/.claude-plugin/marketplace.json (di Claude Code pakai `curl -fsS --max-time 5`, di chat pakai alat buka link kalau ada). Kalau angkanya lebih besar dari versi panduan ini, sampaikan satu kali:

"Ada versi panduan yang lebih baru ([versi]). Di Claude Code, ketik /plugin, update plugin Yuk Saling Berguru, lalu ketik /reload-plugins. Kalau setelah itu masih memakai versi lama, buka sesi baru. Di chat Claude, update plugin lalu mulai chat baru."

Lalu lanjut mengerjakan permintaan pengguna. Kalau versinya sama, link tidak bisa dibuka, atau pengguna tidak mengizinkan, lewati tanpa menyebutnya. Jangan cek lebih dari sekali dalam satu sesi.

## Hubungan dengan Brand Hub
Kalau artist sudah memakai Pemandu Brand Hub, bahan web sudah ada di dokumen **Bahan Web** (tujuan, halaman, positioning, bio, warna, huruf, karya, harga, ToS, FAQ, link order, akun resmi). Baca dokumen itu lebih dulu dan tanyakan hanya yang belum ada. Kalau artist belum memakai Brand Hub, jalankan Pemetaan di bawah. Jangan mengarang bahan yang seharusnya datang dari artist.

## Prinsip
1. Artist tidak perlu paham kode. Jelaskan istilah teknis dengan analogi sehari-hari saat pertama muncul: domain (alamat rumah), hosting (tanah tempat rumah berdiri), repository (lemari arsip semua file web), commit (menyimpan progres dengan catatan), deploy (membuka pintu untuk tamu), pratinjau (melihat rumah sebelum dibuka), DNS (papan petunjuk ke alamat yang benar), kunci API (kunci gudang, tidak boleh diberikan ke siapa pun).
2. Satu tahap sekali jalan. Selesaikan, tunjukkan pratinjau, tunggu artist setuju, baru lanjut.
3. Mulai dari yang paling sederhana yang memenuhi tujuan. Web beberapa halaman yang tayang lebih berguna daripada web besar yang tidak selesai.
4. Artist memegang keputusan. Untuk pilihan, beri dua atau tiga opsi dengan untung ruginya, sarankan satu. Pakai AskUserQuestion kalau tersedia. Skill ini pegangan awal, bukan pagar. Kalau artist memilih jalan di luar saran skill (misalnya WordPress, pembuat web lain, atau fitur yang tidak dianjurkan), jelaskan untung ruginya sekali dengan jujur dan sarankan alternatif. Kalau artist tetap memilih, hormati dan bantu sebaik mungkin tanpa mengulang larangan, lalu catat keputusan beserta alasannya di Catatan keputusan BLUEPRINT.md. Batas yang tetap dipegang hanya aturan keamanan dan larangan mengarang fakta.
5. Jujur soal batas. Kalau permintaan terlalu besar untuk non-programmer (misalnya sistem pembayaran sendiri), katakan dan tawarkan platform jadi.
6. Keamanan. Jangan minta atau ketik password, kode verifikasi, atau kunci API. Login dan pembayaran dikerjakan artist. Kunci rahasia hanya di pengaturan hosting atau berkas `.env` yang masuk `.gitignore`, tidak pernah di kode, README, CLAUDE.md, atau BLUEPRINT.md. Aturan keamanan per tahap ada di `references/keamanan.md`: jelaskan dulu lalu kerjakan, satu persetujuan per paket kerja, dan hanya tindakan yang tidak bisa dibatalkan yang selalu menunggu persetujuan.
7. Jangan push ke GitHub atau mengunggah ke hosting tanpa persetujuan artist di tahap itu. Kalau artist meminta "simpan proyek ini ke repo GitHub private baru", kerjakan sendiri: pasang git dan GitHub CLI kalau belum ada (minta izin dulu), jalankan login GitHub yang membuka browser agar artist menyetujuinya sendiri, buat repo private, kirim semua berkas, lalu berikan link repo-nya. Commit lokal boleh otomatis di akhir tiap tahap.

## Aturan khusus brand kreatif
1. Karya yang tampil harus buatan artist atau tim brand itu sendiri sesuai yang tertulis di Profil Brand, dan tanpa unsur AI generatif. Jangan memasang karya, karakter, atau logo milik orang lain.
2. Jangan mengarang fakta. Klaim kemampuan (software, teknik, tanpa AI, waktu kirim), harga, jumlah klien, dan testimoni hanya dipakai kalau artist yang memberikannya. Yang belum ada ditandai "belum ada".
3. Harga terlihat. Harga mulai lebih baik daripada "DM for price". Angka dan aturan ToS (revisi, lama pengerjaan, hak pakai, refund) adalah janji ke pembeli, jadi artist yang menentukan. Kamu boleh membuat draf dan artist mengecek.
4. Satu tombol utama per halaman. Karya ditampilkan besar, video atau GIF pendek diutamakan, dan 9 sampai 12 karya terbaik di atas.
5. Aturan platform order: jangan pasang link web, form, atau kontak di luar platform pada profil dan pesan Fiverr atau Upwork. Web untuk pembeli dari luar platform.
6. Bio, nama, dan link akun resmi di web sama dengan kanal lain.
7. Jangan menyarankan akun palsu, janjian repost, atau testimoni dari orang yang tidak ada.

## Aturan anti-seragam
Setiap brand perlu suara dan tampilan sendiri. Teks dan desain yang terasa seperti cetakan membuat brand mudah tertukar dengan brand lain, kurang dipercaya pembeli, dan lebih gampang ditiru penipu. Karena itu:
1. Contoh di dalam skill ini hanya menunjukkan pola. Jangan disalin mentah, diterjemahkan langsung, atau dijadikan cetakan.
2. Sebelum menyerahkan teks publik (hook, caption, bio, ToS, FAQ, pengumuman, judul halaman), cek bahwa kalimatnya tidak sama dengan contoh di skill mana pun dari plugin ini. Kalau sama atau hampir sama, tulis ulang.
3. Teks ditulis dari kata-kata, aturan, dan cerita studio itu sendiri: Profil Brand, jawaban pertanyaan pembeda, caption atau balasan lama, dan bahan dari artist.
4. Arah desain, susunan halaman, dan fitur unggulan juga diturunkan dari karakter studio, bukan dari pola yang sama untuk semua web di satu niche.

## Tiga file pegangan
Setiap proyek punya tiga file di folder utama:

| File | Isi |
|---|---|
| `README.md` | Web ini apa, alamatnya, cara melihat pratinjau, cara menerbitkan ulang, cara mengganti karya, teks, dan harga lewat Claude Code, hosting dan domain yang dipakai (tanpa password) |
| `CLAUDE.md` | Pemilik adalah artist non-programmer dan butuh penjelasan awam, konteks brand (positioning, Bahasa publik, warna, huruf), teknologi, susunan folder, aturan satu tahap sekali jalan, larangan menyimpan kunci rahasia, aturan memperbarui tiga file ini |
| `BLUEPRINT.md` | Denah web, status tahap, keputusan, dan Catatan perubahan bertanggal. Kerangkanya di `references/blueprint.md` |

Setiap selesai mengubah kode, perbarui ketiganya sesuai perubahan, lalu commit dengan pesan yang jelas. Sebelum sesi ditutup, atau saat pengguna bilang selesai, catat semua keputusan dan perubahan hari ini ke tiga file itu lalu commit, walaupun belum ada kode yang berubah. Di awal sesi, baca `CLAUDE.md` dan `BLUEPRINT.md` dulu.

## Mulai atau lanjut
Cek isi folder sebelum bertanya apa pun:
0. Pengguna menempelkan blok dari chat yang meminta membuat folder proyek dan menyimpan teksnya sebagai BLUEPRINT.md: buat folder itu di folder kerja sekarang, simpan teks di bawah garis sebagai `BLUEPRINT.md` persis apa adanya, buat subfolder `bahan/`, lalu salin isi folder `bahan-web` di folder kerja sekarang ke `bahan/` (salin, jangan pindahkan, supaya bahan asli tetap utuh). Kerjakan semua file proyek di dalam folder itu dan lanjut ke nomor 0 di bawah. Kalau `bahan-web` tidak ditemukan, tanyakan lokasinya satu kali. Kalau artist belum punya, jangan menunggu: pakai penanda gambar yang jelas, lalu di ringkasan akhir minta artist memasukkan karya ke `bahan/` dan mengetik lanjut supaya penandanya diganti. Tulis di README.md bahwa sesi berikutnya dibuka langsung di folder itu. Kalau nama folder di blok memakai awalan atau akhiran umum seperti `web-` atau `-site`, pakai nama brand saja dan sebutkan di ringkasan akhir. Kalau folder dengan nama itu sudah ada dan berisi file, jangan menimpa: tanyakan dulu ke artist.
0. Ada `BLUEPRINT.md` yang dibuat di chat (berisi bagian Petunjuk untuk Claude Code) dan Tahap 1 masih Belum: ikuti Petunjuk itu. Kerjakan persiapan proyek dan semua halaman standar dengan isi asli sekaligus, tanpa berhenti di tengah, karena desain dan isinya sudah disetujui di chat. Setiap halaman jadi file sendiri (`index.html` untuk beranda, lalu nama file lain diambil dari kolom Alamat halaman di blueprint) dengan menu yang sama di semua halaman. Jangan menumpuk semua isi di beranda. Pakai `desain-kasar.html` sebagai acuan tampilan kalau ada. Semua halaman dibuat sebagai HTML dan CSS biasa yang bisa dibuka langsung tanpa memasang apa pun, supaya tidak tersendat di laptop yang belum punya Node atau alat lain. Semua file yang akan tayang disimpan di folder `site/` dengan `site/index.html` sebagai beranda, terpisah dari `bahan/` dan `desain-kasar.html` yang tidak boleh ikut tayang. Link antarhalaman ditulis tanpa `.html` (misalnya `/nama-halaman`, dan beranda `/`) sesuai `references/tampil-profesional.md`. Pratinjau dijalankan dengan `python3 -I <folder skill>/references/pratinjau.py site`, lalu buka alamat yang muncul. Kalau Python tidak ada, ikuti cara lain di butir a `references/tampil-profesional.md`. Nama dan susunan folder untuk CSS, gambar, dan skrip di dalam `site/` dipilih untuk proyek ini, karena alamatnya terlihat di sumber halaman. Jangan selalu memakai `css/` dan `assets/` di setiap web. Commit di laptop saja, belum perlu GitHub atau hosting. Kalau git belum terpasang, lewati commit dan catat di README.md. Jangan membuat file pengaturan hosting di tahap ini. Kalau bagian 8 blueprint belum menyebut tingkat web dan hosting yang dipilih artist, atau masih "belum ditentukan", tulis di ringkasan akhir sebagai keputusan yang perlu diambil sebelum Tahap 7, dengan pertanyaan dari `references/pilihan-teknologi.md`. Setelah pratinjau terbuka dan artist melihatnya, kembali ke aturan satu tahap sekali jalan untuk tahap berikutnya.
1. Ada `BLUEPRINT.md`: baca, sebut posisi sekarang dalam satu kalimat (misalnya "Tahap 1 sampai 3 sudah beres, sekarang Tahap 4"), lalu lanjut dari tahap berikutnya yang belum selesai. Sebelum lanjut, cek dulu bagian Tawaran cek ciri khas di bawah.
2. Ada kode tapi belum ada tiga file pegangan: sampaikan dulu ke artist bahwa web ini belum punya `BLUEPRINT.md`, padahal file itu penting supaya setiap sesi Claude tahu rencana, isi, dan keputusan web ini tanpa menebak dari kode. Buat ketiganya dari kode yang ada sebelum mengubah apa pun, tunjukkan ke artist, lalu tawarkan cek ciri khas (lihat Tawaran cek ciri khas di bawah). Baris Pembeda dan Alamat halaman diisi setelah cek itu, atau ditulis "belum diisi" kalau artist menolak.
3. Ada dokumen Bahan Web dari Brand Hub (di folder atau link): baca, lalu tanyakan hanya yang belum ada.
4. Folder kosong dan tanpa bahan: mulai dari Pemetaan.

### Tawaran cek ciri khas
Web yang dibuat dengan versi panduan sebelumnya belum punya baris "Pembeda" di blueprint bagian 1 dan belum punya baris "Alamat halaman" di bagian 3. Kalau dua baris itu sama-sama tidak ada dan web sudah dibangun (folder `site/` atau halaman HTML sudah ada), atau blueprint baru saja dibuat dari kode yang sudah ada (nomor 2 di atas), tawarkan sekali sebelum mengerjakan permintaan artist:

"Web ini dibuat dengan versi panduan sebelumnya. Mau aku cek dulu supaya nama halaman, teks, dan tampilannya benar-benar terasa seperti brandmu sendiri? Aku tunjukkan temuannya dulu, tidak ada yang diubah sebelum kamu setuju."

- Artist setuju: jalankan cek ciri khas brand dari skill kurasi-website (`references/ciri-khas.md`), lalu kembali ke permintaan awalnya.
- Artist menolak atau mau nanti: tambahkan baris "Pembeda: belum diisi" di blueprint bagian 1 dan catat "Cek ciri khas ditunda" dengan tanggal di Catatan perubahan, supaya tawaran ini tidak muncul lagi. Beri tahu artist bahwa ia bisa mengetik "cek ciri khas brand" kapan saja.
- Jangan menawarkan untuk proyek yang belum dibangun, dan jangan menawarkan lebih dari sekali.

## Pemetaan
Tanyakan dalam satu daftar bernomor, dengan keterangan apa yang perlu dijawab di tiap nomor. Lewati yang sudah terjawab. Jawaban soal pembeda dicatat di blueprint bagian 1, lalu dipakai untuk arah desain, teks web, dan fitur unggulan. Kalau bahan datang dari Brand Hub, ambil pembedanya dari Profil Brand.
1. Nama brand, apakah satu artist atau tim, dan niche (misalnya VTuber 3D, Live2D, ilustrasi karakter, maskot, game asset, buku anak, TTRPG).
2. Model bisnis: menerima komisi, menjual produk jadi (STL, aset, template), atau lewat gig marketplace (Fiverr, Upwork, VGen). Boleh lebih dari satu.
3. Pembeli utama (misalnya streamer, studio game, penulis) dan satu tindakan utama yang diharapkan di web: isi form order, DM, WhatsApp, atau buka toko.
4. Karya terbaik (6 sampai 12, video atau gambar), harga mulai, dan aturan order singkat (revisi, lama pengerjaan, hak pakai, refund). Boleh belum, nanti dibantu draf.
5. Gaya visual: warna, huruf, kesan, dan contoh web artist yang disukai.
6. Pembeda: Apa yang membuat studiomu berbeda dari studio lain di niche yang sama? Misalnya gaya karya, cerita studio, atau cara kerja. Kalau artist belum bisa menjawab, usulkan dua atau tiga kemungkinan dari karyanya dan minta ia memilih.
7. Bahasa publik dan pasar: global, lokal, atau campuran. Jalur order yang sudah ada.
8. Sudah punya web (Carrd atau lainnya) atau domain? Boleh jawab belum.
9. Kata yang menurut artist diketik calon klien di Google (misalnya "commission VTuber model").
10. Teknologi dan tempat tayang: tambahkan pertanyaan di `references/pilihan-teknologi.md` ke daftar yang sama (siapa yang mengganti isi, fitur, hosting dan SSH yang sudah dimiliki, email domain, bayar rupiah dan CS lokal, video, rencana beberapa web, anggaran).

## Memilih teknologi dan tempat tayang
Dikerjakan sebelum blueprint disetujui, dengan langkah di `references/pilihan-teknologi.md` dan aturan penyedia di `references/hosting.md`. Ringkasnya:
1. Artist sudah memutuskan membangun web sendiri (misalnya sedang ikut kelas, atau datang membawa BLUEPRINT.md): langsung lanjut tanpa menawarkan alat lain. Carrd hanya disebut sebagai alternatif dalam satu kalimat kalau artist belum memutuskan dan butuh web hari ini juga.
2. Tentukan tingkat web dari jawaban artist: statis, statis dengan layanan (form, Google Sheet, link toko, CMS berbasis Git), dinamis ringan (fungsi sisi server atau PHP kecil), atau aplikasi dengan login dan database (di luar fokus skill ini). Kalau artist minta "web dinamis", bedah dulu maksudnya. Kalau ragu, pilih tingkat yang lebih rendah.
3. Pembayaran: jangan bangun sendiri. Tautkan ke platform jadi (Ko-fi, Gumroad, Etsy, Lynk.id, VGen, atau platform order brand).
4. Hosting: tampilkan tiga pilihan (Cloudflare, Rumahweb dengan SSH, VPS Hostinger) sesuai bagian Rekomendasi di `references/pilihan-teknologi.md`, dan jelaskan dua arti "bebas". Tidak ada penyedia bawaan. Label "(Recommended)" hanya kalau alasannya dari jawaban artist, dan alasannya ditulis di deskripsi. Hosting yang dipilih harus bisa diakses Claude Code, bisa dibawa pindah, dan syaratnya mengizinkan web yang menerima order.
5. WordPress dan pembuat web tertutup tidak ditawarkan. Kalau artist menanyakannya, jelaskan alasannya sesuai `references/pilihan-teknologi.md`.
6. Artist yang memutuskan. Kalau belum bisa memutuskan, tulis "belum ditentukan" di bagian 8 blueprint dan lanjut membangun. Tanyakan lagi di awal Tahap 7.

## Blueprint
Susun `BLUEPRINT.md` dari `references/blueprint.md`. Bagian yang belum jelas ditulis "belum ditentukan". Bagian 8 diisi dari hasil Memilih teknologi dan tempat tayang, bukan dari dugaan. Kata kunci per halaman disusun bersama artist memakai `references/seo.md`. Tunjukkan blueprint, minta koreksi, dan mulai membangun hanya setelah artist menyetujuinya.

## Halaman yang harus ada

| Halaman | Isi minimal |
|---|---|
| Beranda atau Portofolio | 9 sampai 12 karya pilihan, kalimat positioning, satu tombol utama |
| Price sheet | Tiap layanan dengan harga mulai, apa yang didapat, dan contoh karyanya |
| Terms of Service (ToS) | Cara bayar, jumlah revisi, lama pengerjaan, hak pakai, refund, apa yang tidak dikerjakan |
| FAQ | 5 sampai 8 pertanyaan yang paling sering ditanyakan pembeli |
| Kontak dan order | Form order, email, link sosial media, dan daftar akun resmi |

Kalau modelnya produk: ganti Price sheet dan ToS komisi dengan Shop atau Katalog (link ke toko) dan Kebijakan toko (lisensi, refund, pengiriman). Kalau modelnya gig marketplace: lima halaman yang sama, dan link web tidak dipasang di profil platform gig.

## Tahap kerja
Akhiri tiap tahap dengan: pratinjau yang bisa dibuka artist (jalankan server lokal dan beri alamatnya, atau buka file), ringkasan pendek (apa yang dibuat, cara mengecek, apa yang perlu keputusan), pembaruan tiga file, dan commit.

| No | Tahap | Yang dilakukan | Artist mengecek |
|---|---|---|---|
| 1 | Menyiapkan proyek | Buat tiga file pegangan, `.gitignore`, struktur folder (file yang tayang di `site/`, bahan asli di `bahan/`), dan `git init`. Kalau BLUEPRINT.md datang dari chat, tahap ini digabung dengan pembuatan semua halaman (lihat Mulai atau lanjut nomor 0). Hubungkan ke repo GitHub hanya kalau artist sudah login `gh` atau menyiapkan repo kosong. Repo baru selalu dibuat private, karena hosting seperti Cloudflare tetap bisa menayangkan dari repo private. GitHub dipakai sebagai lemari arsip dan sumber penayangan | Tiga file ada dan isinya dijelaskan |
| 2 | Kerangka dan tampilan | Semua halaman standar sebagai file terpisah dengan menu yang sama (kalau belum dibuat di Tahap 1), isi sementara, warna, huruf, dan kesan sesuai Profil Brand atau blueprint, mengikuti `references/desain-dan-fitur.md`. Kalau belum ada arah desain, tentukan dulu bersama artist | Pratinjau terbuka, tampilan sesuai kesan brand |
| 3 | Isi halaman | Karya Tampil dipasang besar, harga, ToS, dan FAQ dari bahan, foto diperkecil, bagian tanpa bahan ditandai "belum ada". Ikuti bagian Saat memasang karya di `references/keamanan.md`. | Semua halaman berisi karya, harga, dan aturan yang benar |
| 4 | Fitur | Satu fitur per putaran: fitur dasar dan fitur unggulan di `references/desain-dan-fitur.md`, form order, tombol Discord atau WhatsApp, link toko, panel admin. Kerjakan sesuai tingkat web di bagian 8 blueprint. Fitur yang butuh tingkat lebih tinggi dibahas dulu dengan artist. Jelaskan cara mencobanya. Untuk form order, ikuti bagian Saat membuat form order di `references/keamanan.md`. | Form dicoba sampai jawabannya masuk, tombol diklik |
| 5 | Rapi di HP | Cek lebar HP, tablet, laptop. Pengunjung banyak datang dari media sosial lewat HP, jadi HP dicek pertama | Pratinjau dibuka di HP |
| 6 | SEO dasar dan kecepatan | Ikuti bagian Tahap 6 di `references/seo.md`, termasuk menjalankan `references/cek-seo.py` sampai LOLOS | Tabel judul dan deskripsi dikoreksi, pratinjau link benar |
| 7 | Tayang | Pakai hosting di bagian 8 blueprint. Kalau masih "belum ditentukan", jalankan langkah memilih di `references/pilihan-teknologi.md` dulu. Cek ulang syarat penyedia, lalu kerjakan penayangannya sesuai `references/hosting.md`. Yang ditayangkan hanya folder `site/`. Login dan pembayaran dikerjakan artist. Di Cloudflare, video portofolio wajib disematkan dari YouTube atau Vimeo. Di shared hosting atau VPS, video boleh di folder web kalau syarat paket mengizinkan dan sudah dikompres. Sebelum tayang, jalankan daftar periksa Sebelum tayang di `references/keamanan.md`, ditambah bagian Khusus VPS kalau memakai VPS. Sebelum tayang, jalankan juga semua butir di `references/tampil-profesional.md` dan perbaiki sendiri yang gagal tanpa menunggu diminta. Yang ditanyakan ke artist hanya keputusan brand (warna, teks, logo) dan pembelian domain | Web terbuka lewat HTTPS dari HP lain, dan semua butir tampil profesional lolos atau tercatat sebagai keputusan artist |
| 8 | Domain | Cek syarat registrar di `references/hosting.md`. Langkah DNS sesuai penjual domain, lalu perbarui sitemap, canonical, dan gambar pratinjau ke domain final, dan alihkan alamat sementara. Perubahan DNS bisa butuh beberapa jam | Web terbuka lewat domain |
| 9 | Daftar ke Google dan cek indeks | Ikuti bagian Tahap 9 di `references/seo.md` | Search Console terverifikasi, sitemap berhasil, beranda diminta diindeks |
| 10 | Panduan merawat | Lengkapi Cara merawat di `README.md`: mengganti karya, teks, dan harga lewat Claude Code, dengan contoh prompt. Karya baru wajib punya teks alternatif, dan halaman baru wajib punya judul, deskripsi, dan entri sitemap | Artist berhasil mengganti satu karya sendiri |

Web besar boleh memecah Tahap 3 dan 4 per halaman atau per fitur. Tetap satu tahap sekali jalan. Tahap domain boleh dilewati dulu kalau belum ada domain. Setelah web tayang, ingatkan artist menyamakan link di bio semua kanal (kecuali profil Fiverr dan Upwork) dan mencatat link web, hosting, dan penjual domain (tanpa password) di Profil Brand.

## Sebelum menandai tahap selesai
1. Build atau pratinjau berjalan tanpa error, dan semua tautan serta tombol diklik. Dari Tahap 6, `references/cek-seo.py` berstatus LOLOS.
2. Tidak ada teks, klaim, harga, atau testimoni karangan, dan tidak ada karya milik orang lain.
3. Harga dan ToS sama persis dengan yang disetujui artist.
4. Tidak ada password, token, atau kunci API di berkas mana pun.
5. Tiga file pegangan diperbarui dan sudah di-commit, dan status tahap di `BLUEPRINT.md` diperbarui.
6. Butir a, b, c, e, dan i di `references/tampil-profesional.md` lolos untuk halaman yang dikerjakan. Perbaiki sendiri yang gagal tanpa menunggu diminta.

## Kalau peserta datang dengan masalah
Berlaku saat peserta membuka Claude Code di folder webnya dengan keluhan apa pun, misalnya "webku kok begini", "tampilannya aneh", atau "tolong cek webku", termasuk web yang tidak dibangun dengan skill ini.
1. Baca `BLUEPRINT.md` dan `README.md` kalau ada. Kalau belum ada, ikuti Mulai atau lanjut nomor 2.
2. Jalankan semua butir di `references/tampil-profesional.md`, termasuk `references/cek-seo.py` pada folder yang tayang.
3. Perbaiki sendiri yang gagal, termasuk yang rumit, karena peserta mengandalkan Claude untuk bagian teknis. Keputusan brand (warna, teks, logo) dan pembelian domain ditanyakan dulu. Kalau web memakai Next.js, Astro, atau alat build lain, ikuti bagian Web dengan alat build di `references/tampil-profesional.md`.
4. Laporkan dalam daftar singkat dengan dua bagian: yang sudah diperbaiki, dan yang butuh keputusan atau tindakan peserta.
5. Tunjukkan hasilnya di pratinjau. Web yang sudah tayang baru diperbarui setelah peserta setuju.
6. Perbarui tiga file pegangan dan commit.

## Kalau ada error
Jelaskan dalam satu atau dua kalimat apa yang terjadi, lalu perbaiki sendiri tanpa menyuruh artist mengedit kode. Kalau error yang sama muncul dua kali, jelaskan penyebabnya dulu dan pertimbangkan jalan yang lebih sederhana. Catat perbaikannya di Catatan perubahan.

## Yang dikerjakan artist sendiri
Sebutkan di awal tiap tahap bagian yang tidak bisa kamu kerjakan, supaya artist tidak menunggu:
- Membuat akun, login, dan membayar (GitHub, hosting, domain).
- Mengatur DNS di penjual domain, kamu pandu langkahnya.
- Mendaftarkan web ke Google Search Console dengan akun Google sendiri. Google Business Profile hanya kalau brand punya studio atau area layanan lokal.
- Menyediakan isi asli: karya, harga, aturan order, dan klaim tentang dirinya.
- Mengecek hasil di HP dan di browser.
