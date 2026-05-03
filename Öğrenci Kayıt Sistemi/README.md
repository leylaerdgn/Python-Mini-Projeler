# 🎓 Öğrenci Kayıt Sistemi (Student Management System)

##  Proje Açıklaması

Bu proje, Python kullanılarak geliştirilmiş basit bir **öğrenci kayıt ve yönetim sistemidir**.
Kullanıcı, terminal üzerinden öğrencileri ekleyebilir, silebilir, güncelleyebilir ve arayabilir.

Proje, yazılım geliştirme sürecinde **modüler yapı ve temel backend mantığını öğrenmek** amacıyla geliştirilmiştir.

##  Özellikler

*  Öğrenci ekleme
*  Öğrenci arama
*  Öğrenci güncelleme
*  Öğrenci silme
*  Kayıtlı öğrenciler üzerinde işlem yapabilme


##  Proje Yapısı

```bash
ogrenci_kayit_sistemi/
│
├── main.py        # Program akışını yönetir
├── logics.py      # İş mantığı (CRUD işlemleri)
├── interface.py   # Kullanıcıdan veri alma ve gösterme
├── data.py        # Öğrenci verilerinin tutulduğu yer
└── README.md      # Proje açıklaması
```

##  Çalışma Mantığı

Proje 4 ana katmandan oluşur:

* **data.py** → Verilerin tutulduğu katman
* **logics.py** → Veriler üzerinde işlem yapan katman
* **interface.py** → Kullanıcı ile etkileşim
* **main.py** → Tüm sistemi yöneten kontrol katmanı

Bu yapı, gerçek yazılım projelerinde kullanılan **katmanlı mimari (layered architecture)** mantığını basit bir şekilde yansıtır.


##  Öğrenilenler

Bu proje ile:

* Modüler Python yapısı
* Fonksiyonlar arası veri aktarımı
* CRUD işlemleri
* Dictionary ile veri yönetimi
* Basit sistem tasarımı

konuları pratik edilmiştir.

