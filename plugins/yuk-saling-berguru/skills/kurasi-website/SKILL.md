---
name: kurasi-website
description: "Gunakan saat artist, studio kreatif, atau pemilik usaha punya website yang sudah jadi atau sudah tayang dan ingin dinilai: skor 11 area, simulasi calon pembeli, checklist niche artist, angka teknis, lalu daftar perbaikan dan prompt perbaikan siap tempel untuk Claude Code. Pemicu: \"kurasi website\", \"kurasi web\", \"kurasi lengkap\", \"kurasi ulang\", \"cek ciri khas brand\", \"review web\", \"audit website\", \"cek website ini\", \"nilai web saya\", \"apa yang kurang dari web ini\", atau saat pengguna mengirim link, screenshot, file HTML, atau folder proyek web sambil minta masukan. Untuk membangun web dari nol pakai bangun-website atau bangun-website-code. Untuk memilih karya yang akan dipajang (kurasi karya di Brand Hub) pakai pemandu-brand-hub."
---

# Kurasi Website

Tugas skill ini: memeriksa website yang sudah ada, menilai tiap area, lalu memberi perbaikan yang bisa langsung dikerjakan. Hasilnya harus siap pakai, bukan teori. Pemilik web harus bisa membaca hasilnya dalam dua menit dan tahu apa yang dikerjakan duluan.

## Cek versi panduan
Versi panduan ini: 0.7.0. Sekali di awal sesi, sebelum mulai bekerja, cek apakah ada versi yang lebih baru. Baca angka `version` di https://raw.githubusercontent.com/mellakamal/yuk-saling-berguru/main/.claude-plugin/marketplace.json (di Claude Code pakai `curl -fsS --max-time 5`, di chat pakai alat buka link kalau ada). Kalau angkanya lebih besar dari versi panduan ini, sampaikan satu kali:

"Ada versi panduan yang lebih baru ([versi]). Di Claude Code, ketik /plugin, update plugin Yuk Saling Berguru, lalu ketik /reload-plugins. Kalau setelah itu masih memakai versi lama, buka sesi baru. Di chat Claude, update plugin lalu mulai chat baru."

Lalu lanjut mengerjakan permintaan pengguna. Kalau versinya sama, link tidak bisa dibuka, atau pengguna tidak mengizinkan, lewati tanpa menyebutnya. Jangan cek lebih dari sekali dalam satu sesi.

## 1. Kenali bahan yang masuk

Bahan bisa datang dalam empat bentuk. Tiap bentuk punya batas cek yang berbeda, jadi sebutkan batas itu di hasil supaya pemilik web tidak mengira semua sudah diperiksa.

| Bahan | Cara periksa | Yang tidak bisa dicek |
|---|---|---|
| Link website live | Buka di browser (built-in browser atau Claude in Chrome). Lihat lebar desktop (sekitar 1440px) dan HP (sekitar 390px), ambil screenshot keduanya, baca teks halaman, cek request jaringan untuk ukuran gambar dan file yang gagal dimuat, cek pesan error di console. Kalau tidak ada browser, pakai WebFetch untuk teks dan meta. | Tanpa browser: tampilan visual, HP, dan kecepatan |
| Screenshot | Nilai dari gambar saja | SEO, kecepatan, link rusak, kode |
| File HTML/CSS | Baca kodenya, cek meta tag, alt gambar, ukuran file gambar, struktur heading, responsif lewat media query | Kecepatan nyata di hosting |
| Folder proyek (Claude Code) | Baca file, jalankan server lokal kalau bisa, buka di browser | Kondisi hosting live, kecuali ada link juga |

Kalau halaman lebih dari satu (misalnya Beranda, Portofolio, Harga, Order), periksa semua halaman utama, bukan hanya beranda.

Jangan tanya-jawab panjang sebelum mulai. Langsung periksa dari bahan yang ada. Kalau ada informasi yang benar-benar menentukan penilaian (misalnya target pembeli web ini siapa), tanyakan satu kali di akhir hasil, bukan di awal.

## 2. Tentukan lapisan pemeriksaan

Pemeriksaan disusun berlapis supaya hasil tetap fokus. Baca hanya file referensi yang lapisannya jalan.

