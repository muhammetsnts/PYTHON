import modul1
import time

print('''
##################

Hesap Makinesi

##################

****************************************
İŞLEMLER:

1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Aşağı yuvarla
6. Yukarı yuvarla
7. Karekök al
8. Mod al
9. Faktöriyel
10. Ebob
11. Hipotenüs
12. Çıkış
****************************************
''')

while True:
    işlem = int(input("İşlem seçiniz:"))
    if işlem == 12:
        print("Hesap makinesi kapatılıyor...")
        time.sleep(1)
        break

    a = float(input("1.Sayı :"))
    b = float(input("2.Sayı :"))

    if işlem == 1:
        print("Toplam=", modul1.toplama(a,b))
    elif işlem == 2:
        print("Fark=", modul1.çıkarma(a,b))
    elif işlem == 3:
        print("Çarpım=", modul1.çarpma(a,b))
    elif işlem == 4:
        print("Bölüm=", modul1.bölme(a,b))
    elif işlem == 5:
        print("Aşağı yuvarlama=", modul1.aşağıyuvarla(a), "--", modul1.aşağıyuvarla(b))
    elif işlem == 6:
        print("Yukarı yuvarlama=", modul1.yukarıyuvarla(a), "--", modul1.yukarıyuvarla(b))
    elif işlem == 7:
        print("Kare kök=", modul1.karekök(a), "ve", modul1.karekök(b))
    elif işlem == 8:
        print("Mod=", modul1.mod(a,b))
    elif işlem == 9:
        print("Faktöriyelleri=", modul1.faktöriyel(a), "ve", modul1.faktöriyel(b))
    elif işlem == 10:
        a = int(a)
        b = int(b)
        print("Ebob=", modul1.ebob(a,b))
    elif işlem == 11:
        print("Hipotenüs değeri=", modul1.hipotenüs(a,b))





