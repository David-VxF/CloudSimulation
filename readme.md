# Simulasi Penyimpanan Cloud

Aplikasi baris perintah (CLI) kecil berbasis Python yang mensimulasikan layanan penyimpanan cloud sederhana dengan pendaftaran/login pengguna dan penyimpanan file per pengguna.

**Ringkasan singkat:** Daftar atau masuk menggunakan `main.py`, lalu unggah, lihat, atau hapus file yang disimpan di direktori `storage/` (satu folder per nama pengguna).

**Persyaratan**
- Python 3.6+

**Instalasi**
1. Salin atau clone repositori ini ke device Anda.
2. (Opsional) Buat virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Jalankan aplikasi:

```
python3 main.py
```

**Penggunaan**
- Pilih `1` untuk Sign Up (mendaftar) dan buat akun (username, email, password).
- Pilih `2` untuk Login dengan akun yang sudah ada.
- Setelah login, pilih `Cloud Storage` untuk mengelola file:
	- `Upload File` — membuat file kosong di `storage/<username>/`.
	- `View Files` — menampilkan daftar file di folder pengguna.
	- `Delete File` — menghapus file dengan memilih nomor file.


**File dalam proyek**
- `main.py` — file utama CLI dengan alur pendaftaran/login dan menu.
- `drive.py` — fungsi penyimpanan file (`upload_file`, `view_files`, `delete_file`) yang beroperasi di folder `storage/`.
- `emailValidation.py` — helper validasi email yang digunakan saat pendaftaran.
- `users.json` — menyimpan data pengguna yang terdaftar (dibuat otomatis saat diperlukan).
- `storage/` — direktori tempat folder pengguna dan file unggahan tersimpan.

**Catatan & Keterbatasan**
- `users.json` hanya file JSON sederhana; password di-hash menggunakan SHA-256, namun proyek ini hanya untuk pembelajaran/demo — jangan gunakan untuk layanan autentikasi nyata.
- Unggah file hanya membuat file kosong; ini hanya simulasi sederhana dan belum mendukung isi file asli, upload nyata, atau akses bersamaan.

**Reset / Pembersihan**
- Untuk menghapus semua pengguna dan file, hapus `users.json` dan folder `storage/`:

```
rm users.json
rm -rf storage/
```

**Lisensi**
Proyek ini dibuat apa adanya untuk tujuan pembelajaran. Gunakan atau adaptasi sesuai kebutuhan.
