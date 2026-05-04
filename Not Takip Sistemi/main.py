import logics,data,interface

data.verileri_yukle()#Bu en başta olmalı ki eski notlar dosyadan yüklensin.

while True:
    secim=interface.islem_sec()

    if secim=="1":
        baslik,icerik,tarih=interface.not_ekle()
        sonuc=logics.ekle(baslik,icerik,tarih)
        interface.sonuc_goster(sonuc)

    if secim=='2':
        not_id=interface.not_sil()
        sonuc=logics.sil(not_id)
        interface.sonuc_goster(sonuc)

    elif secim == "3":
        not_id = interface.not_arama()
        sonuc = logics.arama(not_id)
        interface.sonuc_goster(sonuc)

    elif secim == "4":
        not_id, baslik, icerik, tarih = interface.not_guncelleme()
        sonuc = logics.guncelleme(not_id, baslik, icerik, tarih)
        interface.sonuc_goster(sonuc)

    elif secim == "5":
        print("Programdan çıkılıyor...")
        break
