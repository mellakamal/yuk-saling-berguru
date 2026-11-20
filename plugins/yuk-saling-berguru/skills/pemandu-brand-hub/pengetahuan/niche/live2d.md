# Niche: Model Live2D (VTuber 2D)

Dibaca kalau brand membuat model VTuber 2D dengan Live2D Cubism: menggambar art model (PSD berlapis), rigging, atau keduanya, beserta tambahan seperti ekspresi, outfit, dan animasi. Untuk aset stream lain (emote, eye banner, panel) lihat niche/ilustrasi-anime.md. Untuk avatar 3D (VRM, VRoid) lihat niche/vtuber-3d.md. Data per November 2026. Harga dan aturan lisensi cek ulang sebelum dipakai.

## Cara kerja niche ini

Model Live2D dibuat dalam dua tahap yang sering dikerjakan orang berbeda:

| Tahap | Siapa | Hasil |
|---|---|---|
| Art model | Artist (illustrator) | File PSD dengan setiap bagian di lapisan sendiri (mata, alis, mulut, rambut depan, rambut belakang, badan, aksesori) |
| Rigging | Rigger | Model yang bisa bergerak, diekspor sebagai file .moc3, .model3.json, tekstur, ekspresi, dan file fisika |

Klien bisa memesan art saja, rigging saja, atau keduanya. Studio yang bisa keduanya punya nilai jual lebih, karena klien tidak perlu mengatur dua orang.

## Siapa pembelinya

| Jenis | Yang dicari | Ketakutan utama |
|---|---|---|
| VTuber baru | Paket lengkap art dan rig, siap debut | Model kaku, harga di luar anggaran, artist menghilang |
| VTuber yang sudah jalan | Outfit baru, ekspresi, toggle, rig ulang | Gaya baru tidak cocok dengan model lama |
| Klien yang sudah punya art | Rigging saja | PSD ditolak karena lapisannya belum siap |
| Klien yang sudah punya rigger | Art model saja | Lapisan tidak sesuai kebutuhan rigger |
| Agensi VTuber | Beberapa model dengan gaya seragam | Kontrak, kerahasiaan, jadwal |

## Di mana mereka mencari

- **VGen**, tempat utama komisi Live2D.
- **X**, lewat postingan showcase model dan "commissions open".
- **Halaman Carrd atau Google Docs** berisi harga, antrean, dan ToS. Banyak artist memasang tabel slot per bulan.
- **Fiverr**, dengan kata kunci seperti live2d rigging, vtuber model, vtube studio, rigging only.
- **nizima**, marketplace model Live2D milik Live2D Inc., untuk model jadi dan pre-made.
- **Booth dan Ko-fi**, untuk model pre-made dan aset.

## Produk dan cara menyusunnya

### Ukuran model

Harga biasanya dibagi menurut potongan: **chibi**, **half body atau thigh up**, dan **full body**. Masing-masing dihargai terpisah untuk art, rig, dan art plus rig.

### Art model (PSD siap rig)

Ini titik yang paling sering bermasalah. PSD harus:
- Satu elemen per lapisan, dengan nama lapisan yang jelas.
- Bagian yang tertutup tetap digambar (misalnya rambut di balik kepala, bagian mata di balik kelopak), supaya tidak bolong saat bergerak.
- Bersih tanpa piksel nyasar, tanpa lapisan kosong, tanpa latar.
- Resolusi cukup besar.

Banyak rigger memasang biaya tambahan untuk merapikan atau memisahkan lapisan kalau PSD dari klien belum siap. Tulis syarat PSD dengan jelas di halaman harga studio.

### Rigging

Yang biasanya masuk paket dasar: kedip mata, gerak mata, gerak mulut, gerak kepala dan badan di tiga sumbu (X, Y, Z), fisika rambut dan pakaian, dan beberapa ekspresi.

Yang membedakan tingkat rigging:
- Jumlah bentuk mulut dan kehalusan gerak kepala.
- Dukungan iPhone atau VBridger untuk tracking wajah yang lebih detail (misalnya lidah, pipi menggembung).
- Gerak badan yang lebih kompleks dan animasi diam (idle).

Format yang dikirim untuk VTube Studio: .moc3, .model3.json, tekstur, file fisika, ekspresi, dan kadang file pengaturan VTube Studio. File sumber Cubism (.cmo3) sering dijual terpisah dengan harga tambahan, karena dengan file ini orang lain bisa mengubah rig.

### Tambahan yang umum

Ekspresi (senang, marah, menangis, mata berbinar), toggle aksesori, gaya rambut lain, outfit lain, toggle tangan, hewan peliharaan atau maskot kecil yang ikut bergerak, sayap atau ekor, animasi idle, dan model ASMR.

### Produk lain

- **Model pre-made atau adoptable**, model jadi yang dijual sekali ke satu pembeli.
- **YCH model**, desain dasar yang diubah sesuai karakter pembeli.
- **Ilustrasi beranimasi**, ilustrasi biasa yang dibuat bergerak dengan Live2D untuk video atau layar tunggu.
- **Mini model atau model khusus**, misalnya model kecil dengan rig sederhana, lebih murah dan cepat.

## Harga pasar

