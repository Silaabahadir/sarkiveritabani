import sqlite3
import time
"""Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;

                     1. Şarkı İsmi 
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi

                     Örnek Metodlar;

                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil"""
class Sarkı():

    def __init__(self,isim,sanatçı,albüm,sirket,sarkı_süresi):
        self.isim=isim
        self.sanatçı=sanatçı
        self.albüm=albüm
        self.sirket=sirket
        self.sarkı_süresi=sarkı_süresi
    def __str__(self):
        return f"Şarkının ismi: {self.isim}\nsanatçı: {self.sanatçı}\nalbüm: {self.albüm}\nprodüksiyon şirketi: {self.sirket}\nŞarkı süresi: {self.sarkı_süresi}\n"

class Veriler():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.connect=sqlite3.connect("benimkütüphanem.db")
        self.cursor=self.connect.cursor()

        sorgu="CREATE TABLE IF NOT EXISTS sarkılar(isim TEXT,sanatçı TEXT,albüm TEXT,sirket TEXT,sarkı_süresi INT)"
        self.cursor.execute(sorgu)
        self.connect.commit()
    def baglanti_kes(self):
        self.connect.close()
    def sarkı_goster(self):
        sorgu="SELECT * FROM sarkılar"
        self.cursor.execute(sorgu)
        sarkılar=self.cursor.fetchall()
        if (len(sarkılar)==0):
            print("hiç şarkı yok")
        else:
            for i in sarkılar:
                sarkı=Sarkı(i[0],i[1],i[2],i[3],i[4])
                print(sarkı)
    def sarkı_ekle(self,yeni):
        sorgu="INSERT INTO sarkılar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(yeni.isim,yeni.sanatçı,yeni.albüm,yeni.sirket,yeni.sarkı_süresi))
        self.connect.commit()

    def sarkı_sil(self,isim):
        sorgu="DELETE FROM sarkılar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.connect.commit()
    def sarkı_süresi_hesapla(self):
        sorgu="SELECT sarkı_süresi FROM sarkılar"
        self.cursor.execute(sorgu)
        sarkılar=self.cursor.fetchall()
        toplam=0
        for i in sarkılar:
            for a in i:
                toplam+=a
        print(toplam)

