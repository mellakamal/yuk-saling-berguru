# Tampil Profesional

Daftar hal yang membuat web terlihat amatir kalau terlewat. Claude Code membereskannya sendiri tanpa menunggu artist meminta, karena artist biasanya tidak tahu hal ini perlu dicek. Yang ditanyakan ke artist hanya keputusan brand (warna, teks, logo) dan pembelian domain.

Sebagian butir dicek otomatis oleh `references/cek-seo.py`. Jalankan pada folder yang tayang: `python3 -I <folder skill>/references/cek-seo.py site`.

## a. Alamat tanpa .html
**Cek:** semua link antarhalaman ditulis tanpa `.html` (misalnya `/nama-halaman`), dan link ke beranda ditulis `/`. `cek-seo.py` melaporkan link yang masih berakhiran `.html`. Buka satu alamat lama yang berakhiran `.html` di web yang tayang, pastikan dialihkan ke alamat tanpa `.html`.

**Benerin:**
- Ganti semua link di menu, tombol, footer, sitemap, dan canonical ke alamat tanpa `.html`. Nama file tetap `nama-halaman.html`.
- Pratinjau di laptop memakai `python3 -I <folder skill>/references/pratinjau.py site`, lalu buka alamat yang muncul, supaya link tanpa `.html` bekerja seperti setelah tayang. Kalau Python tidak ada dan Node terpasang, pakai `npx serve site`. Kalau keduanya tidak ada, file bisa dibuka langsung, tapi sampaikan ke artist bahwa pindah halaman lewat menu baru berfungsi setelah tayang.
- **Apache atau LiteSpeed** (Rumahweb, shared hosting Hostinger, VPS dengan Apache): buat `.htaccess` di folder yang tayang.

```
RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
RewriteCond %{THE_REQUEST} \s/+(.*/)?index\.html[\s?] [NC]
RewriteRule ^ /%1 [R=301,L]
RewriteCond %{THE_REQUEST} \s/+(.+?)\.html[\s?] [NC]
RewriteRule ^ /%1 [R=301,L]
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+?)/?$ $1.html [L]
ErrorDocument 404 /404.html
```

  Kalau web berada di belakang proxy Cloudflare, atur SSL Cloudflare ke Full atau Full (strict) supaya aturan HTTPS tidak berputar.
- **Nginx** (VPS): di blok server untuk port 443.

```
rewrite ^/index(\.html)?$ / permanent;
if ($request_uri ~ ^/(.+)\.html(\?.*)?$) { return 301 /$1$is_args$args; }
location / { try_files $uri $uri.html $uri/ =404; }
error_page 404 /404.html;
```

  Pengalihan dari `http` ke `https` diatur di blok server port 80. Jalankan `nginx -t` sebelum reload.
- **Cloudflare:** cukup link yang benar. Cloudflare sudah membuka `/nama-halaman` dari `nama-halaman.html` dan mengalihkan alamat lama berakhiran `.html`. Cek sekali setelah tayang.

## b. Tidak ada kode yang tampil sebagai teks
**Cek:** buka setiap halaman dan baca seperti pengunjung. Cari tag yang tidak tertutup, `&nbsp;` atau `&amp;` yang tampil mentah, komentar HTML yang terlihat di layar, dan sisa teks penanda seperti "Lorem ipsum" atau "TODO". `cek-seo.py` menangkap entitas yang ter-escape dua kali.

**Benerin:** tutup tag yang terbuka, tulis entitas sekali saja, hapus komentar dan penanda dari halaman.

## c. Judul halaman unik
**Cek:** setiap halaman punya `<title>` yang berbeda, bukan "Document", "Untitled", "Home", atau nama file. `cek-seo.py` melaporkan judul bawaan dan judul kembar.

**Benerin:** pola judulnya nama halaman lalu nama brand, misalnya "Daftar Harga Komisi | Kebun Kertas". Nama halaman memuat kata kunci halaman itu sesuai `seo.md`. Pemisahnya (garis tegak, tanda hubung, atau titik tengah) dipilih sekali untuk web ini dan sama di semua halamannya. Jangan selalu memakai pemisah yang sama di setiap web yang dibantu.