Gambaran kasar dari halaman harga artist dan rigger 2026, sangat bergantung pada gaya dan reputasi:

| Produk | Rentang yang terlihat |
|---|---|
| Chibi art plus rig | Sekitar $300, bisa lebih |
| Half body art plus rig | Sekitar $800 sampai $1.050 |
| Full body art plus rig | Sekitar $1.000 sampai $1.600, studio besar bisa lebih |
| Rigging saja full body | Dari sekitar $545 sampai $1.500 |
| Art saja full body | Sekitar $350 sampai $700 |
| Ekspresi sederhana | Sekitar $10 sampai $60 per ekspresi |
| Outfit tambahan | Sering dihitung 50 persen dari harga dasar |
| File sumber .cmo3 | Sekitar $100 sampai 100 persen dari harga komisi |

Antrean Live2D panjang. Banyak artist menulis slot per bulan dan waktu kerja beberapa minggu. DP 50 persen di awal juga umum. Ikuti otak-marketing.md bagian Harga, dan pakai standar studio kalau sudah ada.

## Lisensi software Live2D

- **Live2D Cubism** punya versi FREE dan PRO. Untuk perorangan atau usaha kecil dengan penjualan tahun terakhir di bawah 10 juta yen, versi FREE atau PRO for indie boleh dipakai untuk komersial. Kalau penjualan seluruh usaha 10 juta yen atau lebih, wajib PRO for business. Ini dihitung dari penjualan seluruh usaha, bukan hanya bagian yang memakai Live2D.
- Model buatan studio boleh dijual ke pihak lain, termasuk di nizima.
- Kalau model dipakai di aplikasi atau game yang memakai Cubism SDK, ada kontrak terpisah dengan Live2D Inc. Video yang diekspor dari Cubism Editor tidak perlu kontrak.
- Cek ulang batas penjualan dan jenis lisensi di help.live2d.com sebelum memberi saran ke studio.

## Hak pakai model

Tulis dengan jelas di ToS:
- Apakah klien boleh streaming dan monetisasi dengan model (hampir selalu ya).
- Apakah klien boleh menjual ulang model atau menyerahkannya ke orang lain.
- Apakah klien menerima file .cmo3 dan PSD, dan apakah boleh mengubahnya atau memberikannya ke rigger lain.
- Apakah studio boleh memajang model, membuat video showcase, dan menunggu sampai klien debut dulu.
- Kerahasiaan desain sebelum debut.

## Ide penawaran

- **Paket debut lengkap:** art, rig, beberapa ekspresi, dan aset pendukung seperti eye banner dan emote dengan gaya sama.
- **Paket rig saja dengan cek PSD:** klien mengirim PSD, studio memeriksa dulu dan memberi penawaran harga merapikan lapisan.
- **Upgrade berkala:** outfit baru untuk ulang tahun channel atau musim tertentu, ditawarkan ke klien lama.
- **Pre-made atau YCH:** mengisi slot kosong dan menarik pembeli dengan anggaran kecil.
- **Model mini:** produk pintu masuk yang cepat.

## Ide konten

| Konten | Format | Peran |
|---|---|---|
| Showcase model bergerak dengan tracking wajah | Video pendek | Ditemukan |
| Sebelum dan sesudah rigging (PSD diam lalu bergerak) | Video atau carousel | Percaya |
| Isi PSD berlapis yang dibuka satu per satu | Video pendek | Percaya dan edukasi |
| Uji fisika rambut dan ekspresi | Video pendek | Bukti kualitas |
| Model klien saat debut, kalau diizinkan | Repost | Bukti |
| Tabel slot bulanan | Postingan disematkan | Order |

Hashtag yang umum: #Live2D, #VTuber, #Live2DCommission, #VtuberModel, #ENVtuber, #VTuberUprising. Cek dulu bahwa hashtag masih aktif.

## Diagnosa khusus niche ini

- **Banyak yang bertanya, sedikit yang jadi order:** harga total tidak jelas karena art dan rig dipisah. Buat tabel art, rig, dan gabungan.
- **Order rigging sering tertunda:** PSD klien belum siap. Tulis syarat PSD dan tawarkan jasa merapikan lapisan.
- **Klien lama tidak kembali:** tawarkan outfit, ekspresi, atau aset tambahan setelah debut.
- **Showcase sepi:** video terlalu panjang atau tidak menunjukkan gerak terbaik di detik pertama. Lihat konten-dan-hook.md.

## Aturan dan batasan

- VGen tidak mengizinkan AI generatif. Pastikan pernyataan tanpa AI memang benar.
- Jangan memakai model sampel atau base orang lain tanpa izin. Model contoh bawaan aplikasi sering hanya boleh dipakai non-komersial.
- Model berdasarkan karakter milik pihak lain hanya untuk pemakaian pribadi kecuali ada izin.
- NSFW mengikuti kebijakan studio dan platform.

## Sumber

- Halaman harga artist dan rigger Live2D di Carrd dan Google Docs (2026).
- Gig Fiverr untuk Live2D art dan rigging (2026).
- Syarat PSD dari halaman komisi rigger (2026).
- Pusat bantuan Live2D tentang lisensi Cubism Editor dan SDK.
