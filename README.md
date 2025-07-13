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

```
postgresql://postgres:postgres@db:5432/EmbeddingDatabase
```

> Bu dosyada `db` ifadesi, docker-compose içerisindeki PostgreSQL servisinin adıdır.

---

## Veritabanı Yönetimi — PgAdmin Kullanımı

Proje Docker Compose ile PostgreSQL ve PgAdmin servislerini çalıştırmaktadır. Veritabanını görselleştirmek veya yönetmek için PgAdmin arayüzünü kullanabilirsiniz.

### PgAdmin’e Erişim

- PgAdmin web arayüzü `http://localhost:9090` adresinde çalışmaktadır.
- Burada email kısmına : admin@admin.com ve
- Parola kısmına : admin yazarak giriş yapabilirsiniz.

### PostgreSQL Server Bağlantısı

PgAdmin üzerinde yeni bir **Server** eklemek için:

1. **General** sekmesinde:

   - Name: `PostgresDB` (dilediğiniz isim olabilir)

2. **Connection** sekmesinde şu bilgileri girin:

   - **Host name/address:** `db`  
     _(Docker Compose’daki PostgreSQL servisi adı, PgAdmin konteynerinden erişim için)_
   - **Port:** `5432`
   - **Maintenance database:** `EmbeddingDatabase`  
     _(Docker Compose ortamında tanımladığınız veritabanı adı)_
   - **Username:** `postgres`
   - **Password:** `postgres`

3. Ayarları kaydedin ve bağlanın.

### Neden `db` kullanıyorum?

Docker Compose, servisleri aynı özel ağda oluşturur. Bu nedenle, PgAdmin konteyneri PostgreSQL konteynerine `localhost` veya `127.0.0.1` üzerinden değil, servis adı olan `db` üzerinden erişir.

### Özet

| Ayar                | Değer                 |
| ------------------- | --------------------- |
| PgAdmin URL         | http://localhost:9090 |
| PostgreSQL Hostname | db                    |
| PostgreSQL Port     | 5432                  |
| Veritabanı Adı      | EmbeddingDatabase     |
| Kullanıcı Adı       | postgres              |
| Parola              | postgres              |

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
