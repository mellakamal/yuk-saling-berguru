# Checklist Kurasi Website

Pakai pertanyaan ini sebagai alat bantu, bukan formulir. Tidak semua pertanyaan perlu dijawab di hasil; yang masuk hasil hanya temuan yang perlu diperbaiki atau kekuatan yang perlu dipertahankan.

## 1. Kesan pertama (hero)
- Dalam 5 detik, apakah pengunjung tahu: ini siapa, menawarkan apa, untuk siapa?
- Ada satu CTA utama yang jelas di layar pertama, tanpa scroll, di desktop dan HP?
- Gambar atau karya di hero adalah yang terbaik, bukan sekadar dekorasi?

## 2. Pesan brand dan positioning
- Headline spesifik (contoh: "Ilustrasi maskot untuk brand kuliner") atau generik ("Kreatif dan profesional")?
- Pembeda dari pesaing terlihat?
- Nada bahasa konsisten di semua halaman?

## 3. Kurasi karya / portofolio
- Jumlah karya cukup tapi tidak berlebihan (9 sampai 12 karya terbaik untuk web, mengikuti kriteria kurasi karya Brand Hub)?
- Karya terkuat diletakkan paling atas atau paling awal?
- Ada karya lama atau lemah yang menurunkan kesan keseluruhan?
- Kategori jelas (misalnya per jenis layanan) dan sesuai dengan yang dijual?
- Tiap karya punya konteks singkat (klien, kebutuhan, hasil)?
- Gaya visual konsisten, atau terlihat seperti karya beberapa orang berbeda tanpa penjelasan?

## 4. Jalur order dan CTA
- Berapa klik dari beranda sampai bisa order atau menghubungi? Idealnya maksimal dua.
- Teks tombol jelas ("Pesan Ilustrasi", "Chat via WhatsApp") atau samar ("Submit", "Klik di sini")?
- Alur order dijelaskan (langkah, DP, revisi, waktu pengerjaan)?
- Form tidak meminta data yang tidak perlu? Link WhatsApp/email benar-benar berfungsi dan berisi pesan pembuka?
- CTA muncul lagi di tengah dan akhir halaman panjang?

## 5. Harga dan penawaran
- Harga atau kisaran harga ditampilkan, atau ada alasan jelas kenapa tidak?
- Paket mudah dibandingkan (tabel atau kartu sejajar)?
- Yang didapat di tiap paket jelas (jumlah revisi, format file, hak pakai komersial)?
- Format angka: Rp 1.500.000, bukan 1,5jt atau IDR1500000.

## 6. Copywriting dan bahasa
- Ada typo, campuran bahasa yang tidak sengaja, atau kalimat terlalu panjang?
- Tulisan terdengar seperti AI (pembuka klise, kata "tak hanya ... tetapi juga", deretan tiga kata sifat, kalimat berbunga)?
- Ada kata "kalian" atau nada menggurui?
- Fokus ke manfaat untuk pembeli, bukan hanya cerita tentang diri sendiri?

## 7. Desain visual dan konsistensi brand
- Palet warna konsisten (umumnya 1 warna utama, 1 aksen, netral)?
- Maksimal dua jenis font? Ukuran teks body cukup terbaca (minimal 16px)?
- Kontras teks dengan latar cukup? (Cek teks abu-abu tipis di atas putih atau teks di atas foto.)
- Spasi antar-section rapi dan seragam? Ada elemen yang menempel atau terlalu renggang?
- Logo dan elemen brand sama dengan yang dipakai di media sosial?

## 8. Tampilan HP
- Cek di lebar sekitar 390px.
- Ada teks atau gambar yang terpotong, keluar layar, atau membuat halaman bisa digeser ke samping?
- Tombol cukup besar untuk jari (minimal sekitar 44px tinggi) dan tidak terlalu berdempetan?
- Menu bisa dibuka dan ditutup? Menu atau banner menutupi CTA?
- Galeri karya nyaman di-scroll, gambar tidak terlalu kecil?

## 9. Kecepatan dan teknis
- Ukuran gambar besar (di atas sekitar 300 KB untuk gambar umum, atau di atas sekitar 500 KB untuk gambar utama dan karya unggulan)? Sudah format WebP/AVIF? Setiap gambar punya `width` dan `height`?
- Alamat halaman tanpa `.html` (`/nama-halaman`, beranda `/`), dan alamat lama berakhiran `.html` dialihkan ke alamat tanpa `.html`?
- Ada kode yang tampil sebagai teks: tag tidak tertutup, `&nbsp;` atau `&amp;` mentah, komentar HTML, atau teks penanda seperti "Lorem ipsum"?
- Ada file gagal dimuat (404), link mati, atau error di console?
- Favicon ada? HTTPS aktif?
- Ada video atau embed berat yang dimuat otomatis di atas halaman?

## 10. SEO dasar
- Tiap halaman punya `<title>` unik berisi nama halaman lalu nama brand, bukan "Document", "Untitled", atau nama file? Meta description menjelaskan layanan + lokasi kalau relevan?
- Satu `<h1>` per halaman, struktur heading berurutan?
- Gambar punya atribut alt yang deskriptif?
- Ada Open Graph (judul, deskripsi, gambar) supaya pratinjau rapi saat dibagikan di WhatsApp dan media sosial?
- Ada sitemap.xml dan robots.txt?
- URL bersih? Cek alamat semua halaman utama, link menu, canonical, og:url, dan isi sitemap. Alamat dianggap bersih kalau:
  - Tanpa akhiran `.html` dan tanpa `index.html` (`/portofolio`, bukan `/portofolio.html` atau `/portofolio/index.html`).
  - Tanpa tanda pagar untuk pindah halaman (`/#/harga`). Tanda pagar hanya boleh untuk loncat ke bagian di web satu halaman (`/#harga`).
  - Tanpa parameter (`?id=3`, `?page=harga`, `?utm_source=...`, `?fbclid=...`) di link menu, canonical, og:url, dan sitemap.
  - Huruf kecil semua, kata dipisah tanda hubung, tanpa spasi (`%20`), garis bawah, atau angka acak (`/harga-commission`, bukan `/Harga_Commission` atau `/page-2`).
  - Satu versi alamat saja: https, pilih pakai www atau tanpa www, dan garis miring di akhir dibuat konsisten. Versi lain dialihkan (301) ke versi itu, bukan tampil sebagai halaman kembar.
  - Link di bio, QR, dan kartu nama langsung ke domain, bukan lewat pemendek link yang menampilkan halaman perantara atau iklan sebelum web terbuka.
  - Penilaian: web pakai domain sendiri, bukan `namaakun.github.io/nama-repo`, `nama.vercel.app`, atau `nama.netlify.app`.

## 11. Kepercayaan dan kontak
- Ada testimoni, logo klien, atau jumlah proyek yang bisa dibuktikan?
- Kontak mudah ditemukan dari halaman mana pun?
- Web terbuka lewat domain sendiri, bukan alamat sementara (`pages.dev`, `netlify.app`, atau IP server)?
- Email di halaman kontak memakai nama domain kalau hosting menyediakannya, bukan email gratisan yang terlihat dibuat seadanya?
- Ada syarat dan ketentuan order (revisi, refund, hak cipta)?
- Link media sosial aktif dan akunnya masih diperbarui?
- Ada foto atau cerita singkat tentang orang di balik studio?
