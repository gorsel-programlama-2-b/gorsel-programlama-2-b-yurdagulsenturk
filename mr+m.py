# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:39:57 2023

@author: C-117
"""

class HesapMakinesi:
    def __init__(self):
        self.hafiza = 0
        self.suanki_deger = 0

    def topla(self, x):
        self.suanki_deger += x

    def cikar(self, x):
        self.suanki_deger -= x

    def carp(self, x):
        self.suanki_deger *= x

    def bol(self, x):
        if x != 0:
            self.suanki_deger /= x
        else:
            print("Hata: Sıfıra bölme")

    def hafiza_kaydet(self):
        self.hafiza = self.suanki_deger

    def hafiza_hatirla(self):
        self.suanki_deger = self.hafiza

    def temizle(self):
        self.suanki_deger = 0

    def goster(self):
        return self.suanki_deger


hesap_makinesi = HesapMakinesi()

while True:
    print("Şuanki Değer:", hesap_makinesi.goster())
    print("Seçenekler:")
    print("1. Topla")
    print("2. Çıkar")
    print("3. Çarp")
    print("4. Böl")
    print("5. M (Hafızaya Kaydet)")
    print("6. MR (Hafıza Geri Çağırma)")
    print("7. Temizle")
    print("8. Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == '1':
        num = float(input("Toplamak için bir sayı girin: "))
        hesap_makinesi.topla(num)
    elif secim == '2':
        num = float(input("Çıkarmak için bir sayı girin: "))
        hesap_makinesi.cikar(num)
    elif secim == '3':
        num = float(input("Çarpmak için bir sayı girin: "))
        hesap_makinesi.carp(num)
    elif secim == '4':
        num = float(input("Bölmek için bir sayı girin: "))
        hesap_makinesi.bol(num)
    elif secim == '5':
        hesap_makinesi.hafiza_kaydet()
    elif secim == '6':
        hesap_makinesi.hafiza_hatirla()
    elif secim == '7':
        hesap_makinesi.temizle()
    elif secim == '8':
        break
    else:
        print("Hatalı işlem.Tekrar deneyin!")