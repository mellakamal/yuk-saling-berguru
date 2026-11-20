# Langkah 5. Perbaiki web

Tujuannya membereskan temuan audit di web dan memasang karya hasil kurasi. Web adalah "warung sendiri", tempat semua kanal lain bermuara.

## Kalau belum punya web

Kerjakan dalam dua tahap (detailnya di pengetahuan/web.md):
1. **Web pertama di Carrd.** Satu halaman berisi karya, harga, ToS singkat, dan tombol order. Paket gratis cukup untuk mulai. Kalau artist datang dari jalur cepat web, tahap ini mungkin sudah aktif.
2. **Web sendiri lewat Claude Code**, ditawarkan setelah Langkah 7 selesai. Anggap artist bukan programmer. Siapkan dokumen Bahan Web dari Brand Hub, lalu serahkan pembangunannya ke skill bangun-website-code (di dalam Claude Code) atau bangun-website (di chat tanpa akses folder). Claude Code yang membangun dan memasang web, artist cukup menyetujui dan mengecek tampilan. Pilihan hosting dan domain dibahas di pengetahuan/web.md bagian Memilih hosting dan domain.

Setelah web pertama aktif, ganti link di semua bio ke halaman ini.

## Kenali dulu web-nya dibuat pakai apa

Kalau brand sudah punya web, tanyakan: web kamu dibuat pakai apa? Pilihannya:
- Dibuat dengan Claude Code (ada folder proyeknya di komputer)
- Pembuat web seperti Carrd, Wix, Framer, Notion Sites, atau sejenisnya
- Belum tahu atau dibuatkan orang lain

Cara memandu berbeda untuk tiap pilihan:
- **Claude Code**: minta artist membuka folder web-nya di Claude Code, dan kalau skill bangun-website-code terpasang, pakai skill itu untuk melanjutkan. Cek dulu apakah README.md, CLAUDE.md, dan BLUEPRINT.md sudah ada (lihat pengetahuan/web.md). Kalau belum, prompt pertama adalah membuat ketiganya dari kode yang ada. Setelah itu salin daftar perbaikan dari Tasks ke sana sebagai satu prompt, ditutup dengan pengingat memperbarui ketiga file. Tulis prompt itu untuk artist, lengkap dengan konteks dari Profil Brand, dan minta Claude Code menjelaskan setiap langkah dengan bahasa sederhana.
- **Pembuat web**: pandu lewat menu pembuat web itu, satu perubahan sekali jalan. Kalau kamu tidak yakin letak menunya, minta screenshot layar artist.
- **Belum tahu**: minta link web dan screenshot halaman admin-nya, lalu tentukan bersama. Kalau web lama sulit diurus, tawarkan pindah ke Carrd atau web sendiri lewat Claude Code.

## Halaman yang harus ada

| Halaman | Isi minimal |
|---|---|
| Beranda atau Portofolio | 9 sampai 12 karya Tampil dari Bank Karya, urutan sesuai Langkah 4 |
| Price sheet | Tiap layanan dengan harga mulai, apa yang didapat, dan contoh karyanya |
| Terms of Service (ToS) | Cara bayar, jumlah revisi, lama pengerjaan, hak pakai, kebijakan refund, apa yang tidak dikerjakan |
| FAQ | 5 sampai 8 pertanyaan yang paling sering ditanyakan pembeli |
| Kontak dan order | Form order (dibangun di Langkah 7), email akun, link sosial media |

Semua teks di web memakai Bahasa publik di Profil Brand. Kamu boleh membuatkan draf ToS, FAQ, dan teks price sheet dari Profil Brand. Tunjukkan drafnya dan minta artist mengecek angka dan aturannya, karena itu janji ke pembeli.

## SEO dasar di web

Supaya web bisa ditemukan di Google, pastikan hal ini ada. Detailnya di pengetahuan/web.md bagian SEO dasar.
- Tiap halaman punya judul dan deskripsi sendiri, ditulis dari kata yang diketik calon klien.
- Satu judul utama per halaman, dan teks alternatif di tiap gambar karya.
- Gambar pratinjau muncul saat link dibagikan.
- Untuk web sendiri: sitemap terkirim ke Google Search Console, dan beranda sudah diminta diindeks.
- Beri tahu artist bahwa halaman baru butuh hari sampai minggu untuk terindeks, dan peringkat tidak bisa dijanjikan.

Daftar ke Search Console dikerjakan artist sendiri dengan akun Google-nya. Kamu memandu klik demi klik.

## Pandu pelan

1. Ambil baris Tasks hasil audit yang berhubungan dengan web (nomor 5.x).
2. Kerjakan satu temuan sekali jalan. Setelah artist bilang beres, minta ia membuka web di HP dan memastikan tampilannya oke.
3. Ubah Status baris itu jadi Selesai, lalu lanjut ke temuan berikutnya.

## Kalau modelnya produk

Halaman yang dibutuhkan berbeda:

| Halaman | Isi minimal |
|---|---|
| Beranda atau Portofolio | Karya dan produk pilihan dari Bank Karya |
| Shop atau Katalog | Daftar produk dengan link ke toko (Etsy, Ko-fi Shop, Gumroad, atau lainnya) |
| FAQ | Pengiriman, lisensi file digital, refund, cara pakai produk |
| Kebijakan toko | Lisensi pemakaian, refund, pengiriman |
| Kontak | Email akun dan link sosial media |

Price sheet dan ToS komisi tidak perlu kalau brand tidak menerima komisi. Kalau web belum ada sama sekali, Langkah 5 dikerjakan sebagai membangun web dari awal. Mulai dari Carrd dengan halaman Shop berisi tombol ke toko, lalu tawarkan web sendiri lewat Claude Code.

## Kalau modelnya gig marketplace

Web tetap memakai lima halaman di atas. Price sheet untuk pembeli dari luar boleh mengikuti paket gig. Ingatkan artist: link web hanya dibagikan di kanal di luar platform gig, tidak di profil atau pesan Fiverr atau Upwork.

## Selesai kalau

Semua temuan prioritas tinggi untuk web sudah Selesai, kelima halaman di atas ada, dan tiap halaman punya judul serta deskripsi sendiri. Untuk brand yang mulai dari halaman satu lembar, langkah ini selesai saat halaman itu aktif dengan karya, harga, ToS, dan tombol order, dan link-nya sudah terpasang di bio. Ubah Status Langkah 5 jadi Selesai.
