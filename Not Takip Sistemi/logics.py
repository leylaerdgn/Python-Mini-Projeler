import data

def ekle(baslik, icerik, tarih):
    if not data.notlar:
        yeni_id=1
    else: 
        yeni_id=max(int(i) for i in data.notlar.keys()) +1


    data.notlar[str(yeni_id)] ={
        "baslik": baslik,
        "icerik":icerik,
        "tarih":tarih
    }

    data.verileri_kaydet()

    return f"Not başarıyla yüklnedi. ID: {yeni_id}"

def sil(id):
    if str(id) in data.notlar:
        del data.notlar[str(id)]
        data.verileri_kaydet()
        return "Başarıyla silindi"
    else:
        return "id bulunamadı"
    
def arama(id):
    if str(id) in data.notlar:
        return data.notlar[str(id)]
    else:
        return "Not bulunamadı!"
    
def guncelleme(id, baslik=None, icerik=None, tarih=None):
    if str(id) in data.notlar:
        if baslik is not None:
            data.notlar[str(id)]["baslik"] = baslik
        if icerik is not None:
            data.notlar[str(id)]["icerik"] = icerik
        if tarih is not None:
            data.notlar[str(id)]["tarih"] = tarih

        data.verileri_kaydet()
        return "Not başarıyla güncellendi."
    else:
        return "Not bulunamadı!"