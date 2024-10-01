#İlk aşamada fonksiyonları kullanarak bir dictionary tipinde yani key 
# value ikilisini kullanarak bir rehber uygulaması yapmanı rica ediyorum
# id, ad, soyad, telefon, ve adres tutsun fonksiyonlar kişi kaydet kişi 
# çıkar kişi düzenle ve kişileri getir fonksiyonları yanında id kişi
# ekledikçe otomatik artsın. id ye göre de kişileri arama fonksiyonu olsun.

rehber = [
    {"id" : 1, 
     "ad" : "deniz", 
     "soyad" : "erdoğan", 
     "telefon" : 1234567890,
     "adres" : "itü ayazağa kampüsü"},
    {"id" : 2, 
     "ad" : "baran", 
     "soyad" : "tapar", 
     "telefon" : 1238473992,
     "adres" : "fulya şişli"},
     {"id" : 3, 
     "ad" : "özge", 
     "soyad" : "öz", 
     "telefon" : 1238487492,
     "adres" : "altan edige yurdu"}
     
]

sayac = len(rehber)



def kisileriListele():
    for kisi in rehber:
        print("-----------------")
        print("id: ", kisi["id"])
        print("adı: ", kisi["ad"])
        print("soyad: ", kisi["soyad"])
        print("telefon: ", kisi["telefon"])
        print("adres: ", kisi["adres"])
        print("-----------------")



def kisiEkle():
    kisi = {}
    kisi["id"] = sayac + 1
    kisi["ad"] = input("yeni kişinin adını giriniz: ")
    kisi["soyad"] = input("kişinin soyadını giriniz: ")
    kisi["telefon"]  = int(input("kişinin telefon numarasını giriniz: "))
    kisi["adres"] = input("kişinin adres bilgilerini giriniz giriniz: ")
    rehber.append(kisi)


def kisiyiSil():
    id = int(input("silmek istediğiniz kişinin id'sini giriniz: "))
    for kisi in rehber:
        if id == kisi["id"]:
            print("{} {} kişisi silindi.".format(kisi["ad"],kisi["soyad"]))
            rehber.remove(kisi)
            return 
        
    print("bu id'ye sahip bir kişi bulunamadı.")
       
          

def kisiDuzenle():
    id = int(input("düzenlemek istediğiniz kişinin id'sini giriniz: "))
    for kisi in rehber:
        if id == kisi["id"]:
             while True:
                islem = input("neyi düzenlemek istediğinizi girin(ad,soyad,telefon,adres): ")
                if islem in ["ad", "soyad", "telefon", "adres"]:
                    if islem == "telefon":
                        kisi[islem] = int(input(f"{islem}: "))
                    else:
                        kisi[islem] = input(f"{islem}: ")
                    print("Bilgi güncellendi.")
                    return
                else:
                    print("Geçersiz işlem. Lütfen tekrar deneyin.")
               
    print("bu id'ye sahip kişi bilgisi bulunamadı.")
 

    
def kisiyiAra():
   
    id = int(input("aramak istediğiniz kişinin id'sini giriniz: "))
    for kisi in rehber:
        if id == kisi["id"]:
            print("{} {} aranıyor...".format(kisi["ad"],kisi["soyad"]))
            return
        
    print("bu id'ye sahip bir kişi bulunamadı.")
       


def menu():
   print("++++++++++++REHBER++++++++++")
   print("---1. kişileri gör----------")
   print("---2. kişi ekle-------------")
   print("---3. kişi sil--------------")
   print("---4. rehberden birini ara--")
   print("---5. kişiyi düzenle--------")
   print("işlemi sonlandırmak için 0'ı tuşlayınız.\n")
   
   while True:
    islem=int(input("yapmak istediğiniz işlemi tuşlayın: "))
    
    if islem == 0:
      print("çıkılıyor...")
      return    

    elif islem == 1:
       kisileriListele()
       
    elif islem == 2:
       kisiEkle()
       
    elif islem == 3:
       kisiyiSil()
       
    elif islem == 4:
       kisiyiAra()
       
    elif islem == 5:
       kisiDuzenle() 
       
    else:
       print("yanlış bir tuşlama yaptınız.")
    
    menu()
       
   
menu()


