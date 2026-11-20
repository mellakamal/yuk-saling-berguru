# Tempat kerja Notion

Dipakai kalau artist memilih Notion di Tahap B, untuk membangun Brand Hub di Notion artist. Bangun berurutan dari atas. Semua nama halaman, kolom, dan pilihan ditulis persis seperti di bawah, karena langkah-langkah lain membacanya dengan nama itu.

## 1. Halaman utama

Judul: nama akun artist. Ikon: 🎨. Isi:

```
Ini tempat kerja untuk satu akun branding. Claude memandu pengisiannya langkah demi langkah. Ketik "lanjut panduan" di Claude untuk melanjutkan.

## Cara pakai

1. Simpan halaman ini untuk kamu sendiri. Jangan taruh di teamspace yang bisa dibuka orang lain.
2. Kerjakan Tasks urut dari nomor kecil. Claude akan memberi tahu langkah mana yang sedang dikerjakan.
3. Masukkan karya ke Bank Karya dan centang ceklisnya. Karya yang lolos lalu ditarik ke Kalender Konten.
4. Isi Rekap Mingguan tiap akhir minggu.

## Cara isi ceklis di Bank Karya

- Butir 3 (Izin klien) dicentang juga kalau karyanya bukan komisi.
- Butir 8 (Keterangan fan art) dicentang juga kalau karyanya bukan fan art.
- Kolom Boleh tampil baru berisi Ya kalau butir 1, 3, dan 4 tercentang. Kalau isinya Tidak, karya itu jangan diberi keputusan Tampil.
- Skor itu jumlah kriteria yang sudah terpenuhi, dari total 10.

## Aturan dasar

- Satu karya bisa dipakai di semua kanal. Ada versi jadi, potongan WIP, dan video prosesnya.
- Reply, DM, dan komentar ditulis kamu atau admin yang kamu tunjuk, dan kamu tetap memantau.
- Jangan bahas tuduhan atau komunitas lama. Posting karya dan prosesnya saja.
- Halaman ini hanya dibagikan ke admin dan tim yang dipercaya.
```

## 2. Halaman Profil Brand (anak halaman utama)

Ikon: 🧭. Isi:

```
Bagian yang nanti tampil di publik ditulis dalam Bahasa publik brand.

## Ringkasan akun
## Artist di balik akun
## Pembeda
Apa yang membuat studio ini berbeda dari studio lain di niche yang sama, dengan kata-kata artist sendiri.
## Layanan
Model bisnis: (Komisi, Gig marketplace, Produk, atau campuran). Model utama:
| Layanan atau produk | Kisaran harga | Catatan |
## Audiens

Baris pertama: Bahasa publik (Inggris, Indonesia, atau dua bahasa).
## Gaya visual
## Suara
- Kata atau ungkapan yang sering dipakai:
- Kata yang dihindari:
- Panjang kalimat:
- Pemakaian emoji:
- Contoh caption asli tulisanmu sendiri (2 sampai 3):
## Pilar konten
| Pilar | Contoh isi | Porsi |
## Batasan
- Topik yang tidak dibahas:
- Tidak membahas tuduhan atau komunitas lama
## Kanal dan link
| Kanal | Alamat | Status |
Baris: Web atau halaman satu lembar, X, Instagram, TikTok, YouTube, Bluesky (opsional), Discord, WhatsApp Business (kalau ada klien lokal), Portofolio (ArtStation atau Behance, dan folder Drive kalau ada), Platform order atau toko
## Catatan aturan platform
```

## 3. Database (semua anak halaman utama, tidak inline)

### Projects
| Kolom | Tipe |
|---|---|
| Nama | Title |
| Status | Status: Belum (to do), Jalan (in progress), Selesai (complete). Bawaan Belum |
| Mulai | Date |
| Target | Date |
| Catatan | Text |

### Tasks
| Kolom | Tipe |
|---|---|
| Task | Title |
| No | Number |
| Status | Status: Belum (to do), Jalan (in progress), Selesai (complete). Bawaan Belum |
| Kondisi | Select: Sudah ada (green), Perlu dirapikan (yellow), Perlu dibangun (blue), Tidak relevan (gray) |
| Alat | Select: Claude, Claude Code, Notion, Scheduler, Calendar, Manual |
| Project | Relation dua arah ke Projects, nama di sisi Projects: Tasks |
| Due | Date |
| PIC | Person |
| Selesai kalau | Text |

### Bank Karya
| Kolom | Tipe |
|---|---|
| Karya | Title |
| Gambar | Files |
| Layanan | Select: Ilustrasi, Karakter, 3D, Animasi, Lainnya (sesuaikan dengan layanan atau jenis produk di Profil Brand) |
| Keputusan | Select: Tampil (green), Cadangan (yellow), Tidak (gray) |
| Tahun | Number |
| Folder proses | URL |
| 1 Dikerjakan sendiri, 2 File proses ada, 3 Izin klien, 4 Tanpa AI generatif, 5 Kualitas terbaik, 6 Mewakili layanan, 7 Gaya sejalan, 8 Keterangan fan art, 9 Tanpa data klien, 10 File rapi | Checkbox, satu kolom per butir |
| Skor | Formula, jumlah kotak yang tercentang: `toNumber(prop("1 Dikerjakan sendiri")) + toNumber(prop("2 File proses ada")) + ... + toNumber(prop("10 File rapi"))` |
| Boleh tampil | Formula: `if(prop("1 Dikerjakan sendiri") and prop("3 Izin klien") and prop("4 Tanpa AI generatif"), "Ya", "Tidak")` |
| Catatan | Text |

