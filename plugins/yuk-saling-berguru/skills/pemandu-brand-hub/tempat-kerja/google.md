# Tempat kerja Google

Dipakai kalau artist memilih Google di Tahap B. Brand Hub terdiri dari satu folder Drive, satu Google Doc, dan satu Google Sheet. Semua nama tab, kolom, dan pilihan ditulis persis seperti di bawah, karena langkah-langkah lain membacanya dengan nama itu.

## Connector yang dipakai

| Connector | Dipakai untuk |
|---|---|
| Google Drive | Membuat folder, membuat Doc dan Sheet, mencari Brand Hub |
| Google Sheets | Membaca dan menulis Tasks, Bank Karya, Kalender Konten, Order, Rekap Mingguan |
| Google Docs | Mengisi dan mengubah Profil Brand |
| Google Calendar | Memasukkan jadwal tayang dan pengingat (Langkah 11) |
| Gmail | Menyiapkan draf balasan order, tidak pernah mengirim (Langkah 12) |

Sebelum membangun, cek connector mana yang menyala di chat ini. Kalau Drive atau Sheets mati, minta artist menyalakannya (klik + di kotak pesan, Connectors). Calendar dan Gmail baru dibutuhkan di Langkah 11 dan 12.

Kalau ada skill google-workspace, baca dulu sebelum menulis ke Sheet atau Doc.

## Hal teknis yang wajib diingat

1. **Atur format spreadsheet sebelum menulis rumus.** Begitu Sheet dibuat, set locale `in_ID` (kode Google untuk bahasa Indonesia, bukan `id_ID` yang akan ditolak) dan time zone `Asia/Jakarta` lewat `updateSpreadsheetProperties`. Dengan locale ini tanggal tampil dalam bahasa Indonesia dan **pemisah rumus adalah titik koma**. Semua rumus di file ini sudah memakai titik koma. Rumus yang ditulis dengan koma akan error.
2. Jangan pakai array literal seperti `{"a","b"}` di rumus. Pemisahnya berbeda per locale dan mudah error.
3. Tanggal ditulis sebagai `2026-11-18`, nanti tampil sesuai format kolom.
4. Teks yang mirip angka ditulis dengan tanda kutip satu di depan, misalnya tahun `'2026`.
5. Baca dulu baris yang mau diubah sebelum menulis. Jangan menimpa baris lain.

## 1. Folder

Di Drive artist, buat:
- Folder `Brand Hub, <nama akun>` di My Drive.
- Di dalamnya, subfolder `Karya dan Proses`.

## 2. Doc Profil Brand

Buat lewat Drive `create_file` dengan konten HTML (contentMimeType `text/html`, parentId folder Brand Hub), judul `Profil Brand`. Drive mengubahnya jadi Google Doc. Isinya:

- Judul: Profil Brand
- Kalimat pembuka miring: "Pegangan untuk semua bio, caption, dan halaman web. Bagian yang tampil ke publik ditulis dalam Bahasa publik brand."
- Bagian (heading 2): Ringkasan akun, Artist di balik akun (solo atau tim tanpa merinci peran anggota, dan siapa yang membalas komentar dan DM), Pembeda (jawaban artist soal apa yang membuat studionya berbeda dari studio lain di niche yang sama), Layanan (baris "Model bisnis" dan "Model utama", lalu tabel Layanan atau produk, Kisaran harga, Catatan), Audiens (dengan baris "Bahasa publik": Inggris, Indonesia, atau dua bahasa), Gaya visual, Suara (Kata atau ungkapan yang sering dipakai, Kata yang dihindari, Panjang kalimat, Pemakaian emoji, Contoh caption asli), Pilar konten (tabel Pilar, Contoh isi, Porsi), Batasan (selalu ada "Tidak membahas tuduhan atau komunitas lama"), Kanal dan link (tabel Kanal, Alamat, Status, dengan baris Web atau halaman satu lembar, X, Instagram, TikTok, YouTube, Bluesky (opsional), Discord, WhatsApp Business (kalau ada klien lokal), Portofolio (ArtStation atau Behance, dan folder Drive kalau ada), Platform order atau toko), Catatan aturan platform. Setelah Langkah 6 ditambah bagian Riset (dengan tanggal dan sumber), Positioning, dan Bio per kanal.

