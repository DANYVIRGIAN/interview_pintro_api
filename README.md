# Automation API

Proyek ini berisi pengujian API otomatis untuk [JSONPlaceholder](https://jsonplaceholder.typicode.com), dibuat menggunakan Python, `pytest`, dan `requests`. Proyek ini menggunakan pola *Service Object* untuk pemeliharaan dan skalabilitas yang lebih baik.

## Struktur Proyek

```
├── tests/              # Berisi kasus uji (test cases)
├── services/           # Kelas layanan (logika endpoint API)
├── utils/              # Kelas pembantu/utility (contoh: APIClient)
├── conftest.py         # Konfigurasi dan fixtures Pytest
├── requirements.txt    # Ketergantungan proyek (dependencies)
└── README.md           # Dokumentasi proyek
```

## Memulai

Ikuti langkah-langkah berikut untuk menyiapkan proyek di komputer lokal Anda.

### 1. Prasyarat
Pastikan Python sudah terinstal di komputer Anda.

### 2. Langkah Implementasi

Langkah-langkah berikut digunakan untuk menginisialisasi proyek:

```bash
# 1. Buat folder project utama
mkdir api_testing_project
cd api_testing_project

# 2. Buat Virtual Environment (biar library tidak tercampur)
python -m venv venv

# 3. Aktifkan Virtual Environment
# -> Untuk Windows:
venv\Scripts\activate
# -> Untuk Mac/Linux:
source venv/bin/activate

# 4. Install Dependencies
pip install pytest requests
```

## Running Test

Untuk menjalankan pengujian otomatis, jalankan perintah berikut di direktori root:

```bash
pytest
```

Untuk menjalankan pengujian dengan output yang lebih detail (verbose):
```bash
pytest -v
```

Untuk menjalankan file pengujian tertentu:
```bash
pytest tests/test_api_post.py
```

## Stack Teknologi

- **Python**: Bahasa Pemrograman
- **Pytest**: Kerangka Kerja Pengujian (Testing Framework)
- **Requests**: Library HTTP untuk melakukan pemanggilan API
