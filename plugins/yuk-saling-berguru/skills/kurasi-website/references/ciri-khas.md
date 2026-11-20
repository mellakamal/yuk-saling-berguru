# Cek Ciri Khas Brand

Dipakai saat pengguna meminta "cek ciri khas brand", atau saat web, akun, dan jalur order brand dibuat sebelum panduan di plugin ini meminta semua nama dan teks disusun dari suara brand. Tujuannya memastikan tidak ada bagian yang masih terdengar seperti template, sama dengan contoh panduan, atau kembar dengan brand lain.

Cek ini melengkapi kurasi biasa. Kalau dijalankan bersama 11 area, tulis hasilnya sebagai bagian terpisah di akhir.

## Patokan

Sebelum menilai, baca bahan yang menggambarkan brand: Profil Brand atau dokumen Bahan Web kalau ada (terutama Suara, Positioning, dan Pembeda), `BLUEPRINT.md`, `CLAUDE.md`, dan caption atau balasan yang ditulis artist sendiri. Kalau jawaban pertanyaan pembeda belum tercatat, tanyakan satu kali: "Apa yang membuat studiomu berbeda dari studio lain di niche yang sama?"

Setiap temuan dibandingkan dengan dua hal: apakah teks atau nama itu sama dengan contoh di skill plugin ini, dan apakah ia bisa dipakai brand mana pun tanpa diubah. Kalau ya, tandai untuk diganti.

## Yang diperiksa

| Area | Yang dicari | Perbaikan |
|---|---|---|
| Teks web | Judul halaman, hook di beranda, ajakan, ToS, FAQ, dan teks tombol yang terdengar umum atau sama dengan contoh panduan | Tulis ulang dari kata-kata, aturan, dan cerita studio. ToS dan FAQ mengikuti cara kerja dan pertanyaan klien studio itu |
| Alamat halaman | Nama file dan nama menu yang sama dengan pola umum semua web | Ganti dengan alamat dari kata kunci brand. Wajib pasang pengalihan dari alamat lama supaya link dan Google tidak rusak, lalu perbarui sitemap, canonical, dan link antarhalaman |
| Tampilan | Huruf yang termasuk pilihan pertama yang sering dipakai web buatan AI, susunan beranda yang sama dengan pola umum, fitur dasar dengan bentuk dan letak yang sama | Ikuti `desain-dan-fitur.md` di skill bangun-website-code. Tawarkan pilihan, artist yang memutuskan |
| Kode | Komentar bawaan, teks contoh, tag generator, nama class atau file yang dibawa dari proyek lain, susunan folder aset yang terlihat di alamat file (misalnya selalu `css/style.css` dan `assets/`), dan isi `robots.txt` yang disalin apa adanya | Bersihkan dari folder yang tayang. Kalau nama folder aset diganti, perbarui semua link di halaman |
| File gambar | Data tersembunyi: lokasi, kamera, nama pembuat, nama software | Hapus datanya, ukuran dan tampilan gambar tidak berubah |
| File yang ikut tayang | `BLUEPRINT.md`, `CLAUDE.md`, `README.md`, `desain-kasar.html`, atau folder bahan yang bisa dibuka dari alamat web | Pastikan hanya folder `site/` yang tayang |
| Hosting | Nama proyek dengan pola umum, alamat sementara yang masih tayang di samping domain, repo web yang publik | Ganti atau alihkan sesuai `hosting.md`. Perubahan di akun hosting dan GitHub menunggu persetujuan artist |
| Discord | Nama channel, nama role, teks peringatan, dan pesan bot tiket yang memakai nama atau kalimat baku | Usulkan dua versi nama dari kata-kata brand. Teks peringatan disusun dari isi wajibnya |
| Form order | Judul form, kata-kata pertanyaan, dan pesan terima kasih yang baku | Susun ulang dari suara brand. Sesuaikan dengan bentuk alur order yang dipilih |
| Akun media sosial | Bio, postingan sematan, nama Highlight, dan judul daftar akun resmi yang memakai kalimat umum | Tulis ulang dengan suara brand |
| Pesan | Pesan sambutan WhatsApp, pengumuman pindah akun, pesan ke klien lama, dan pesan penutup order yang memakai template | Susun ulang dari daftar isi wajibnya di panduan Brand Hub |

## Cara menyampaikan hasil

1. Tunjukkan satu tabel: area, temuan, usulan, dan siapa yang mengerjakan (Claude Code atau artist).
2. Bagian web dikerjakan Claude Code setelah artist setuju, dalam satu paket kerja.
3. Bagian di luar web (Discord, form, akun, pesan) disiapkan Claude sebagai teks siap tempel. Artist yang memasangnya sendiri.
4. Sarankan perubahan di luar web dikerjakan bertahap dalam satu sampai dua minggu, tidak semuanya di hari yang sama.
5. Catatan perubahan, pesan commit, dan isi file pegangan ditulis singkat dan netral, misalnya "teks dan tampilan disesuaikan dengan suara brand". Jangan menyebut nama kelas, nama plugin, atau brand lain di file proyek.
6. Setelah selesai, isi baris "Pembeda" di blueprint bagian 1 dan baris "Alamat halaman" di bagian 3 sesuai hasil cek. Kalau cek dijalankan dari Brand Hub, isi bagian Pembeda di Profil Brand. Baris dan bagian ini juga menandakan cek sudah dijalankan, jadi tawaran cek tidak muncul lagi.
