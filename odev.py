from bkütüphane import *

veriler=Veriler()
print("""Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;

                     1. Şarkı İsmi
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi

                     Örnek Metodlar;
                    
                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil
                     4. Şarkıları göster
                     çıkmak için "q" ya basınız """)
while True:
    islem=input("İslem giriniz: ")

    if (islem=="q"):
        print("Çıkılıyor...")
        time.sleep(1)
        break
    elif (islem=="1"):
        print("Süreler toplamı: ")
        veriler.sarkı_süresi_hesapla()
    elif (islem=="2"):
        isim=input("Şarkı ismi: ")
        sanatçı=input("Sanatçı: ")
        albüm=input("Albüm: ")
        sirket=input("Prodüksiyon sirketi: ")
        sarkı_süresi=int(input("şarkı süresi: "))
        yeniler=Sarkı(isim,sanatçı,albüm,sirket,sarkı_süresi)
        veriler.sarkı_ekle(yeniler)
    elif (islem=="3"):
        isim=input("İsim gir: ")
        veriler.sarkı_sil(isim)
    elif (islem=="4"):
        veriler.sarkı_goster()
    else:
        print("Yanlış girdiniz")





