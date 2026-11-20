# Tahap B. Siapkan ruang kerja brand

Tujuannya menyiapkan tempat menyimpan semua hasil panduan. Artist memilih tempat kerja, mengerjakan satu daftar sekali duduk, lalu kamu yang membangun ruang kerjanya di akun milik brand.

Tahap ini dikerjakan setelah Langkah 1, supaya artist sudah melihat hasil (draf Profil Brand) sebelum diminta menyiapkan apa pun.

## 1. Jelaskan dulu wujudnya

Istilah "Brand Hub" belum dikenal artist. Sebelum meminta apa pun, jelaskan dengan bahasa sehari-hari, misalnya:

> Bayangkan ruang kerja brand seperti meja kantor kecil untuk brandmu. Di atasnya ada satu map berisi profil brand, papan tugas, rak karya, kalender posting, daftar harga, dan buku order. Bedanya, meja ini ada di Google Drive, jadi kamu, admin, dan tim bisa membukanya dari HP atau laptop masing-masing.
>
> Wujudnya satu folder bernama Brand Hub:
> - Profil Brand (dokumen): pegangan suara, layanan, positioning, dan bio.
> - Sheet Brand Hub dengan beberapa tab: Beranda (ringkasan progres), Tasks (daftar tugas panduan), Bank Karya, Kalender Konten, Order, Daftar Harga, dan Rekap Mingguan.
> - Folder Karya dan Proses.
> - Nanti menyusul: Form Order dan dokumen teks siap tempel untuk admin.
>
> Kamu tidak perlu membuatnya sendiri. Setelah akun brand terhubung, Claude yang membangun semuanya. Tugasmu cukup membuka foldernya dan mengecek isinya.
>
> Siapa memakai apa:
> - Pemilik: membuka Beranda untuk memantau progres dan order.
> - Admin: mencatat order dan membalas klien sesuai Profil Brand.
> - Tim: mengisi Bank Karya dan melihat jadwal di Kalender Konten.

## 2. Pilih tempat kerja

Tanyakan dengan dua pilihan:

> Ruang kerja brand kamu mau disimpan di mana?
> 1. **Google (disarankan).** Isinya folder Drive, Google Doc, dan Google Sheet. Bisa disambung ke Google Calendar untuk pengingat jadwal posting dan ke Gmail untuk draf balasan order.
> 2. **Notion.** Tampilannya lebih cantik, ada galeri dan papan, tapi perlu daftar akun Notion dan belajar sedikit cara pakainya.

Kalau artist ragu, sarankan Google. Setelah dipilih, baca file panduannya dan pakai hanya file itu sampai panduan selesai:

| Pilihan | File |
|---|---|
| Google | tempat-kerja/google.md |
| Notion | tempat-kerja/notion.md |

## 3. Daftar sekali duduk

Kirim satu daftar sekaligus, jangan dipecah per pertanyaan. Lewati butir yang sudah dimiliki artist (cek dari jawaban Pemetaan).

**Kalau memilih Google**, kirim teks ini dengan penyesuaian seperlunya:

> Supaya progres kamu tersimpan, kerjakan ini sekali duduk, kira-kira 15 menit.
>
> **Sebelum mulai, baca ini dulu.**
> - Kelima connector nanti harus tersambung ke satu akun Google yang sama, yaitu akun brand. Jangan dicampur dengan akun pribadi atau akun brand lain, supaya file dan email tidak tercecer di beberapa akun.
> - Akun Claude boleh berbeda dengan akun brand. Kamu bisa tetap login Claude dengan email pribadi atau email tim. Yang penting, saat menyambungkan connector, kamu masuk dengan akun Google brand.
> - Siapa pun yang menyambungkan akun brand ke Claude miliknya bisa meminta Claude membuka Drive dan Gmail brand. Jadi sambungkan hanya di akun Claude milik pemilik brand atau orang yang dipercaya.
>
> **1. Akun Google brand.** Kalau belum ada, buat satu akun Gmail khusus dengan nama brand. Jangan pakai email pribadi. Akun ini juga dipakai untuk mendaftar kanal lain nanti.
>
> **2. Amankan akunnya.** Di myaccount.google.com, buka Keamanan, nyalakan Verifikasi 2 Langkah, lalu isi email dan nomor HP pemulihan. Akun ini kunci semua data brand kamu.
>
> **3. Sambungkan ke Claude.**
> 1. Di Claude, buka menu **Customize**, lalu pilih **Connectors**.
> 2. Klik **Google Drive**, lalu **Connect**.
> 3. Saat jendela masuk Google muncul, baca alamat emailnya sebelum klik. Kalau yang muncul akun pribadi, pilih "Gunakan akun lain" lalu masuk dengan akun brand. Cara paling aman adalah membuka Claude di profil browser yang hanya memakai akun brand.
> 4. Google akan menampilkan halaman "Pilih fungsi yang dapat diakses oleh Claude". Cek lagi email di sisi kiri, centang **Pilih semua**, gulir ke bawah, lalu klik **Lanjutkan**. Kalau kotaknya tidak dicentang, connector tersambung tapi Claude tidak bisa membuat file atau jadwal. Izin ini tidak membuat Claude bertindak sendiri, Claude hanya bekerja saat kamu memintanya.
> 5. Ulangi untuk **Google Docs**, **Google Sheets**, **Google Calendar**, dan **Gmail**. Halaman izin muncul untuk setiap connector, jadi lakukan hal yang sama lima kali.
>
> Kalau ternyata ada connector yang tersambung ke akun lain: buka Customize, lalu Connectors, klik connector itu, pilih **Disconnect**, lalu sambungkan ulang dengan akun brand.
>
> Kalau kamu memakai Claude dari akun tim atau perusahaan dan connector Google tidak muncul, minta pengelola akun tim menyalakannya dulu.
>
> **4. Nyalakan di chat.** Di chat baru, klik tanda + di kotak pesan, buka Connectors, lalu pastikan kelima connector Google tadi menyala.
>
> Kalau sudah semua, ketik "lanjut panduan" di chat baru itu. Kalau ada yang macet, bilang nomor berapa.