| Lapisan | Kapan jalan | File |
|---|---|---|
| 11 area + rubrik skor | Selalu | `references/checklist.md`, `references/rubrik.md` |
| Cek per halaman | Selalu (one-page: per section) | `references/per-halaman.md` |
| Simulasi calon pembeli | Selalu | `references/simulasi-pembeli.md` |
| Checklist niche | Otomatis kalau web melayani VTuber/Live2D, ilustrasi, maskot, buku anak, game asset, atau TTRPG | `references/niche.md` |
| Cek ciri khas brand | Kalau pengguna bilang "cek ciri khas brand". Otomatis kalau web milik artist atau studio kreatif dan salah satu ini benar: folder proyek tidak punya `BLUEPRINT.md`, blueprint belum punya baris "Pembeda" dan "Alamat halaman", atau bahan hanya berupa link atau screenshot sehingga versinya tidak bisa diketahui. Dalam mode kurasi, cek ini hanya membaca dan melaporkan | `references/ciri-khas.md` |
| Kurasi ulang | Otomatis kalau ada hasil kurasi sebelumnya atau pengguna bilang "kurasi ulang"/"cek lagi" | `references/kurasi-ulang.md` |
| Klien internasional | Otomatis kalau ada teks Inggris, harga USD, link Fiverr/Upwork/VGen, atau target luar negeri | `references/mode-lanjutan.md` bagian A |
| Angka teknis terukur | Otomatis kalau bahan berupa link live atau kode | `references/mode-lanjutan.md` bagian B, `scripts/kontras.py` |
| Tracking dan legal | Otomatis kalau bahan berupa link live atau kode | `references/mode-lanjutan.md` bagian C |
| Bandingkan pesaing | Hanya kalau diminta, ada kata "kurasi lengkap", atau pesaing disebut | `references/mode-lanjutan.md` bagian D |

Kalau pengguna menulis "kurasi lengkap", jalankan semua lapisan yang mungkin dengan bahan yang ada.

Sebutkan lapisan yang dijalankan dalam satu baris di awal hasil, supaya pengguna tahu cakupannya.

## 2b. Periksa 11 area

Detail pertanyaan per area ada di `references/checklist.md`, dan skornya mengikuti `references/rubrik.md`.

Dua skill lain di plugin ini dipakai sebagai patokan supaya penilaian sejalan dengan materi kelas:
- Area Kurasi karya: pakai 10 kriteria di `pemandu-brand-hub/langkah/04-kurasi-karya.md` (9 sampai 12 karya terbaik).
- Area SEO dasar, kalau bahan berupa folder proyek: jalankan `python3 -I <folder skill bangun-website-code>/references/cek-seo.py FOLDER_WEB` dan masukkan temuannya sebagai Fakta.

1. Kesan pertama (5 detik pertama di hero)
2. Pesan brand dan positioning
3. Kurasi karya / portofolio
4. Jalur order dan CTA
5. Harga dan penawaran
6. Copywriting dan bahasa
7. Desain visual dan konsistensi brand
8. Tampilan HP
9. Kecepatan dan teknis
10. SEO dasar
11. Kepercayaan dan kontak

Kalau suatu area tidak berlaku (misalnya web tidak menjual apa pun sehingga area Harga kosong), tulis "Tidak berlaku" dan jangan dipaksakan.

Kalau bahan berupa folder proyek dan tidak ada `BLUEPRINT.md`, `CLAUDE.md`, atau `README.md`, masukkan sebagai temuan Penting di Daftar perbaikan. Tanpa file itu, setiap sesi Claude harus menebak rencana dan keputusan web dari kode, sehingga perbaikan berikutnya mudah keliru. Jadikan butir pertama di prompt: "Buat BLUEPRINT.md, CLAUDE.md, dan README.md dari kode yang ada sebelum mengubah apa pun, ikuti skill bangun-website-code. Tanyakan pembeda studio dan isi baris Pembeda serta Alamat halaman di blueprint."

## 3. Bedakan fakta dan penilaian

Pemilik web perlu tahu mana temuan yang pasti dan mana yang selera. Tandai tiap temuan:

- **Fakta**: bisa dicek ulang. Contoh: "Gambar hero 4,2 MB", "Tombol Order di HP tertutup menu", "Tidak ada meta description".
- **Penilaian**: pendapat berdasarkan praktik umum. Contoh: "Warna aksen kurang kontras dengan latar".

Setiap temuan wajib menyebut lokasinya (halaman dan bagian), supaya bisa langsung ditemukan.

## 4. Format hasil

Hasil utama skill ini adalah **prompt siap tempel untuk Claude Code.** Pengguna utamanya adalah pemilik skill sendiri, yang akan membaca temuan, mencoret yang tidak setuju, lalu menempel prompt ke Claude Code. Jadi temuan di atas prompt dibuat ringkas dan bernomor sama dengan butir di prompt, supaya gampang dicoret.

Pakai urutan ini persis. Jangan tambah bagian kesimpulan atau tips bonus di luar format.

**Ringkasan.** Tiga kalimat: kondisi web secara umum, kekuatan terbesar, masalah terbesar.

**Skor per area.** Tabel:

| Area | Skor (1 sampai 5) | Temuan utama |
|---|---|---|

Skor mengikuti `references/rubrik.md`. Tambahkan skor rata-rata di bawah tabel.

**Perjalanan pembeli.** Tabel hasil simulasi (format di `references/simulasi-pembeli.md`).