## d. Favicon dan gambar pratinjau link
**Cek:** ada favicon di tab browser, dan link yang dibagikan di WhatsApp atau media sosial menampilkan gambar, judul, dan deskripsi.

**Benerin:**
- Favicon dibuat dari logo atau potongan karya artist, bukan ikon umum. Sediakan ukuran kecil untuk tab dan ukuran besar untuk layar HP.
- Gambar Open Graph 1200 x 630 dari karya terbaik, dengan `og:title`, `og:description`, dan `og:image` di setiap halaman. Pakai JPG atau PNG untuk gambar ini, karena sebagian aplikasi chat belum menampilkan WebP sebagai pratinjau.

## e. Menu, header, dan footer sama di semua halaman
**Cek:** kalau web lebih dari 3 halaman, isi `<header>`, `<nav>`, dan `<footer>` sama persis di semua halaman. `cek-seo.py` membandingkannya. Penanda halaman aktif ditulis dengan `aria-current="page"`, dan itu tidak dihitung sebagai beda.

**Benerin:** simpan menu, header, dan footer di satu file sumber di luar folder yang tayang. Setiap kali ada perubahan, Claude Code menyalinnya ke semua halaman, lalu menjalankan `cek-seo.py`. Kalau proyek sudah memakai alat build seperti Astro, pakai komponen bersama dari alat itu. Jangan memuat menu atau footer lewat JavaScript, karena Google dan pengunjung yang JavaScript-nya mati tidak akan melihatnya.

## f. Domain sendiri
**Cek:** web yang dianggap selesai terbuka lewat domain milik artist. Alamat sementara seperti `pages.dev`, `netlify.app`, atau IP server hanya untuk pratinjau.

**Benerin:** di Tahap 7 web boleh tayang di alamat sementara untuk dicek, tapi web baru dianggap selesai setelah domain terpasang di Tahap 8. Setelah domain aktif, alihkan alamat sementara ke domain dan perbarui sitemap, canonical, dan gambar pratinjau. Kalau artist belum membeli domain, tulis "belum ada domain" di `README.md` dan di ringkasan akhir.

## g. Email dengan nama domain
**Cek:** email di halaman kontak memakai nama domain (misalnya hello@namabrand.com) kalau hosting menyediakannya.

**Benerin:** kalau hosting menyediakan kotak email, pandu artist membuatnya dan pasang di halaman kontak. Kalau hosting hanya menyediakan penerusan email (seperti Cloudflare), pasang alamat domain yang diteruskan ke email artist. Kalau belum ada sama sekali, tulis "email domain: belum ada" di `README.md` dan pakai email brand yang sudah ada.

## h. Tidak terasa seperti template AI
**Cek:** tidak ada emoji sebagai hiasan, tidak ada gradasi ungu dan biru bawaan, dan warna serta huruf berasal dari karya artist. Bandingkan dengan aturan tampilan di `desain-dan-fitur.md`.

**Benerin:** ikuti `desain-dan-fitur.md`. Perubahan warna, huruf, dan teks adalah keputusan brand, jadi tunjukkan dulu ke artist sebelum diterapkan.

## i. Rapi di HP dan laptop
**Cek:** buka di lebar 390px dan 1440px. Tidak ada teks atau gambar yang terpotong, halaman tidak bisa digeser ke samping, dan tombol cukup besar untuk jari (tinggi sekitar 44px) dengan jarak yang cukup.

**Benerin:** perbaiki CSS sampai lolos di kedua lebar, lalu cek lagi di lebar tablet sekitar 768px.

## j. Gambar ringan dan tidak membuat tata letak loncat
**Cek:** setiap gambar di bawah 300 KB, karya memakai format WebP, dan setiap tag `img` punya `width` dan `height`. `cek-seo.py` melaporkan gambar yang terlalu besar dan tag `img` tanpa ukuran.

**Benerin:** perkecil gambar ke ukuran tampil, ubah ke WebP, dan isi `width` dan `height` sesuai ukuran aslinya. File resolusi penuh tetap di `bahan/` atau Drive artist, tidak ikut tayang. Gambar pratinjau link di butir d boleh tetap JPG atau PNG asal di bawah 300 KB.