Kalau draf Profil Brand dari Langkah 1 sudah disetujui, langsung tulis isinya di HTML ini, tidak perlu membuat kosong dulu. Perubahan berikutnya dikerjakan lewat connector Google Docs pada Doc yang sama.

## 3. Sheet Brand Hub

Buat Sheet kosong bernama `Brand Hub` di folder Brand Hub. Lalu, dalam satu `update_spreadsheet`:
- `updateSpreadsheetProperties`: locale `in_ID`, timeZone `Asia/Jakarta`.
- Ganti nama tab pertama (sheetId 0) jadi `Beranda` dan sembunyikan gridline.
- `addSheet` dengan sheetId tetap: 1 `Tasks`, 2 `Bank Karya`, 3 `Kalender Konten`, 4 `Order`, 6 `Daftar Harga`, 5 `Rekap Mingguan` (Daftar Harga diletakkan sebelum Rekap Mingguan). Bekukan baris pertama di tab 1 sampai 5, dan kolom pertama di Bank Karya.

### Tab Tasks

Kolom A sampai I: `No`, `Langkah`, `Fase`, `Status`, `Kondisi`, `Alat`, `Selesai kalau`, `Due`, `Catatan`.

| No | Langkah | Fase | Alat | Selesai kalau |
|---|---|---|---|---|
| 'A | Pemetaan model bisnis dan kanal | Persiapan | Claude | Model bisnis dan Kondisi tiap langkah sudah tercatat |
| 1 | Tentukan brand voice | Fondasi akun | Claude | Profil Brand terisi lengkap |
| 'B | Siapkan ruang kerja brand | Persiapan | Claude | Folder, Profil Brand, dan Sheet ini sudah ada dan sudah dibuka artist |
| 2 | Audit fondasi | Fondasi akun | Claude | Ada daftar kekurangan dengan prioritas |
| 3 | Kumpulkan stok karya | Fondasi akun | Manual | Semua karya kandidat ada di Bank Karya dengan link folder prosesnya |
| 4 | Kurasi karya | Fondasi akun | Claude | 9 sampai 12 karya berkeputusan Tampil |
| 5 | Perbaiki web | Perbaikan web dan kanal | Claude Code | Semua temuan prioritas tinggi untuk web beres dan halaman wajib ada |
| 6 | Samakan bio semua kanal | Perbaikan web dan kanal | Manual | Semua bio jujur, seragam, dan link-nya benar |
| 7 | Siapkan dua jalur order | Perbaikan web dan kanal | Manual | Dua jalur order aktif dan sudah diuji |
| 8 | Buat akun yang belum ada | Perbaikan web dan kanal | Manual | Semua kanal wajib ada, username sama, dan bio terpasang |
| 9 | Bangun server Discord | Perbaikan web dan kanal | Manual | Server, channel, aturan, role, dan sistem tiket siap, link terpasang di web |
| 10 | Posting karya bertahap | Peluncuran bertahap | Scheduler | Unggahan karya 2 minggu ke depan ada di Kalender Konten |
| 11 | Kalender konten 2 minggu | Peluncuran bertahap | Calendar | Dua minggu ke depan terisi di Kalender Konten dan Google Calendar |
| 12 | Jalankan 2 minggu | Peluncuran bertahap | Manual | Semua jadwal 2 minggu sudah Tayang atau dibatalkan |
| 13 | Evaluasi | Evaluasi siklus pertama | Claude | Rekap Mingguan dua minggu pertama terisi dan ada daftar perubahan |

Status awal semua `Belum`. Kondisi diisi dari Pemetaan.

Dropdown (`ONE_OF_LIST`, strict, showCustomUi) sampai baris 40:
- Status: Belum, Jalan, Selesai
- Kondisi: Sudah ada, Perlu dirapikan, Perlu dibangun, Tidak relevan
- Alat: Claude, Claude Code, Manual, Scheduler, Calendar

Warna bersyarat: Status Selesai hijau dan Jalan biru. Kondisi Sudah ada hijau, Perlu dirapikan kuning, Perlu dibangun biru. Seluruh baris abu-abu dan dicoret kalau `=$E2="Tidak relevan"`. Baris tahap (No berupa satu huruf) miring dengan rumus `=REGEXMATCH(TO_TEXT($A2);"^[A-Z]$")`. Jangan pakai `ISTEXT`, karena baris tugas tambahan seperti '3.1 juga berupa teks dan ikut miring.