**Lapisan tambahan.** Hanya untuk lapisan yang jalan, masing-masing satu tabel singkat: angka teknis, temuan niche, klien internasional, tracking dan legal, pesaing. Temuan yang perlu diperbaiki tidak dijelaskan panjang di sini; cukup masuk Daftar perbaikan.

**Daftar perbaikan.** Tabel bernomor, urut dari yang paling berdampak ke order:

| No | Tingkat | Masalah | Lokasi | Jenis |
|---|---|---|---|---|

- Tingkat: **Wajib** (menghambat orang order, merusak tampilan, atau error), **Penting** (menurunkan kepercayaan atau kejelasan), **Tambahan** (memoles).
- Jenis: Fakta atau Penilaian.

**Prompt untuk Claude Code.** Satu blok kode, siap tempel. Strukturnya:

```
Kamu sedang memperbaiki website [nama/URL]. Kerjakan butir di bawah sesuai urutan.
Sebelum mengubah, baca file yang relevan dulu. Setelah tiap butir Wajib selesai,
cek tampilan di lebar 390px dan 1440px.

WAJIB
1. [Masalah singkat] di [file/bagian kalau diketahui]
   Ubah: [kondisi sekarang] → [kondisi yang diinginkan, spesifik: teks pengganti
   lengkap, ukuran, warna hex, urutan section, ukuran gambar target]
   Selesai kalau: [kriteria yang bisa dicek]

PENTING
...

TAMBAHAN
...

Setelah semua selesai, laporkan butir mana yang sudah dan belum dikerjakan,
lalu tunjukkan screenshot HP dan desktop.
```

Aturan isi prompt:
- Nomor butir sama dengan nomor di tabel Daftar perbaikan.
- Tiap butir harus bisa dikerjakan tanpa konteks percakapan ini. Claude Code tidak melihat screenshot atau temuanmu, jadi tulis teks pengganti lengkap, bukan "perbaiki headline".
- Tiap butir punya "Selesai kalau" supaya Claude Code tahu kapan berhenti.
- Butir Penilaian yang menyangkut copy, warna, atau gaya brand ditandai "(tunjukkan dulu sebelum diterapkan)", karena itu keputusan pemilik brand.
- Kalau nama file belum diketahui (bahan berupa link atau screenshot), tulis bagian halamannya dan minta Claude Code mencari filenya sendiri.
- Kalau URL web belum bersih (kriteria di `references/checklist.md` area 10), jadikan butir sendiri. Tulis daftar alamat lama dan alamat bersih penggantinya satu per satu, minta semua link internal, canonical, og:url, dan sitemap ikut diganti, dan minta alamat lama dialihkan (301) ke alamat baru supaya link yang sudah dibagikan tidak mati. Cara membuang `.html` mengikuti hosting: di GitHub Pages pakai folder `portofolio/index.html` lalu tautkan ke `/portofolio/`, di Vercel pakai `cleanUrls`, di Netlify pakai Pretty URLs. Selesai kalau: semua link di menu dan sitemap tanpa `.html` atau parameter, dan alamat lama terbuka ke alamat baru.

Semua link yang ditulis di hasil kurasi dan di prompt juga ditulis bersih: alamat utama saja, tanpa `index.html`, parameter pelacak (`utm_`, `fbclid`, `gclid`), parameter cek cache (`?x=123`), atau sisa pencarian. Parameter hanya dipertahankan kalau memang bagian dari fungsi, misalnya `?text=` di link WhatsApp.

Di Claude Code dengan akses folder, simpan juga hasil lengkap ke `KURASI-YYYY-MM-DD.md` di akar folder proyek, supaya kurasi ulang nanti bisa membandingkan skor.

**Batas pemeriksaan.** Satu baris: apa yang tidak bisa dicek dari bahan ini dan bahan apa yang perlu dikirim untuk melengkapinya. Lewati kalau semua sudah tercek.

## 5. Aturan bahasa hasil

- Ikuti register pengguna. Kalau ia menulis santai (aku/gue), jawab santai. Kalau baku, jawab baku. Jangan dicampur.
- Ikuti skill `tulisan-tanpa-gaya-ai` untuk semua teks hasil kurasi dan semua teks pengganti yang diusulkan untuk web. Skill itu juga dipakai sebagai patokan saat menilai area Copywriting.
- Jangan pakai kata "kalian" di teks pengganti untuk pengunjung web.
- Angka uang ditulis lengkap: Rp 285.000, bukan 285rb.
- Jangan ulang poin yang sama di dua bagian. Kalau sudah ada di tabel skor, daftar perbaikan cukup berisi tindakannya.

## 6. Kalau pengguna minta langsung dibetulkan

Di Claude Code dengan akses folder: kerjakan butir Wajib dulu, tunjukkan hasilnya (screenshot desktop dan HP), baru lanjut ke Penting setelah pengguna setuju. Perubahan copy dan warna adalah keputusan pemilik brand, jadi tunjukkan dulu sebelum diterapkan ke semua halaman.
