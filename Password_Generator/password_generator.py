import random
import string

### Kodun Dokümantasyonu ve Gerekçeleri
# 1. string.ascii_letters, string.digits ve string.punctuation kütüphaneden 
#    gelen standart karakter setleridir. Bu, karakterleri tek tek yazmaktan daha temizdir.
# 2. random.sample(karakter_havuzu, uzunluk) fonksiyonu, verilen havuzdan 
#    tekrar etmeyen rastgele elemanları seçmek için en verimli yoldur.
# 3. "".join() metodu, seçilen karakter listesini tek bir metin (string) haline getirir.

def generate_password(uzunluk):
    """
    Belirtilen uzunlukta rastgele ve güçlü bir şifre oluşturur.
    """
    # Tüm olası karakter setlerini birleştirme
    kucuk_harfler = string.ascii_lowercase
    buyuk_harfler = string.ascii_uppercase
    sayilar = string.digits
    ozel_karakterler = string.punctuation
    
    # Tüm havuzu oluşturma
    karakter_havuzu = kucuk_harfler + buyuk_harfler + sayilar + ozel_karakterler

    if uzunluk < 4:
        # En az 4 karakterde birer tür (küçük, büyük, sayı, özel) olmasını öneriyoruz.
        print("Uyarı: Şifre uzunluğu en az 4 olmalıdır.")
        return None
    
    # Şifreyi random.sample ile oluşturma
    # random.sample: Belirtilen havuzdan belirtilen sayıda (uzunluk) rastgele öğe seçer.
    sifre_listesi = random.sample(karakter_havuzu, uzunluk)
    
    # Listeyi tek bir string (metin) halinde birleştirme
    sifre = "".join(sifre_listesi)
    
    return sifre

# --- Uygulama Başlangıcı ---
if __name__ == "__main__":
    print("✨ PYTHON İLE GÜÇLÜ ŞİFRE ÜRETİCİ ✨")
    
    try:
        # Kullanıcıdan uzunluk bilgisini alma
        # int(input()): Kullanıcının girdiği değeri tam sayıya dönüştürür.
        istenen_uzunluk = int(input("Oluşturmak istediğiniz şifrenin uzunluğunu girin (Örn: 12): "))
        
        yeni_sifre = generate_password(istenen_uzunluk)
        
        if yeni_sifre:
            print("\n-------------------------------------")
            print(f"Oluşturulan Güçlü Şifre: **{yeni_sifre}**")
            print("-------------------------------------")
            
    except ValueError:
        print("\nHATA: Lütfen geçerli bir sayı girin.")
    except Exception as e:
        print(f"\nBeklenmedik bir hata oluştu: {e}")