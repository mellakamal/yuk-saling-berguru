---
name: resume-meeting
description: "Gunakan saat pengguna meminta Claude mengawal meeting atau kelas untuk notulensi, atau meminta resume, ringkasan, atau notulensi dari catatan mentah, termasuk saat ia menulis \"kawal meeting\" atau \"susun resume\"."
---

# Resume Meeting

Susun resume meeting atau kelas dari catatan mentah dengan metode "catat dulu, susun belakangan". Resume adalah sari yang bisa dibawa pulang, bukan salinan semua yang dibicarakan.

Skill ini dipakai bersama `slide-presentasi` (tampilan dan tata tulis slide) dan `tulisan-tanpa-gaya-ai` (tanda baca dan pola kalimat). Kalau ada aturan yang bertabrakan, aturan slide menang untuk isi slide.

## Alur singkat
Membuka ("kawal meeting"), mencatat selama meeting berjalan, menyusun ("susun resume"), memeriksa, lalu mengirim PDF. Jangan melompati tahap dan jangan menyusun sebelum diminta.

## Profil penyusun
Resume selalu punya penyusun, dan tiap penyusun punya palet sendiri agar resume tiap orang bisa dibedakan.

1. Cek dulu apakah nama dan palet penyusun sudah tersimpan di memori atau preferensi pengguna. Kalau sudah, pakai tanpa bertanya.
2. Kalau belum, tanyakan sekali di Tahap 0: nama penyusun, dan palet yang diinginkan (tiga warna, misalnya biru tua, krem, oranye). Kalau pengguna belum punya ide, tawarkan tiga pilihan palet yang berbeda karakter dan biarkan ia memilih.
3. Setelah dipilih, sarankan pengguna menyimpannya sebagai preferensi agar tidak ditanya lagi di meeting berikutnya.
4. Resume yang disusun orang lain memakai palet orang itu, bukan palet pengguna.

## Gaya bahasa
- Bahasa Indonesia santai tetapi baku ringan.
- Tanpa "kamu" dan "aku" di slide. Pakai bentuk netral atau "kita".
- Nama orang mengikuti ejaan dan sapaan yang dipakai pengguna (misalnya Mas, Mbak, Pak, Bu, atau tanpa sapaan). Satu orang disebut dengan cara yang sama sepanjang resume.
- Anak magang diberi (magang) setelah namanya bila pengguna menyebutnya magang.
- Kata dari bahasa daerah dan Inggris yang belum baku boleh ditulis miring. Satu istilah ditulis seragam sepanjang resume.
- Ucapan penting pembicara dikutip langsung bila bunyi katanya yang penting, selain itu diringkas. Putuskan sesuai konteks dan jangan mengubah makna.
- Pakai analogi sehari-hari. Jawaban singkat dan nyaman dibaca di HP.

## Kurasi (wajib di setiap resume)
1. Ada ruh dan maknanya. Setiap poin menjelaskan apa yang disampaikan dan kenapa itu penting, atau bagaimana kaitannya dengan ucapan lain di forum. Jangan sekadar kalimat lepas atau label tanpa penjelasan. Isi yang terlalu tipis dilengkapi dari catatan, bukan dikarang.
2. Sesuai sumber. Setiap kalimat dicocokkan dengan slide atau bahan sumber dan catatan forum. Kalau slide dan ucapan pembicara saling melengkapi, satukan keduanya. Jangan menyederhanakan sampai maknanya bergeser (misalnya dana yang masih harus dikumpulkan jangan ditulis seolah sudah ada).
3. Diksi tepat, tidak harus baku. Kata daerah dan Inggris diberi padanan dalam kurung saat pertama muncul, misalnya jagongan (obrolan santai), seduluran (persaudaraan). Kata asli pembicara tetap dipakai, padanannya di dalam kurung.
4. Singkatan ditulis panjang saat pertama muncul, misalnya balik modal (ROI), upah minimum regional (UMR). Istilah Inggris di tabel dan label diganti bahasa Indonesia.
5. Helicopter view. Prinsip ditulis dari sudut pandang keseluruhan, tidak dipersempit ke satu orang. Contoh: "keuangan terbuka di dalam dan terjaga dari pihak luar", bukan "terbuka kepada satu orang tertentu".
6. Analogi pembicara ditulis sebagai analogi ("ibarat"), jangan dibuat harfiah, agar tidak salah persepsi.
7. Kalimat penghubung atau tafsiran yang tidak diucapkan persis di forum boleh dipakai untuk memperjelas makna, tetapi sebutkan ke pengguna saat mengirim agar ia bisa mengecek.

