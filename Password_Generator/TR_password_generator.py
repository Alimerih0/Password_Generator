import random
import string

def sifre_olustur(uzunluk):
    """
    Belirtilen uzunlukta rastgele ve güçlü bir şifre oluşturur.
    """
    # Karakter Setlerini Tanımla
    kucuk_harfler = string.ascii_lowercase
    buyuk_harfler = string.ascii_uppercase
    sayilar = string.digits
    ozel_karakterler = string.punctuation
    
    # Tüm havuzu oluşturma
    karakter_havuzu = kucuk_harfler + buyuk_harfler + sayilar + ozel_karakterler

    if uzunluk < 4:
        print("Uyarı: Şifre uzunluğu en az 4 olmalıdır.")
        return None
    
    # Rastgele Seçim Yap
    sifre_listesi = random.sample(karakter_havuzu, uzunluk)
    
    # Şifreyi Birleştir
    sifre = "".join(sifre_listesi)
    
    return sifre

if __name__ == "__main__":
    print("✨ PYTHON İLE GÜÇLÜ ŞİFRE ÜRETİCİ (TR) ✨")
    
    try:
        istenen_uzunluk = int(input("Oluşturmak istediğiniz şifrenin uzunluğunu girin (Örn: 12): "))
        
        yeni_sifre = sifre_olustur(istenen_uzunluk)
        
        if yeni_sifre:
            print("\n-------------------------------------")
            print(f"Oluşturulan Güçlü Şifre: **{yeni_sifre}**")
            print("-------------------------------------")
            
    except ValueError:
        print("\nHATA: Lütfen geçerli bir sayı girin.")