Catatan teknis: `addConditionalFormatRule` tanpa `index` menaruh aturan baru di posisi 0, jadi urutan aturan di Sheet terbalik dari urutan kamu menambahkannya. Sebelum memakai `updateConditionalFormatRule`, baca dulu daftar aturannya dengan `get_spreadsheet` (field `sheets.conditionalFormats`) dan pakai index dari hasil baca itu.

### Tab Bank Karya

Kolom A sampai T: `Karya`, `Pratinjau`, `Link file`, `Layanan`, `Tahun`, `Folder proses`, lalu sepuluh kotak centang `1 Dikerjakan sendiri`, `2 File proses ada`, `3 Izin klien`, `4 Tanpa AI generatif`, `5 Kualitas terbaik`, `6 Mewakili layanan`, `7 Gaya sejalan`, `8 Keterangan fan art`, `9 Tanpa data klien`, `10 File rapi` (kolom G sampai P), lalu `Skor`, `Boleh tampil`, `Keputusan`, `Catatan`.

- G sampai P: validasi `BOOLEAN` sampai baris 60.
- Q2: `=IF(A2="";"";COUNTIF(G2:P2;TRUE))`
- R2: `=IF(A2="";"";IF(AND(G2;I2;J2);"Ya";"Tidak"))`
- Salin Q2:R2 ke bawah sampai baris 60 dengan `copyPaste` PASTE_FORMULA.
- Dropdown Layanan sesuai layanan atau jenis produk di Profil Brand. Dropdown Keputusan: Tampil, Cadangan, Tidak.
- Warna: Boleh tampil Ya hijau dan Tidak merah. Keputusan Tampil hijau, Cadangan kuning, Tidak abu-abu.
- Kolom Pratinjau boleh diisi `=IMAGE("<link gambar publik>")`. File Drive yang privat tidak bisa ditampilkan, jadi cukup isi Link file kalau gambarnya privat.

### Tab Kalender Konten

Kolom A sampai J: `Tanggal tayang`, `Judul`, `Kanal`, `Format`, `Status`, `Karya`, `Caption (EN)`, `Link tayang`, `Sudah di Calendar`, `Catatan`.

- A: format tanggal `ddd, d mmm yyyy` dan validasi `DATE_IS_VALID`.
- Kanal: teks bebas, beberapa kanal dipisah koma, misalnya `Instagram, TikTok, YouTube Shorts`.
- Format: Karya jadi, WIP, Proses, Info slot, Info produk.
- Status: Ide, Draf, Ditulis ulang, Terjadwal, Tayang. Warna: Tayang hijau, Terjadwal biru, Ditulis ulang kuning, Draf oranye muda.
- Karya: `ONE_OF_RANGE` ke `='Bank Karya'!$A$2:$A$60`, tidak strict.
- Sudah di Calendar: `BOOLEAN`.

### Tab Order

Tab ini sementara. Begitu Google Form disambungkan (Langkah 7), tab ini diganti tab jawaban Form. Kolom sementara: `Masuk`, `Name or handle`, `Email`, `Preferred contact`, `Discord username`, `Service`, `Description`, `Reference links`, `Budget range`, `Deadline`, `Usage`, `Read ToS`, lalu kolom milik artist `Status order`, `Harga deal`, `Jalur bayar`, `Bukti proses`, `Catatan`, `Sumber`.

- Status order: Baru, Dibalas, Deal, Dikerjakan, Selesai, Batal. Warna: Baru kuning tebal, Deal dan Dikerjakan biru, Selesai hijau, Batal abu-abu.
- Jalur bayar: PayPal invoice, Ko-fi, VGen, Transfer bank, Lainnya.
- Bukti proses: Lengkap, Sebagian, Belum. Lengkap berarti timelapse, file berlapis, WIP bertanggal, dan file akhir sudah tersimpan di folder `proses/` (daftarnya di `pengetahuan/lintas-platform.md` bagian Bukti proses kerja). Wajib Lengkap sebelum order VGen ditandai Selesai. Warna: Belum merah muda, Sebagian kuning, Lengkap hijau.
- Sumber: Form, WhatsApp, Platform, Rekomendasi, Lainnya. Baris dari Google Form diisi Form. Order dari WhatsApp atau platform dicatat manual oleh Claude setelah artist menempelkan ringkasannya.
- Header kolom milik artist diberi warna berbeda (cokelat) supaya jelas itu bukan isian klien.

