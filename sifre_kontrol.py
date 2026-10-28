import re

def sifre_gucunu_kontrol_et(sifre):
    puan = 0
    
    if len(sifre) >= 8:
        puan += 1
    if re.search(r"[A-Z]", sifre):
        puan += 1
    if re.search(r"[a-z]", sifre):
        puan += 1
    if re.search(r"[0-9]", sifre):
        puan += 1
    if re.search(r"[^A-Za-z0-9]", sifre):
        puan += 1
        
    if puan <= 2:
        return "Zayıf Şifre"
    elif puan <= 4:
        return "Orta Güçte Şifre"
    else:
        return "Güçlü Şifre"

if __name__ == "__main__":
    parola = input("Kontrol edilecek şifreyi girin: ")
    sonuc = sifre_gucunu_kontrol_et(parola)
    print(f"Sonuç: {sonuc}")
