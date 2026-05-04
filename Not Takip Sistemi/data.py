import json

notlar= {}

def verileri_yukle(): #Bu fonksiyon program başlarken çalışacak.
    global notlar #Ben fonksiyon içindeki yeni bir notlar değil, yukarıdaki notlar değişkenini değiştireceğim.
    try:
     with open("dosya.json", "r") as file:
        notlar=json.load(file)
    except FileNotFoundError:
       notlar ={}

def verileri_kaydet():
    with open("dosya.json", "w") as file:
        json.dump(notlar,file)
