# OpenShop RESTful API

OpenShop RESTful API adalah proyek backend sederhana berbasis Django REST Framework yang dibuat untuk memenuhi submission kelas **Belajar Back-End Pemula dengan Python** dari Dicoding.

API ini digunakan untuk mengelola data produk pada toko online dengan fitur CRUD (Create, Read, Update, Delete), pencarian produk berdasarkan nama, dan filter produk berdasarkan lokasi.

---

# Tech Stack

* Python 3.10
* Django 4.2 (LTS)
* Django REST Framework
* SQLite3
* Pipenv

---

# Fitur API

* Menambahkan produk
* Mendapatkan seluruh data produk
* Mendapatkan detail produk berdasarkan ID
* Update data produk
* Hapus produk
* Search produk berdasarkan nama
* Filter produk berdasarkan lokasi

---

# Struktur Project

```text
Submission-OpenShopRESTfulAPI-Dicoding/
│
├── OpenShop/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── OpenShop_RestFull_Api/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── .gitignore
```

---

# Instalasi

Clone repository:

```bash
git clone https://github.com/username/repository-name.git
cd Submission-OpenShopRESTfulAPI-Dicoding
```

Install dependency:

```bash
pipenv install
```

Masuk virtual environment:

```bash
pipenv shell
```

Migrasi database:

```bash
python manage.py migrate
```

Jalankan server:

```bash
python manage.py runserver
```

Server akan berjalan di:

```text
http://127.0.0.1:8000/
```

---

# API Endpoint

## Product List

### GET Products

```http
GET /products/
```

### Search Product by Name

```http
GET /products/?name=python
```

### Filter Product by Location

```http
GET /products/?location=jakarta
```

---

## Product Detail

### GET Product by ID

```http
GET /products/<id>/
```

### Update Product

```http
PUT /products/<id>/
```

### Delete Product

```http
DELETE /products/<id>/
```

---

# Example Request Body

```json
{
  "name": "Belajar Django",
  "sku": "DJG001",
  "description": "Kursus Django REST API",
  "shop": "Dicoding Academy",
  "location": "Bandung",
  "price": 1500000,
  "discount": 0,
  "category": "Course",
  "stock": 100,
  "is_available": true,
  "picture": "https://example.com/image.jpg"
}
```

---

# Example Response

## GET Products

```json
{
  "products": [
    {
      "id": "52e76895-7df6-40fc-ba70-8541bc84b5ac",
      "name": "Belajar Django",
      "sku": "DJG001",
      "description": "Kursus Django REST API",
      "shop": "Dicoding Academy",
      "location": "Bandung",
      "price": 1500000,
      "discount": 0,
      "category": "Course",
      "stock": 100,
      "is_available": true,
      "picture": "https://example.com/image.jpg"
    }
  ]
}
```

## GET Product Detail

```json
{
  "id": "52e76895-7df6-40fc-ba70-8541bc84b5ac",
  "name": "Belajar Django",
  "sku": "DJG001",
  "description": "Kursus Django REST API",
  "shop": "Dicoding Academy",
  "location": "Bandung",
  "price": 1500000,
  "discount": 0,
  "category": "Course",
  "stock": 100,
  "is_available": true,
  "picture": "https://example.com/image.jpg"
}
```

## Error Response

### Not Found

```json
{
  "detail": "Not found."
}
```

### Validation Error

```json
{
  "price": [
    "This field is required."
  ]
}
```

---

# Example Request Body

```json
{
  "name": "Belajar Django",
  "sku": "DJG001",
  "description": "Kursus Django REST API",
  "shop": "Dicoding Academy",
  "location": "Bandung",
  "price": 1500000,
  "discount": 0,
  "category": "Course",
  "stock": 100,
  "is_available": true,
  "picture": "https://example.com/image.jpg"
}
```

---

# Author

Created by **Irma Damaiyanti**

---

# License

Project ini dibuat untuk kebutuhan pembelajaran dan submission Dicoding.