## Tahap 0: Membuka (saat pengguna menulis "kawal meeting")
1. Tanyakan dalam satu daftar bernomor hal yang belum disebut: nama meeting, tanggal dan tempat, peserta, dan siapa penyusun resume (beserta paletnya bila belum tersimpan, lihat Profil penyusun).
2. Bila pengguna langsung mengirim catatan, jangan menahan. Catat dulu, data yang kurang ditanyakan sebelum menyusun.
3. Balas pendek bahwa Claude siap mencatat.

## Tahap 1: Mencatat
1. Rapikan setiap potongan catatan jadi poin ringkas. Jangan menambah isi yang tidak ada di catatan.
2. Tandai bagian yang meragukan atau mungkin salah dengar dengan (?). Jangan menebak.
3. Beri label pada poin yang jenisnya jelas: [Keputusan], [Tindak lanjut], [Angka]. Tindak lanjut dicatat dengan siapa, apa, kapan. Bagian yang belum disebut ditandai (?). Label hanya penanda kerja dan tidak ditampilkan di slide.
4. Catatan bisa berupa ketikan atau foto papan dan slide. Perlakukan sama.
5. Jangan menyusun resume sebelum diminta. Balasan di tahap ini pendek saja: poin yang sudah dirapikan, tanpa komentar atau saran.

## Tahap 2: Menyusun (saat pengguna menulis "susun resume")
1. Kumpulkan seluruh catatan dari chat ini. Bila ada (?) yang menyangkut keputusan, nama, atau angka, tanyakan dulu dalam satu daftar bernomor. Bila pengguna meminta lanjut, susun dengan (?) tetap terlihat.
2. Urutkan: konteks, poin utama, keputusan, tindak lanjut (siapa, apa, kapan).
3. Isi hanya dari catatan. Tampilan mengikuti arahan pengguna.
4. Aturan penulisan notulensi:
   - Keputusan ditulis dengan pelaku yang jelas. Tulis "Rina menyusun daftar gaji", jangan "Daftar gaji akan disusun".
   - Tenggat ditulis dengan tanggal, bukan "minggu depan". Bila catatan hanya menyebut "minggu depan", hitung dari tanggal meeting dan tandai (?) bila ragu.
   - Singkatan dipanjangkan saat pertama muncul.
   - Angka dan nama dicocokkan dengan catatan sumber.
5. Di akhir, daftarkan semua tanda (?) yang belum terjawab.
6. Jangan mengarang nama, angka, tanggal, atau keputusan. Bila data kurang, tulis jelas bahwa datanya belum ada.

## Bentuk
- Default: deck slide, dibangun sebagai PPTX. Ikuti bentuk lain bila diminta.
- Urutan slide baku: sampul, konteks, poin utama, keputusan, tindak lanjut, penutup. Judul tiap slide berupa kalimat pesan, sesuai `slide-presentasi`.
- Sampul atau slide penutup memuat "Catatan disusun oleh [nama penyusun]".
- Warna mengikuti palet penyusun.
- Urutan kirim: PDF dulu untuk ditinjau. Kirim PPTX hanya setelah pengguna menyatakan OK.

## Pemeriksaan sebelum menyerahkan
- Cocokkan setiap fakta dengan catatan sumber dan slide sumber.
- Sisir ulang semua slide dengan bagian Kurasi: makna, kesesuaian sumber, diksi dan padanan, singkatan, helicopter view.
- Satu istilah dan satu sebutan orang seragam di seluruh deck.
- Pastikan tidak ada "kamu" atau "aku" di slide.
- Setiap tindak lanjut punya siapa, apa, kapan, atau bertanda (?).
- Tidak ada tanda baca khas AI di slide: garis panjang, titik tengah, garis tegak, titik koma, judul dua bagian dengan titik dua.
- Sebutkan singkat apa yang masih bertanda (?).
