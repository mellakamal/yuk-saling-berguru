# Kurasi Ulang

Jalankan kalau ada hasil kurasi sebelumnya: file `KURASI-*.md` di folder proyek, hasil kurasi yang ditempel pengguna, atau pengguna menulis "kurasi ulang", "cek lagi", "udah dibenerin".

## Menyimpan hasil kurasi
Supaya kurasi ulang bisa dilakukan:
- Di Claude Code dengan akses folder: simpan hasil lengkap ke `KURASI-YYYY-MM-DD.md` di akar folder proyek.
- Di chat: hasil kurasi tetap di percakapan. Untuk kurasi ulang, pengguna menempel hasil lama atau melanjutkan di percakapan yang sama.

## Langkah
1. Baca hasil kurasi terakhir: skor per area dan daftar perbaikan bernomor.
2. Periksa web dengan cara yang sama seperti kurasi pertama (lebar layar, halaman, dan mode yang sama), supaya skornya bisa dibandingkan.
3. Cek tiap butir perbaikan lama satu per satu terhadap kriteria "Selesai kalau"-nya.
4. Catat masalah baru yang muncul akibat perbaikan, misalnya layout HP rusak setelah section baru ditambahkan.

## Format di hasil
Ganti bagian Ringkasan dan Skor per area dengan:

**Perubahan skor**

| Area | Sebelum | Sesudah | Catatan |
|---|---|---|---|

**Status butir lama**

| No lama | Butir | Status |
|---|---|---|

Status: Selesai, Sebagian, Belum, atau Tidak jadi (kalau pemilik memutuskan tidak dikerjakan).

Lalu Daftar perbaikan dan Prompt Claude Code hanya berisi butir yang belum selesai ditambah masalah baru. Nomor butir lama dipertahankan, butir baru melanjutkan nomor terakhir.
