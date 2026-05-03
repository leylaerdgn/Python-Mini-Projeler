import logics,interface

while True:
    secim=interface.islem_sec()

    if secim=='1':
        ogrNo,isim,bolum=interface.ogrenci_bilgileri_al()
        sonuc=logics.ekle(ogrNo,isim,bolum)
        interface.sonuc_goster(sonuc)
    elif secim=='2':
        ogrNo=interface.ogrenci_no_al()
        sonuc=logics.sil(ogrNo)
        interface.sonuc_goster(sonuc)
    elif secim=='3':
        ogrNo, isim, bolum=interface.guncelleme_bilgileri_al()
        sonuc=logics.guncelle(ogrNo, isim, bolum)
        interface.sonuc_goster(sonuc)
    elif secim=='4':
        ogrNo=interface.ogrenci_no_al()
        sonuc=logics.arama(ogrNo)
        interface.sonuc_goster(sonuc)
    elif secim=='5':
        print("Programdan çıkılıyor...")
        break