### Kalender Konten
| Kolom | Tipe |
|---|---|
| Judul | Title |
| Tanggal tayang | Date |
| Kanal | Multi-select: X, Instagram, TikTok, YouTube Shorts, Bluesky, Portofolio |
| Format | Select: Karya jadi, WIP, Proses, Info slot |
| Status | Status: Ide (to do), Draf, Ditulis ulang, Terjadwal (in progress), Tayang (complete). Bawaan Ide |
| Karya | Relation dua arah ke Bank Karya, nama di sisi Bank Karya: Konten |
| Caption (EN) | Text |
| Link tayang | URL |
| Catatan | Text |

### Rekap Mingguan
| Kolom | Tipe |
|---|---|
| Minggu | Title |
| Periode | Date |
| Konten tayang | Relation satu arah ke Kalender Konten |
| Pengikut baru, Inquiry masuk, Order masuk | Number |
| Yang berhasil, Yang kurang, Diubah minggu depan | Text |

## 4. View

- Tasks: view tabel bawaan, ditambah view Papan (board) dikelompokkan per Status dan diurutkan menurut No.
- Kalender Konten: view kalender memakai Tanggal tayang.
- Bank Karya: view galeri dengan Gambar sebagai sampul.

## 5. Isi awal Projects

1. Fondasi akun
2. Perbaikan web dan kanal
3. Peluncuran bertahap
4. Evaluasi siklus pertama

## 6. Isi awal Tasks

| No | Task | Alat | Project | Selesai kalau |
|---|---|---|---|---|
| 1 | Tentukan brand voice | Claude | Fondasi akun | Halaman Profil Brand terisi lengkap |
| 2 | Audit fondasi | Claude | Fondasi akun | Ada daftar kekurangan dengan prioritas |
| 3 | Kumpulkan stok karya | Manual | Fondasi akun | Semua karya kandidat ada di Bank Karya dengan link folder prosesnya |
| 4 | Kurasi karya | Claude | Fondasi akun | 9 sampai 12 karya berkeputusan Tampil |
| 5 | Perbaiki web | Claude | Perbaikan web dan kanal | Semua temuan prioritas tinggi untuk web beres dan halaman wajib ada |
| 6 | Samakan bio semua kanal | Manual | Perbaikan web dan kanal | Semua bio jujur, seragam, dan link-nya benar |
| 7 | Siapkan dua jalur order | Manual | Perbaikan web dan kanal | Dua jalur order aktif dan sudah diuji |
| 8 | Buat akun yang belum ada | Manual | Perbaikan web dan kanal | Semua kanal wajib ada, username sama, dan bio terpasang |
| 9 | Bangun server Discord | Manual | Perbaikan web dan kanal | Server, channel, aturan, role, dan sistem tiket siap, link terpasang di web |
| 10 | Posting karya bertahap | Scheduler | Peluncuran bertahap | Unggahan karya 2 minggu ke depan ada di Kalender Konten |
| 11 | Kalender konten 2 minggu | Notion | Peluncuran bertahap | Dua minggu ke depan terisi di Kalender Konten |
| 12 | Jalankan 2 minggu | Manual | Peluncuran bertahap | Semua jadwal 2 minggu sudah Tayang atau dibatalkan |
| 13 | Evaluasi | Claude | Evaluasi siklus pertama | Rekap Mingguan dua minggu pertama terisi dan ada daftar perubahan untuk siklus berikutnya |

## Catatan teknis

- Untuk membaca isi Tasks dan database lain, pakai mode view (query lewat URL view). Query SQL hanya bisa di Notion paket Business, sedangkan sebagian besar artist memakai paket gratis.
- Kalau formula atau view tidak bisa dibuat lewat connector, lanjutkan saja, lalu catat bagian itu dan pandu artist membuatnya sendiri lewat tampilan Notion.

## Membaca dan menulis progres

- **Membaca posisi**: buka database Tasks lewat view-nya (mode view), lalu baca kolom No, Status, dan Kondisi.
- **Mengubah Status atau Kondisi**: ubah properti halaman baris langkah itu.
- **Menambah baris** di Bank Karya, Kalender Konten, atau Rekap Mingguan: buat halaman baru di database itu.
- **Profil Brand**: ubah bagian yang dimaksud saja, jangan menulis ulang seluruh halaman.
- **Temuan audit** (Langkah 2): tambahkan sebagai baris baru di Tasks dengan No desimal seperti 5.1 dan 5.2.
- Selalu ambil skema terbaru sebelum menulis, karena artist bisa saja menambah atau mengganti kolom.
- Form order (Langkah 7) dibuat di Google Forms atau Tally. Jawabannya masuk ke email atau Google Sheet milik artist, lalu ringkasan order dicatat di Catatan Projects atau database baru kalau artist mau. Untuk order VGen, catat juga status Bukti proses (Lengkap, Sebagian, Belum) dan pastikan Lengkap sebelum order ditandai selesai.
- Google Calendar tidak tersambung dengan Notion. Untuk pengingat jadwal, artist bisa memakai Notion Calendar atau aplikasi penjadwal.
- Daftar Harga dan dokumen teks siap tempel (Langkah 7): buat sebagai dua anak halaman utama. Daftar Harga berupa tabel dengan kolom yang sama seperti di tempat-kerja/google.md bagian Tab Daftar Harga.
