import math

# ---------------------------------------------------------
# Proje: Geometrik Hesaplamalar (Functions)
# Amaç: Fonksiyon tanımlama, parametre kullanımı ve return mekanizması.
# ---------------------------------------------------------

def daire_alani_hesapla(yaricap):
    """
    Verilen yarıçapa göre dairenin alanını hesaplar.
    Formül: π * r^2
    """
    return math.pi * (yaricap ** 2)

def daire_cevresi_hesapla(yaricap):
    """
    Verilen yarıçapa göre dairenin çevresini hesaplar.
    Formül: 2 * π * r
    """
    return 2 * math.pi * yaricap

# Fonksiyonları Test Edelim
r_degeri = 5
alan = daire_alani_hesapla(r_degeri)
cevre = daire_cevresi_hesapla(r_degeri)

print(f"Yarıçapı {r_degeri} olan dairenin;")
print(f"Alanı: {alan:.2f}")
print(f"Çevresi: {cevre:.2f}")

# Kullanıcıdan Bilgi Alma Örneği
def selamla():
    print("Geometri Hesaplayıcıya Hoş Geldiniz!")

selamla()
