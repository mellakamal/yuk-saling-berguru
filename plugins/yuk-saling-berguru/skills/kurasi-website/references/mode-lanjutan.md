# Mode Lanjutan

Empat pemeriksaan tambahan. Kapan masing-masing jalan diatur di SKILL.md bagian 2.

## A. Klien internasional
Jalankan kalau web punya teks bahasa Inggris, harga dalam USD, link Fiverr/Upwork/VGen/Ko-fi, atau pengguna menyebut target luar negeri.

- Versi bahasa Inggris lengkap, bukan hanya beranda; bahasa Inggrisnya natural (tidak terasa hasil terjemahan mesin).
- Harga dalam USD (atau mata uang target) dan jelas apakah sudah termasuk biaya platform/PayPal.
- Metode bayar internasional: PayPal, Wise, Stripe, Ko-fi, VGen; disebutkan siapa yang menanggung biaya transfer.
- Zona waktu dan perkiraan waktu balas disebut (misalnya "GMT+7, replies within 24 hours").
- Kontak yang dipakai orang luar: email atau Discord, bukan hanya WhatsApp.
- Kalau ada profil Fiverr/Upwork: harga, paket, dan portofolio di web selaras dengan profil itu, dan ada link dua arah.
- Kalau ada dua bahasa, ada tombol ganti bahasa yang jelas dan atribut `lang`/`hreflang` benar.

## B. Angka teknis terukur
Jalankan kalau bahan berupa link live atau kode.

- **PageSpeed**: buka `https://pagespeed.web.dev/analysis?url=<URL>` di browser dan tunggu hasil, atau pakai WebFetch ke `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<URL>&strategy=mobile`. Catat skor Performance, Accessibility, Best Practices, SEO untuk HP, plus LCP, CLS, dan INP/TBT. Kalau dua cara gagal, tulis di Batas pemeriksaan.
- **Kontras warna**: ambil warna teks dan latar dari CSS atau lewat `getComputedStyle` di browser, lalu hitung dengan `scripts/kontras.py`:
  `python3 scripts/kontras.py "#777777" "#ffffff"`
  Batas lolos: 4,5:1 untuk teks biasa, 3:1 untuk teks besar (24px ke atas, atau 18,7px tebal) dan ikon/tombol.
- **Berat halaman**: dari request jaringan, catat total ukuran halaman dan tiga file terberat.

Tulis angka-angka ini sebagai Fakta di tabel perbaikan, lengkap dengan angkanya.

## C. Tracking dan legal
Jalankan kalau bahan berupa link live atau kode.

Cek kode sumber halaman (view source atau baca file) untuk:
- Google Analytics / Google Tag Manager (`gtag(`, `googletagmanager.com`), Meta Pixel (`fbq(`), TikTok Pixel.
- Verifikasi Google Search Console (`google-site-verification`), sitemap yang bisa didaftarkan.
- Kebijakan privasi kalau web mengumpulkan data (form, tracking, newsletter).
- Pernyataan hak cipta karya dan larangan pemakaian untuk pelatihan AI kalau relevan untuk artist.
- Syarat refund dan pembatalan yang terlihat sebelum pembeli membayar.

Tracking yang tidak ada bukan otomatis masalah. Jadikan Penting hanya kalau web dipakai untuk iklan atau pengguna ingin mengukur hasil.

## D. Bandingkan dengan pesaing
Jalankan hanya kalau pengguna meminta, menulis "kurasi lengkap", atau menyebut pesaing. Mode ini butuh pencarian dan waktu lebih lama.

- Pakai pesaing yang disebut pengguna. Kalau tidak ada, cari dua atau tiga web artist/studio dengan niche dan pasar yang sama lewat pencarian web. Sebutkan link sumbernya.
- Bandingkan per area dengan skor rubrik yang sama, dalam satu tabel:

| Area | Web ini | Pesaing A | Pesaing B | Yang bisa ditiru |
|---|---|---|---|---|

- Fokus ke pola yang bisa ditiru (struktur harga, cara menampilkan proses, CTA), bukan menyalin desain atau teks.
