import data #logics → data’daki ogrenciler’i kullanır

def ekle(ogrNo,isim,bolum):
    if ogrNo in data.ogrenciler:
        return "Bu öğrenci kayıtlı!"
    else:
        data.ogrenciler[ogrNo]={
            "isim":isim,
            "bolum":bolum
        }
        return "Başarıyla eklendi!"
    
def arama(ogrNo):
    if ogrNo in data.ogrenciler:
        return data.ogrenciler[ogrNo]
    else:
        return "Öğrenci bulunamadı."
    
def sil(ogrNo):
    if ogrNo in data.ogrenciler:
        del data.ogrenciler[ogrNo]
        return "Öğrenci Silindi."
    else:
        return "Öğrenci bulunamadı"
    
def guncelle(ogrNo, isim=None, bolum=None):
    if not ogrNo in data.ogrenciler:
        return "Öğrenci bulunamadı!"
    
    if isim is not None:
        data.ogrenciler[ogrNo]["isim"]=isim

    if bolum is not None:
        data.ogrenciler[ogrNo]["bolum"]=bolum

    return "Öğrenci başarıyla güncellendi!"
    