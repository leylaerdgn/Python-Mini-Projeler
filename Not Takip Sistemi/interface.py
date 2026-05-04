def islem_sec():
    while True:
        secim=input('Seçiminiz:\n1- Ekle\n2- Silme\n3- Arama\n4- Güncelleme\n5- Çıkış\n ')
        if secim in ["1","2","3","4","5"]:
            return secim
        else:
            print('Yanlış sayı girdiniz! Lütfen 1-5 arasında giriniz!')
        
def not_ekle():
    baslik=input('Başlık: ')
    icerik=input('İçerik: ')
    tarih= input('Tarih: ')
    return baslik,icerik,tarih
     
def not_sil():
    not_id=int(input("İD giriniz: "))
    return not_id

def not_arama():
    not_id=int(input("İD giriniz: "))
    return not_id

def not_guncelleme():
    not_id=int(input("İD giriniz: "))
    baslik=input('Başlık: ')
    icerik=input('İçerik: ')
    tarih= input('Tarih: ')
    if baslik=="":
        baslik=None
    if icerik=="":
        icerik=None
    if tarih=="":
        tarih=None
    return not_id,baslik,icerik,tarih

def sonuc_goster(sonuc):
    print(sonuc)
