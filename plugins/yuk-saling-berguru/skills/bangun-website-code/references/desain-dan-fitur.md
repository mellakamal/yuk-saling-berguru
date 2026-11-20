# Desain dan fitur yang tidak terasa template

Dipakai saat membuat desain kasar di chat dan saat membangun di Claude Code. Ukurannya sederhana: kalau logo dan nama ditutup, orang tetap bisa menebak niche dan gaya artist ini dari webnya.

## Arah desain
Sebelum membuat apa pun, tentukan arah desain dalam tiga baris dan tulis di blueprint bagian 6:
1. Kesan dalam tiga kata yang diambil dari karya, misalnya "hangat, kartun, bersih".
2. Warna: dua sampai tiga warna diambil dari karya terbaik (warna pakaian karakter, latar, coretan khas), satu warna netral untuk teks, dan satu warna aksen khusus untuk tombol utama.
3. Elemen khas: satu hal yang hanya cocok untuk artist ini, dipilih dari karakter studio (lihat Memilih fitur unggulan di bawah).

## Aturan tampilan
1. Karya adalah bintangnya. Gambar besar, ruang kosong lega, teks pendek. Yang pertama terlihat adalah karya terbaik, bukan banner berisi kalimat.
2. Huruf: satu huruf judul yang berkarakter dan sesuai kesan, satu huruf isi yang mudah dibaca. Ambil dari Google Fonts lewat link, tanpa instalasi. Jangan memakai Inter, Roboto, Poppins, atau Montserrat sebagai huruf judul karena terlalu umum. Hindari juga pilihan pertama yang sering muncul di web buatan AI, misalnya Playfair Display, Fraunces, Space Grotesk, DM Sans, dan DM Serif Display, kecuali artist sendiri yang memintanya. Cari dari karakter karya: telusuri beberapa kategori Google Fonts, tawarkan tiga pasangan yang berbeda karakter, lalu artist memilih. Catat pilihannya di blueprint bagian 6.
3. Tata letak boleh tidak simetris: ukuran karya berbeda-beda, satu karya selebar layar, teks di samping gambar. Jangan membuat setiap bagian berupa deretan tiga kartu.
4. Hindari ciri template: kartu bulat berbayang yang berderet, chip, label kecil huruf kapital di atas setiap judul, tiga kotak harga dengan "Most popular", gradasi ungu dan biru, kotak penutup bergradasi, panah di setiap tombol, ikon umum di setiap poin, dan emoji sebagai hiasan.
5. Hiasan diambil dari dunia artist: coretan, tekstur kertas, garis sketsa, piksel, atau motif dari karakternya. Bukan bentuk abstrak umum.
6. Gerak secukupnya: muncul halus saat digulir, efek saat kursor di atas karya, video pendek diputar berulang tanpa suara. Tidak ada animasi yang memperlambat atau membuat pusing, dan pengaturan kurangi gerak di perangkat pengunjung dihormati.
7. Teks ditulis seperti artist bicara ke kliennya, bukan kalimat pemasaran umum seperti "Bringing your vision to life".
8. Harga boleh berupa tabel polos dan FAQ berupa daftar tanya jawab. Angka berurutan hanya untuk isi yang memang berurutan, seperti langkah order.
9. Cek di lebar HP dulu, lalu laptop. Pengunjung dari media sosial kebanyakan memakai HP.
10. Kode tidak membawa jejak dari web lain. Nama class, nama variabel warna, nama file CSS dan skrip, serta susunan folder aset disusun untuk proyek ini, tidak disalin dari proyek lain dan tidak selalu sama di setiap web (misalnya tidak selalu `css/style.css` dan `assets/`), karena alamat file itu terlihat di sumber halaman. Hapus komentar bawaan, teks contoh, dan tag generator dari kode yang tayang. Jangan memakai ulang kode, gambar latar, ikon, atau file CSS dari web brand lain yang pernah dibantu.

## Fitur
Setiap web punya fitur dasar, lalu satu sampai dua fitur unggulan yang dipilih dari karakter studio. Semua fitur di bawah dibuat dengan HTML, CSS, dan JavaScript biasa tanpa instalasi, jadi tetap jalan di web statis.

