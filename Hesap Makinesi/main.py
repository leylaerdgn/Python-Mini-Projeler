import logics, interface

while True:
   secim=interface.islem_sec()
   
   if secim=='5':
      print("Programdan çıkılıyor...")
      break
   
   if secim in["1","2","3","4"]:
      a,b=interface.sayilari_al()

      if secim == "1":
            sonuc = logics.topla(a, b)
      elif secim == "2":
            sonuc = logics.cikar(a, b)
      elif secim == "3":
            sonuc = logics.carp(a, b)
      elif secim == "4":
            sonuc = logics.bol(a, b)

      interface.sonucu_goster(sonuc)

   else:
        interface.hata_goster("Hatali seçim yaptınız'")
