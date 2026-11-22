# Kerangka Blueprint Website Artist

Isi setiap bagian dari jawaban Pemetaan, lampiran di chat, folder `bahan-web` di laptop, dokumen Bahan Web Brand Hub, dan keputusan desain kasar. Bagian yang belum jelas ditulis "belum ditentukan", jangan dikarang. Kalau file ini dibuat di chat untuk dibawa ke Claude Code, bagian 0 wajib ditulis lengkap.

```markdown
# Blueprint Website [nama brand]

Disusun: [tanggal]
Pemilik: [nama artist atau studio]

## 0. Petunjuk untuk Claude Code
Pemilik web ini artist atau studio, bukan programmer. Jelaskan setiap langkah dengan bahasa sehari-hari dan tanya dulu kalau ada pilihan.

Saat diminta "Baca BLUEPRINT.md lalu bangun websitenya" (atau "bangun halaman pertamanya"), kerjakan sekaligus tanpa berhenti di tengah:
1. Baca seluruh file ini. Kalau isi file ini ditempel di chat bersama perintah membuat folder, buat folder dan file-nya dulu, lalu kerjakan semuanya di dalam folder itu. Kalau ada `desain-kasar.html` di folder yang sama, jadikan acuan tampilan. Salin karya dari folder `bahan-web` di folder kerja ke `bahan/` kalau ada. Kalau karya asli belum ada, pakai penanda gambar dan minta artist memasukkan karyanya setelah pratinjau terbuka.
2. Buat `README.md`, `CLAUDE.md`, dan `.gitignore` sesuai aturan tiga file pegangan, lalu `git init`. Di `CLAUDE.md` tulis aturan ini: setiap selesai mengubah kode, perbarui `README.md`, `CLAUDE.md`, dan `BLUEPRINT.md` lalu commit. Sebelum sesi ditutup, atau saat pengguna bilang selesai, catat semua keputusan dan perubahan hari ini ke tiga file itu lalu commit, walaupun belum ada kode yang berubah. Kalau git belum terpasang di laptop, lewati git dan catat di README.md, jangan berhenti karena itu.
3. Bangun semua halaman di bagian 3 sebagai file terpisah (satu halaman satu topik sesuai kata kuncinya), dengan menu yang sama di setiap halaman dan beranda yang pendek. Link antarhalaman ditulis tanpa `.html` (misalnya `/nama-halaman`, dan beranda `/`), dan semua halaman mengikuti `references/tampil-profesional.md` di skill bangun-website-code. Pakai HTML dan CSS biasa di folder `site/` yang bisa dibuka langsung dengan klik dua kali, tanpa memasang apa pun. `bahan/` dan `desain-kasar.html` tetap di luar `site/` supaya tidak ikut tayang. Jangan membuat file pengaturan hosting dulu. Hosting di bagian 8 baru dikerjakan di Tahap 7, dan kalau masih "belum ditentukan", sebutkan di ringkasan akhir sebagai keputusan yang perlu diambil. Pindah ke teknologi lain di bagian 8 baru di tahap berikutnya, setelah pemilik setuju. Pakai gaya di bagian 6 dan aturan di `references/desain-dan-fitur.md` dari skill bangun-website-code: tampilan tidak boleh disederhanakan jadi template umum, dan fitur unggulan di bagian 5 ikut dibuat. Pakai isi asli dari bagian 1, 4, dan 7. Bagian yang bahannya belum ada ditandai "belum ada", tidak dikarang.
4. Commit di laptop. Belum perlu GitHub atau hosting.
5. Buka pratinjau di browser dan jelaskan cara melihatnya.
6. Perbarui status Tahap 1 di bagian 9 dan Catatan perubahan, lalu tulis ringkasan pendek: apa yang dibuat, cara mengecek, dan apa yang perlu keputusan pemilik.

## 1. Brand dan tujuan
- Niche dan layanan: ...
- Model bisnis: komisi, produk, atau gig marketplace (boleh lebih dari satu)
- Positioning satu kalimat: ...
- Pembeda dari studio lain di niche yang sama: ... (dari jawaban pertanyaan pembeda, dipakai untuk desain, teks, dan fitur unggulan)
- Tindakan utama pengunjung: ... (satu saja: isi form order, DM, WhatsApp, atau buka toko)
- Ukuran berhasil: ... (misalnya 5 inquiry per minggu dari web)

## 2. Pembeli
- Siapa: ... (misalnya streamer, studio game, penulis)
- Datang dari mana: ... (Instagram, X, Discord, Google, platform order)
- Yang mereka cari: ...
- Kata yang mereka ketik di Google: ... (atau "belum ditentukan")
- Bahasa publik dan pasar: ... (global, lokal, atau campuran)

## 3. Halaman
| Halaman | Isi | Tombol utama | Kata kunci utama dan pendukung |
|---|---|---|---|
| Beranda atau Portofolio | 9 sampai 12 karya pilihan | ... | ... |
| Price sheet | ... | ... | ... |
| ToS | ... | ... | ... |
| FAQ | ... | ... | ... |
| Tentang | Cerita singkat artist, gaya karya, tautan akun resmi | ... | ... |
| Kontak dan order | ... | ... | ... |

Alamat halaman (nama file): ... Ditulis per halaman dari kata kunci dan Bahasa publik brand, pendek, huruf kecil, dipisah tanda hubung. Nama halaman di menu juga memakai kata-kata brand. Jangan memakai daftar nama file dan nama menu yang sama untuk semua web, misalnya selalu pricing, tos, dan about.

## 4. Layanan dan harga
| Layanan | Harga mulai | Yang didapat | Contoh karya |
|---|---|---|---|
| ... | ... | ... | ... |

Aturan order: revisi ..., lama pengerjaan ..., hak pakai ..., refund ...

## 5. Fitur dan jalur order
| Fitur | Keterangan | Perlu simpan data? |
|---|---|---|
| Form order | Google Form, Tally, atau Formspree | Ya, di layanan form |
| Fitur unggulan | Satu sampai dua, dari `desain-dan-fitur.md` | ... |
| ... | ... | ... |

## 6. Gaya visual
- Warna: ... (kode warna kalau ada)
- Huruf: ...
- Kesan: ...
- Contoh web artist yang disukai: ...
- Arah desain: kesan dalam tiga kata, sumber warna dari karya, dan elemen khas
- Huruf judul dan huruf isi: ...
- Desain kasar yang disetujui: ... (urutan bagian tiap halaman dan catatan koreksi, ditambah file `desain-kasar.html` kalau ada)

## 7. Bahan
| Bahan | Status | Lokasi file |
|---|---|---|
| Karya Tampil | Ada atau Belum | ... |
| Logo dan foto profil | ... | ... |
| Teks (bio, harga, ToS, FAQ) | ... | ... |
| Akun resmi dan link | ... | ... |

## 8. Teknologi dan tempat tayang
Diisi dari langkah memilih di `pilihan-teknologi.md`. Jangan diisi tanpa menanyakan artist.
- Tingkat web: ... (statis, statis dengan layanan, atau dinamis ringan)
- Yang mengganti isi: ... (lewat Claude Code, atau panel admin dari CMS berbasis Git)
- Hosting: ... dan alasannya (atau "belum ditentukan")
- Akses Claude Code ke hosting: ... (login penyedia, SSH, atau unggah manual lewat File Manager)
- Email domain: ... (kotak email di hosting, penerusan ke Gmail, atau tidak perlu)
- Video: ... (disematkan dari YouTube atau Vimeo, atau di folder web)
- Domain: ... (atau "belum ada")
- Form dan fitur data: ...
- Crawler AI: ... (izinkan pencarian AI tapi tolak pelatihan, izinkan semua, atau tolak semua)

## 9. Rencana tahap
| No | Tahap | Status |
|---|---|---|
| 1 | Menyiapkan proyek dan semua halaman | Belum |
| 2 | Kerangka dan tampilan halaman lain | Belum |
| 3 | Isi halaman | Belum |
| 4 | Fitur | Belum |
| 5 | Rapi di HP | Belum |
| 6 | SEO dasar dan kecepatan | Belum |
| 7 | Tayang | Belum |
| 8 | Domain | Belum |
| 9 | Daftar ke Google dan cek indeks | Belum |
| 10 | Panduan merawat | Belum |

## 10. Catatan keputusan
- [tanggal] [keputusan] karena [alasan]

## 11. Catatan perubahan
- [tanggal] [apa yang berubah di web, di tahap mana]
```

Perbarui kolom Status, Catatan keputusan, dan Catatan perubahan setiap kali satu tahap selesai, kode berubah, atau rencana berubah.