### Fitur dasar
Fitur dasar adalah fungsi yang perlu ada, bukan bentuk yang harus sama di semua web. Bentuk, letak, dan cara kerjanya dipilih sesuai gaya brand. Contohnya, status slot bisa berupa baris kecil di atas, kalimat di halaman order, atau penanda di tiap layanan. Langkah order bisa berupa daftar, gambar alur, atau cerita singkat. FAQ bisa buka tutup atau daftar biasa. Tombol yang menempel di HP dipakai hanya kalau cocok dengan desainnya. Kode setiap fitur ditulis untuk proyek itu, tidak disalin dari web lain.

| Fitur | Keterangan |
|---|---|
| Galeri dengan filter dan tampilan besar | Karya dikelompokkan per jenis (misalnya full body, chibi, model 3D), diklik untuk dilihat besar, dan bisa digeser di HP. Setiap karya tetap tag `img` di HTML dengan alt dan keterangan, bukan gambar latar CSS atau gambar yang baru dimuat JavaScript, supaya terbaca Google Images |
| Status slot komisi | Tanda Open, Closed, atau sisa slot di bagian atas. Diubah lewat satu baris di satu file, dan caranya ditulis di README.md |
| Langkah order | Tiga sampai lima langkah dari memilih paket sampai karya dikirim |
| Tombol order tetap terlihat di HP | Tombol utama menempel di bawah layar HP |
| FAQ buka tutup | Pertanyaan diklik untuk menampilkan jawaban |
| Dua bahasa | Hanya kalau pasarnya campuran. Ada tombol ganti bahasa EN dan ID |

### Memilih fitur unggulan
Fitur unggulan dipilih dari karakter studio, tidak hanya dari niche-nya. Kalau semua studio di satu niche memakai fitur yang sama, web mereka akan terlihat seragam.
1. Lihat tiga hal: gaya karya (misalnya tekstur cat air, garis tebal, warna neon), cerita studio (asal ide, cara mulai, nilai yang dipegang), dan cara kerja (misalnya selalu mulai dari sketsa di kertas, atau klien ikut memilih warna). Pakai juga jawaban pertanyaan pembeda dari Pemetaan atau Tahap 1.
2. Tawarkan dua sampai tiga pilihan fitur unggulan dengan untung ruginya. Minimal satu pilihan berasal dari luar tabel di bawah, dirancang khusus dari karakter studio itu.
3. Artist yang memilih. Catat pilihannya beserta alasannya di blueprint bagian 5.

Tabel di bawah hanya sumber ide, bukan daftar wajib.

### Contoh fitur unggulan per niche

| Niche | Contoh fitur unggulan |
|---|---|
| VTuber 3D | Model 3D bisa diputar langsung di halaman (model-viewer dengan file .glb), atau geser antara tampilan berwarna dan wireframe |
| Live2D | Video demo gerak yang diputar berulang, perbandingan sebelum dan sesudah rigging |
| Ilustrasi karakter | Geser dari sketsa ke hasil jadi, tampilan proses per tahap |
| Maskot dan figur | Satu maskot dalam beberapa ekspresi atau pose yang bisa diklik bergantian |
| Game asset | Sprite yang bergerak, contoh aset dipasang di potongan layar game |
| Buku anak | Halaman buku yang bisa dibalik, contoh dua halaman berdampingan |
| TTRPG dan peta | Peta yang bisa diperbesar dan digeser |
| Semua niche | Kalkulator perkiraan harga: pilih jenis, jumlah karakter, dan latar, lalu muncul harga mulai |

### Aturan fitur
1. Angka di kalkulator hanya dari daftar harga artist, diberi tulisan "perkiraan", dan diakhiri tombol order.
2. Fitur yang perlu menyimpan data (akun pembeli, pembayaran, panel admin) mengikuti tingkat web di `pilihan-teknologi.md` dan dibahas dulu dengan artist.
3. Di desain kasar, fitur unggulan dibuat sudah bisa dicoba kalau memungkinkan, supaya artist merasakan bedanya.
4. Dua fitur yang rapi lebih baik daripada lima fitur yang setengah jadi.
5. Di Claude Code, desain yang sudah disetujui tidak boleh disederhanakan jadi tampilan umum. Kalau ada bagian yang sulit dibuat, jelaskan ke artist dan tawarkan pengganti yang tetap khas.
