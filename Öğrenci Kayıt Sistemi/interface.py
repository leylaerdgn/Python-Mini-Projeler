def islem_sec():
    while True:
        secim=input('Yapmak istediğiniz işlemi seçiniz: \n1- Ekle\n2- Silme\n3- Güncelleme\n4- Arama\n5- Çıkış\n ')
        if secim in ["1","2","3","4","5"]:
            return secim
        else:
            print('Yanlış sayı girdiniz! Lütfen 1-5 arasında giriniz!')
    
def ogrenci_bilgileri_al():
    ogrNo= int(input('Öğrenci Numarası: '))
    isim=input('İsim: ')
    bolum=input('Bölüm: ')
    return ogrNo, isim, bolum

def ogrenci_no_al():
     ogrNo= int(input('Öğrenci Numarası: '))
     return ogrNo

def guncelleme_bilgileri_al():
    ogrNo= int(input('Öğrenci Numarası: '))
    isim=input('İsim: ')
    bolum=input('Bölüm: ')
    if isim=="":
        isim=None
    if bolum=="":
        bolum=None
    return ogrNo, isim, bolum

def sonuc_goster(sonuc):
    print(sonuc)

def hata_goster(mesaj):
     print(mesaj)