### Tab Daftar Harga

Dibuat saat Tahap B supaya harga punya satu tempat. Kolom A sampai G: `Layanan`, `Paket atau extra`, `Status harga`, `Yang didapat klien`, `Harga global (USD)`, `Harga lokal (Rp)`, `Catatan`.

- Status harga: dropdown Usulan Claude, Standar studio.
- Format angka: kolom E `"$"#,##0`, kolom F `"Rp"#,##0`.
- Di bawah tabel, satu baris digabung (merge) dan miring: "Kalau studio sudah punya standar harga sendiri, kirimkan ke Claude. Status harga akan diubah jadi Standar studio dan dokumen teks siap tempel ikut direvisi."
- Diisi di Langkah 7. Sebelum itu biarkan kosong kecuali harga yang sudah diketahui dari Pemetaan.

### Tab Rekap Mingguan

Kolom A sampai J: `Minggu`, `Mulai`, `Selesai`, `Konten tayang`, `Pengikut baru`, `Inquiry masuk`, `Order deal`, `Yang berhasil`, `Yang kurang`, `Diubah minggu depan`.

Rumus baris 2, lalu salin ke bawah sampai baris 30:
- D2: `=IF(B2="";"";COUNTIFS('Kalender Konten'!$E:$E;"Tayang";'Kalender Konten'!$A:$A;">="&B2;'Kalender Konten'!$A:$A;"<="&C2))`
- F2: `=IF(B2="";"";COUNTIFS(Order!$A:$A;">="&B2;Order!$A:$A;"<"&C2+1))`
- G2: `=IF(B2="";"";SUMPRODUCT((Order!$A$2:$A>=B2)*(Order!$A$2:$A<C2+1)*ISNUMBER(MATCH(INDEX(Order!$A$2:$Z;0;MATCH("Status order";Order!$1:$1;0));{"Deal";"Dikerjakan";"Selesai"};0))))`

Rumus G2 memakai array literal dengan pemisah titik koma (satu kolom), yang aman di locale in_ID. Kalau tetap error, ganti dengan tiga COUNTIFS yang dijumlah.

Pengikut baru diisi manual, beri warna kuning muda sebagai tanda isian.

### Tab Beranda

Kolom A untuk label (lebar 230), kolom B untuk isi (lebar 560).

