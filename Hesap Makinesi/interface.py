def islem_sec():
    while True:
        secim= input('Yapmak istediğiniz işlemi seçiniz:\n1- Toplama\n2- Çıkarma\n3- Çarpma\n4- Bölme\n5- Çıkış\n ')
        if secim in ["1","2","3","4","5"]:
             return secim
        else:
            print('Hatalı Giriş! Lütfen 1-5 arasında bir sayı giriniz!')
def sayilari_al():
    while True:
        print('İşlem yapmak istediğiniz iki sayıyı giriniz: ')
        try:
            a=int(input('1. sayı: '))   
            b=int(input('2. sayı: ')) 
            return a,b
        except:
            print('Hatalı Giriş!')

def sonucu_goster(sonuc):
    print('Sonuç: ',sonuc)

def hata_goster(mesaj):
    print('Hata mesajı: ',mesaj)