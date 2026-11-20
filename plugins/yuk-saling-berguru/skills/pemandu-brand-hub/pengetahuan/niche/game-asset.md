# Niche: Game asset (2D dan 3D)

Dibaca kalau brand membuat aset untuk game: karakter, props, lingkungan, tileset, sprite pixel art, UI, ikon, atau paket aset yang dijual di marketplace. Untuk avatar VTuber lihat niche/vtuber-3d.md atau niche/live2d.md. Untuk miniatur cetak D&D lihat niche/maskot-dan-figur.md dan niche/dnd.md. Data per November 2026. Bagi hasil marketplace dan aturan AI cek ulang sebelum dipakai.

## Dua jalur penghasilan

| Jalur | Cara kerja | Cocok untuk |
|---|---|---|
| Jasa custom | Developer memesan aset sesuai gaya game mereka | Studio yang ingin pendapatan per proyek dan relasi jangka panjang |
| Paket aset di marketplace | Studio membuat paket sekali, dijual berkali-kali | Studio yang punya waktu luang di antara order dan gaya yang konsisten |

Banyak studio menjalankan keduanya. Paket aset juga berfungsi sebagai portofolio yang bisa ditemukan developer.

## Siapa pembelinya

| Jenis | Yang dicari | Ketakutan utama |
|---|---|---|
| Developer indie (sendiri atau tim kecil) | Karakter, sprite sheet, tileset, props dengan harga terjangkau | Gaya tidak seragam, file tidak bisa langsung dipakai |
| Studio game kecil dan menengah | Artist lepas untuk menambah kapasitas, sering kontrak berulang | Kualitas naik turun, tenggat meleset, kerahasiaan |
| Peserta game jam | Paket aset murah atau gratis | Lisensi tidak jelas |
| Kreator Roblox, Minecraft, atau mod | Aset sesuai batas teknis platform tersebut | Aset tidak lolos aturan platform |
| Pembuat aplikasi edukasi | Karakter dan ikon dengan gaya ramah anak | Gaya tidak cocok untuk anak |

## Di mana mereka mencari

- **Fiverr dan Upwork**, untuk jasa custom. Di Upwork juga banyak kontrak jangka panjang dengan studio. Kata kunci: game ready, pixel art, sprite sheet, tileset, low poly, stylized, Unity, Unreal, Godot.
- **Fab (Epic)**, gabungan Unreal Engine Marketplace, Sketchfab Store, ArtStation Marketplace, dan Quixel. Mendukung berbagai engine.
- **Unity Asset Store**, khusus pengguna Unity.
- **itch.io**, untuk paket aset indie, terutama pixel art dan 2D.
- **CGTrader**, untuk model 3D umum.
- **ArtStation dan X**, sebagai etalase dan tempat studio mencari artist. Developer sering memakai hashtag seperti #gamedev, #indiedev, dan #pixelart.

## Bagi hasil marketplace

Gambaran per 2026, cek ulang sebelum menyarankan:

| Marketplace | Bagian untuk penjual | Catatan |
|---|---|---|
| Fab | Sekitar 88 persen | Punya lisensi Personal dan Professional |
| Unity Asset Store | Sekitar 70 persen | Satu jenis lisensi (EULA Unity) |
| CGTrader | Sekitar 55 sampai 80 persen | Bertingkat sesuai penjualan setahun terakhir |
| itch.io | Penjual menentukan sendiri | Bebas, tapi pembeli harus menemukan sendiri |

Persentase bukan satu-satunya pertimbangan. Jumlah pembeli dan seberapa mudah aset ditemukan juga penting.

## Produk 2D

### Pixel art

- **Ukuran umum:** 16x16, 32x32, 48x48, 64x64, 128x128 piksel, atau sesuai permintaan.
- **Sprite sheet animasi:** idle, jalan, lari, lompat, serang, terluka, mati. Bisa 4 atau 8 arah untuk game tampak atas.
- **Tileset** untuk lantai, dinding, dan lingkungan.
- **Format kirim:** PNG transparan sprite sheet, frame satuan, GIF pratinjau, dan file sumber Aseprite atau PSD.
- Harga biasanya dihitung per karakter dan per animasi (jumlah frame).

### Ilustrasi dan aset 2D lain

Karakter dan concept art, potret karakter untuk dialog, ikon item dan skill, UI (tombol, panel, HUD), latar belakang, kartu, dan aset untuk visual novel.

## Produk 3D

### Syarat game ready

Model yang bagus di render belum tentu siap dipakai di game. Syarat yang umum diminta:

- **Topologi bersih**, umumnya quad, dan siap ditekuk kalau karakter akan dianimasikan.
- **Polycount sesuai peran.** Patokan kasar 2026: props lingkungan sekitar 500 sampai 5.000 segitiga, props utama atau senjata yang dipegang sekitar 5.000 sampai 20.000 segitiga. Tanyakan batas dari klien dan platform target (PC, konsol, mobile, VR).
- **UV rapi**, tidak tumpang tindih kecuali sengaja, dengan kepadatan tekstur yang konsisten.
- **Tekstur PBR**, misalnya base color, normal, roughness, metallic, dengan resolusi 1K, 2K, atau 4K.
- **LOD** (versi model dengan detail lebih rendah untuk jarak jauh) kalau diminta.
- **Skala benar dan transform sudah diterapkan**, supaya langsung pas saat diimpor.
- **Format kirim:** FBX, GLB, atau OBJ, kadang paket Unity atau Unreal. Tulis apakah file sumber (BLEND, ZTL, SPP) ikut.
- **Rig dan animasi** untuk karakter, kalau masuk paket.