| Baris | A | B |
|---|---|---|
| 1 | Brand Hub (24pt, tebal) | |
| 2 | `<Nama akun>`. Tempat kerja satu akun branding, dipandu Claude. (miring) | |
| 4 | Progres (judul bagian) | |
| 5 | Langkah selesai | `=COUNTIFS(Tasks!A2:A;">=1";Tasks!D2:D;"Selesai")&" dari "&COUNTIF(Tasks!A2:A;">=1")&" langkah"` |
| 6 | | `=REPT("█";ROUND(20*COUNTIFS(Tasks!A2:A;">=1";Tasks!D2:D;"Selesai")/COUNTIF(Tasks!A2:A;">=1")))&REPT("░";20-ROUND(20*COUNTIFS(Tasks!A2:A;">=1";Tasks!D2:D;"Selesai")/COUNTIF(Tasks!A2:A;">=1")))` |
| 7 | Sedang dikerjakan | `=IFERROR(INDEX(FILTER(Tasks!B2:B;Tasks!D2:D="Jalan");1);IFERROR(INDEX(FILTER(Tasks!B2:B;Tasks!D2:D="Belum");1);"Semua langkah selesai"))` |
| 9 | Ringkasan (judul bagian) | |
| 10 | Karya berkeputusan Tampil | `=COUNTIF('Bank Karya'!S2:S;"Tampil")&" dari target 9 sampai 12"` |
| 11 | Konten 14 hari ke depan | `=COUNTIFS('Kalender Konten'!A2:A;">="&TODAY();'Kalender Konten'!A2:A;"<="&TODAY()+14)&" jadwal"` |
| 12 | Order baru belum dibalas | `=COUNTIF(INDEX(Order!A2:Z;0;MATCH("Status order";Order!1:1;0));"Baru")&" order"` |
| 14 | Link cepat (judul bagian) | |
| 15 | Profil Brand | `=HYPERLINK("<link Doc>";"Buka Profil Brand")` |
| 16 | Folder karya | `=HYPERLINK("<link folder Karya dan Proses>";"Buka folder Karya dan Proses")` |
| 17 | Form order | Belum dibuat, disiapkan di Langkah 7 (ganti dengan HYPERLINK setelah Form jadi) |
| 18 | Google Calendar | Belum disambung, disiapkan di Langkah 11 |
| 20 | Cara pakai (judul bagian) | |
| 21 sampai 25 | 1 sampai 5 | 1. Buka Claude dan ketik "lanjut panduan". Claude membaca tab Tasks lalu melanjutkan dari langkah yang belum selesai. 2. Karya baru masuk tab Bank Karya. Centang ceklisnya, lalu isi Keputusan. Karya hanya boleh Tampil kalau kolom Boleh tampil berisi Ya. 3. Jadwal posting ada di tab Kalender Konten. Claude bisa memasukkannya ke Google Calendar supaya ada pengingat di HP. 4. Order dari form, WhatsApp, dan platform dicatat di tab Order. Isi Status order setiap ada perkembangan. 5. Tiap akhir minggu, isi tab Rekap Mingguan bersama Claude. |
| 27 | Aturan dasar (judul bagian) | |
| 28 sampai 30 | | Satu aturan per baris. Baris 28: Reply, DM, dan komentar ditulis pemilik atau admin yang ditunjuk, dan pemilik tetap memantau. Baris 29: Jangan bahas tuduhan atau komunitas lama. Posting karya dan prosesnya saja. Baris 30: Folder ini hanya dibagikan ke admin dan tim yang dipercaya. |

### Tampilan

- Header tab 1 sampai 5: latar hijau tua `#1F5F5B`, teks putih tebal, tinggi baris 40, teks dibungkus.
- Baris data: banding putih dan `#F6F9F8`, rata atas.
- Judul bagian di Beranda: latar `#E3ECEA`, teks `#1F5F5B` tebal 12pt, tinggi 30. Baris Cara pakai setinggi 44 supaya teksnya tidak terpotong.
- Warna tab: Beranda `#1F5F5B`, Tasks `#5B8C85`, Bank Karya `#C9A227`, Kalender Konten `#7FA99B`, Order `#B5651D`, Daftar Harga `#C9A227`, Rekap Mingguan `#8C8C8C`.
- Atur lebar kolom supaya label tidak terpotong. Kolom teks panjang (Selesai kalau, Caption, Description, Catatan) dibungkus.

### Cek setelah membangun

Baca ulang Beranda!A1:B18, Bank Karya Q1:R3, dan Rekap Mingguan A1:G3 dengan `get_values`. Tidak boleh ada `#ERROR!`, `#REF!`, `#NAME?`, atau `#VALUE!`. Kalau ada `#ERROR!`, hampir pasti pemisah rumusnya salah. Cek locale, lalu tulis ulang rumus dengan titik koma.

## Dokumen teks siap tempel

Mulai Langkah 7, buat satu Google Doc di folder Brand Hub, misalnya `Paket Jalur Order`, lewat Drive `create_file` dengan konten HTML. Isinya semua teks yang akan disalin admin: gig atau produk, paket, FAQ, ToS, profil dan balasan WhatsApp, teks Discord, dan isi halaman satu lembar. Tambahkan bagian baru di akhir dokumen setiap ada langkah yang menghasilkan teks. Untuk mengganti kata atau angka, pakai `replaceAllText`. Untuk mengganti isi sel tabel yang teksnya sama di beberapa tempat, baca dulu dokumennya untuk mencari index, lalu ganti dari index terbesar ke terkecil.

## Membaca dan menulis progres