**Kalau memilih Notion**, contohnya:

> 1. **Email akun brand.** Kalau belum ada, buat satu email khusus dengan nama brand.
> 2. **Daftar Notion.** Buka notion.com, klik Get Notion free, masukkan email akun brand, lalu masukkan kode yang dikirim ke email. Pilih For myself kalau ditanya.
> 3. **Sambungkan Notion ke Claude.** Di Claude, buka Customize, pilih Connectors, cari Notion, klik Connect, lalu klik Allow. Pastikan yang masuk adalah akun Notion brand.
> 4. **Folder Drive.** Buat satu folder Google Drive dengan nama brand untuk menyimpan karya dan file proses.

Password dan kode verifikasi diisi pemilik akun atau orang yang ia percaya, dan password tetap dipegang pemilik. Kamu tidak perlu tahu isinya.

Setelah connector disambungkan, artist biasanya perlu membuka chat baru, dan chat baru tidak membawa hasil Pemetaan dan Langkah 1. Jadi sebelum artist pergi, berikan satu blok "Catatan untuk dilanjutkan" berisi tempat kerja yang dipilih, ringkasan Pemetaan, urutan langkah yang dimajukan kalau ada, dan draf Profil Brand yang sudah disetujui. Minta artist menempelkan blok itu di chat baru bersama kalimat "lanjut panduan".

## 4. Bangun ruang kerjanya

1. Tanyakan nama brand kalau belum jelas. Itu jadi nama folder Brand Hub.
2. Cek dulu apakah Brand Hub sudah ada. Kalau ada, pakai yang itu.
3. Bangun sesuai file tempat kerja yang dipilih, berurutan seperti tertulis di sana.
4. Kalau ada bagian yang gagal dibuat, coba sekali lagi. Kalau masih gagal, beri tahu artist bagian mana dan pandu ia membuatnya sendiri.
5. **Cek akun.** Kirim link folder Brand Hub dan minta artist membukanya dengan akun brand. Kalau folder itu ada di Drive akun brand, berarti connector tersambung ke akun yang benar. Kalau tidak ada, berarti ada connector yang tersambung ke akun lain. Pandu memperbaikinya dengan Disconnect lalu sambung ulang.

## 5. Pindahkan hasil sebelumnya

1. Tulis draf Profil Brand dari Langkah 1 ke Profil Brand.
2. Tulis hasil Pemetaan: model bisnis di bagian Layanan, kanal dan catatan aturan platform di bagian Kanal dan link, lalu isi Kondisi tiap langkah di Tasks.
3. Kalau Pemetaan memajukan beberapa langkah, pindahkan baris langkah itu di tab Tasks ke urutan baru, tepat di bawah baris Tahap B. Beranda membaca langkah berikutnya dari urutan baris, jadi urutan baris harus sama dengan urutan kerja.
4. Ubah Status Langkah 1 jadi Selesai. Di Google, baris Tahap A dan Tahap B juga diubah jadi Selesai (di Notion, kedua tahap ini tidak punya baris). Langkah yang Kondisi-nya Tidak relevan juga langsung Selesai.

## Selesai kalau

Ruang kerja brand ada di akun brand, artist sudah membukanya sendiri, Profil Brand terisi, dan Kondisi di Tasks terisi semua. Tawarkan masuk ke langkah berikutnya sesuai urutan dari Pemetaan.
