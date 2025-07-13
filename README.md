# EmbeddingApp (Dockerized)

Bu proje, Flask ve SentenceTransformers kullanarak girilen metinleri vektör haline getirir ve PostgreSQL veritabanına kaydeder. Tüm sistem Docker ile birlikte çalışır.

---

## 🧰 Gereksinimler

- [Docker](https://www.docker.com/get-started) (Docker Desktop yüklü olmalı)
- [Docker Compose](https://docs.docker.com/compose/) (Docker ile birlikte gelir)

---

## 📦 Kurulum Adımları

### 1. Projeyi İndirin

GitHub üzerinden indirin:

```bash
git clone https://github.com/Clean-Code0244/embedding-app.git

```

### 2. Uygulamayı Başlatın

```bash
docker-compose up --build
```

Bu komut:

- PostgreSQL veritabanı container'ını başlatır
- Flask uygulamasını derler
- Modeli indirir
- Otomatik olarak `EmbeddingDatabase` veritabanında tabloyu oluşturur

---

## 🌐 Uygulamaya Erişim

Tarayıcınızdan aşağıdaki adrese gidin:

```
http://localhost:5000
```

- Metin girerek embedding yapılmasını sağlayabilirsiniz
- Metinler ve vektör karşılıkları veritabanında saklanır

---

---

## 🗃️ Veritabanı Bilgileri

Veritabanı bilgileri `.env` dosyasında saklanır. Örnek:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/EmbeddingDatabase
```

> Bu dosyada `db` ifadesi, docker-compose içerisindeki PostgreSQL servisinin adıdır.

---

## 📌 Notlar

- İlk çalıştırmada model indirileceğinden dolayı internet bağlantısı gerekir.
- Tablolar uygulama başlatıldığında otomatik olarak oluşturulur.
- Veriler, Docker volume ile kalıcı olarak saklanır.

---

## Uygulamayı Durdurmak

```bash
docker-compose down

Geliştirici: Yusuf Ömer Tursun
```