- **Membaca posisi**: `get_values` pada `Tasks!A1:I40`. Langkah yang sedang dikerjakan adalah baris dengan Status Jalan. Kalau tidak ada, ambil baris pertama yang masih Belum sesuai urutan baris.
- **Mengubah Status atau Kondisi**: tulis langsung ke sel di baris langkah itu dengan `update_values`. Cari dulu nomor barisnya dari hasil baca, jangan menebak.
- **Menambah baris** (Bank Karya, Kalender Konten, Rekap Mingguan): baca kolom A untuk mencari baris kosong pertama, lalu tulis di sana. Jangan menulis di atas baris yang sudah terisi.
- **Profil Brand**: ubah lewat connector Google Docs pada bagian yang dimaksud saja.
- **Temuan audit** (Langkah 2): tambahkan sebagai baris baru di Tasks di bawah baris 16, dengan No desimal seperti 5.1 dan 5.2, Fase sesuai langkahnya, dan Status Belum.

## Form order (Langkah 7)

Connector belum bisa membuat Google Form, jadi pandu artist membuatnya. Berikan sebagai satu daftar:

1. Buka forms.google.com dengan akun Google akun branding, lalu klik Blank form.
2. Judul form dan deskripsi singkatnya disusun dengan suara brand dalam Bahasa publik. Jangan memakai judul baku yang sama untuk semua brand.
3. Tambahkan pertanyaan sesuai daftar informasi di langkah/07-jalur-order.md, dengan kata-kata yang sudah disusun untuk brand itu. Pilihan cara kontak memakai pilihan ganda sesuai alur order yang dipilih brand, dan layanan memakai dropdown sesuai price sheet.
4. Klik Settings, buka Responses, lalu nyalakan Collect email addresses (Verified). Kolom Email jadi terisi otomatis.
5. Masih di Settings, buka Presentation, lalu isi Confirmation message dengan teks dari Langkah 7 sesuai alur order yang dipilih brand, misalnya link Discord dan arahan ke channel tiketnya, atau perkiraan kapan email dibalas.
6. Buka tab Responses di atas form, klik Link to Sheets, pilih Select existing spreadsheet, lalu pilih Sheet Brand Hub. Google membuat tab baru berisi jawaban form.

Setelah itu kamu yang merapikan Sheet. Tunjukkan dulu rencananya dan kerjakan setelah artist setuju:
1. Baca tab Order lama. Kalau hanya berisi baris contoh, minta izin menghapus tab itu. Kalau ada data asli, pindahkan dulu ke tab baru.
2. Ganti nama tab jawaban form jadi `Order` dan beri warna tab `#B5651D`.
3. Tambahkan lima kolom di kanan pertanyaan terakhir: `Status order`, `Harga deal`, `Jalur bayar`, `Catatan`, `Sumber`, lengkap dengan dropdown dan warna seperti tab Order sementara.
4. Ganti isi Beranda!B17 dengan `=HYPERLINK("<link form>";"Buka form order")`.
5. Cek Beranda!B12 dan Rekap Mingguan G2. Keduanya mencari kolom Status order lewat nama header, jadi tetap jalan walaupun posisi kolomnya bergeser.

Minta artist mengisi form sekali sebagai uji coba, lalu cek baris barunya muncul di tab Order.

## Calendar (Langkah 11)

- Tanyakan dulu jam berapa artist biasa posting, dan apakah ia mau pengingat 1 jam sebelumnya.
- Untuk tiap baris Kalender Konten yang belum dicentang Sudah di Calendar, buat event di Google Calendar artist:
  - Judul: `Tayang: <Judul> (<Kanal>)`
  - Waktu: Tanggal tayang dan jam posting dari artist, durasi 15 menit.
  - Deskripsi: caption dari kolom Caption (EN) dan link ke Sheet Brand Hub.
  - Pengingat sesuai pilihan artist.
- Tunjukkan daftar event yang akan dibuat, buat setelah artist setuju, lalu centang Sudah di Calendar di baris itu.
- Tawarkan juga satu event berulang tiap Minggu malam: `Isi Rekap Mingguan`.
- Kalau jadwal di Kalender Konten berubah, ubah event yang sama. Jangan membuat event baru.

## Gmail (Langkah 12)

- Gmail hanya dipakai untuk membaca email order yang masuk dan menyiapkan draf balasan kalau artist minta.
- Draf ditulis dalam bahasa Inggris sesuai Suara di Profil Brand. Beri tahu artist bahwa draf sudah ada di folder Drafts.
- Kamu tidak pernah mengirim email. Artist membaca, menyesuaikan dengan gayanya, lalu mengirim sendiri.