### Jenis produk 3D

Karakter (stylized, low poly, atau realistis), props, senjata, kendaraan, kit lingkungan modular, aset Roblox atau UEFN, dan karakter VRChat.

## Harga pasar

Rentang harga game asset sangat lebar dan bergantung pada gaya, detail, jumlah animasi, dan apakah klien perorangan atau studio. Patokan yang bisa dipakai:
- Pixel art dihitung per sprite dan per frame animasi. Karakter dengan animasi lengkap jauh lebih mahal dari sprite diam.
- Model 3D dihitung per aset dan menurut kompleksitas. Karakter dengan rig lebih mahal dari props.
- Freelancer menengah yang menerima tarif per jam sering berada di kisaran sekitar $40 sampai $80 per jam menurut panduan harga studio 2026. Anggap ini patokan kasar.
- Paket aset di marketplace biasanya murah per paket. Unity Asset Store mensyaratkan harga minimal sekitar $4,99 untuk aset berbayar.

Untuk proyek studio, tawarkan harga per batch atau kontrak bulanan, bukan hanya per aset. Ikuti otak-marketing.md bagian Harga, dan pakai standar studio.

## Hak pakai dan lisensi

Tulis dengan jelas:
- **Hak komersial.** Aset game hampir selalu dipakai untuk produk komersial, jadi pastikan lisensinya jelas.
- **Eksklusif atau tidak.** Aset custom biasanya eksklusif untuk klien. Aset dari paket marketplace tidak eksklusif.
- **Hak cipta pindah atau hanya lisensi.** Studio game sering meminta hak cipta penuh. Kalau begitu, harganya lebih tinggi.
- **Hak portofolio.** Banyak studio game meminta NDA sampai game rilis. Tawarkan sebagai pilihan dan tulis kapan studio boleh memajang karya.
- **Kredit di game.** Bisa ditawarkan sebagai pilihan, tidak wajib.
- **Larangan penjualan ulang.** Klien tidak boleh menjual aset sebagai paket aset sendiri.

## Aturan AI

Marketplace dan klien makin ketat soal AI. CGTrader memperketat kebijakan AI pada 2026, dan banyak gig serta artist menulis tanpa AI di ToS. Tulis dengan jujur di setiap listing apakah ada alat AI yang dipakai, dan ikuti aturan pengungkapan di masing-masing marketplace.

## Yang ditakutkan pembeli dan cara menjawabnya

| Ketakutan | Cara menjawabnya |
|---|---|
| Gaya tidak cocok dengan game | Minta tangkapan layar game, buat satu aset uji dulu |
| File tidak langsung jalan di engine | Tulis engine yang sudah diuji dan sertakan video atau gambar di dalam engine |
| Polycount atau ukuran tekstur terlalu besar | Tulis angka polycount dan resolusi tekstur di setiap pengiriman |
| Artist hilang di tengah proyek | Jadwal per milestone dan update rutin |
| Lisensi tidak jelas | Tulis lisensi di paket dan di invoice |

## Ide penawaran

- **Aset uji berbayar:** satu aset kecil dengan harga terjangkau supaya developer bisa mencoba kecocokan gaya sebelum proyek besar.
- **Paket karakter lengkap:** desain, sprite atau model, animasi dasar, dan potret dialog.
- **Paket aset tematik di marketplace:** misalnya kit desa fantasi atau paket monster pixel art. Sekaligus menjadi portofolio.
- **Kontrak bulanan untuk studio:** jumlah aset tetap per bulan dengan harga per aset lebih rendah.
- **Konversi gaya:** mengubah aset placeholder klien menjadi aset final dengan gaya seragam.

## Ide konten

| Konten | Format | Peran |
|---|---|---|
| Animasi sprite berulang (loop) | GIF atau video pendek | Ditemukan |
| Aset di dalam engine dengan pencahayaan game | Video pendek | Bukti teknis |
| Wireframe dan tekstur terpisah | Carousel | Percaya, terutama untuk klien studio |
| Proses dari concept ke model ke engine | Video pendek atau carousel | Percaya |
| Paket aset baru di marketplace | Postingan dengan tautan | Order |
| Ikut tantangan komunitas seperti #PixelArt atau game jam | Postingan | Ditemukan |

Hashtag yang umum: #gamedev, #indiedev, #pixelart, #gameart, #lowpoly, #madewithunity, #UnrealEngine, #Godot, #screenshotsaturday. Cek dulu bahwa hashtag masih aktif.

## Diagnosa khusus niche ini

- **Portofolio dilihat, tapi developer tidak menghubungi:** portofolio belum menunjukkan aset di dalam game atau engine. Tambahkan contoh yang sedang dipakai dan data teknis.
- **Paket aset di marketplace tidak laku:** judul dan gambar sampul belum menjawab apa isinya. Tulis jumlah aset, ukuran, engine, dan gaya di judul dan gambar pertama.
- **Sering ditawar rendah:** pembeli yang datang kebanyakan pemula. Tawarkan aset uji berbayar dan arahkan ke paket bertingkat.
- **Proyek studio tidak berlanjut:** gaya tidak konsisten antar batch. Buat panduan gaya internal untuk setiap klien.

## Sumber

- Gig Fiverr dan Upwork untuk pixel art dan aset 3D game ready (2026).
- Perbandingan Unity Asset Store, Fab, CGTrader, dan itch.io (2026).
- Dokumentasi Fab dari Epic Games.
- Ceklis aset game ready dan patokan polycount (2026).
- Panduan harga karakter 2D game (2026).
