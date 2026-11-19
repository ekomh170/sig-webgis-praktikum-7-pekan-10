# WebGIS Django Praktikum 7 SIG (Pekan 10)

Aplikasi WebGIS dengan Django 6.1, Leaflet.js 1.9.4, dan OpenStreetMap.
Project `webumkm` berisi dua app: `petaindonesia` dan `gempabumi`.

| URL               | App           | Isi                                                         |
| ----------------- | ------------- | ----------------------------------------------------------- |
| `/`               | petaindonesia | Beranda: daftar semua halaman                               |
| `/welcome/`       | petaindonesia | Teks sambutan (HttpResponse)                                |
| `/petasatu/`      | petaindonesia | Peta Indonesia + marker Jakarta                             |
| `/petadua/`       | petaindonesia | Latihan Mandiri 1: peta Jabodetabek dengan panel pilih kota |
| `/gempabumi/`     | gempabumi     | Latihan Mandiri 2: 15 gempa M 5.0+ terkini dari BMKG        |
| `/gempabumi/api/` | gempabumi     | Data gempa yang sudah diolah dalam format JSON              |

## Menjalankan (Windows)

Butuh Python 3.12 atau lebih baru (syarat Django 6.1).

```
git clone https://github.com/ekomh170/sig-webgis-praktikum-7-pekan-10.git
cd sig-webgis-praktikum-7-pekan-10
python -m venv webgis
webgis\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Buka http://localhost:8000/petadua/ atau http://localhost:8000/gempabumi/.

## Pengujian

```
python manage.py test
```

Data gempa: BMKG, https://data.bmkg.go.id/gempabumi/ (wajib mencantumkan BMKG sebagai sumber data).

## Dukung Proyek Ini

Kalau repository ini membantu belajarmu, kamu bisa mendukung lewat GitHub Sponsors:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/ekomh170)

Memberi ⭐ pada repository ini juga sudah sangat membantu.

> **Catatan:** Dibuat oleh **Eko Muchamad Haryono** ([@ekomh170](https://github.com/ekomh170)) untuk Praktikum 7 mata kuliah Sistem Informasi Geografis, STT Terpadu Nurul Fikri. Silakan dipakai sebagai referensi belajar dan cantumkan nama pembuat bila menyalin sebagian kode.
