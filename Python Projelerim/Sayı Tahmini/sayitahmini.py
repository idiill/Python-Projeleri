#PC RASTGELE 10 SAYI SEÇSİN
#SEÇTİKLERİNDEN 6 TANE SEÇSİN
#TEKRAR SEÇTİĞİNDEN 4 TANE SEÇSİN
#SEÇTİĞİ BU SAYIYI BULALUM
#3 HAK VERİLSİN


import random

maxtahsayi=3
secilen_onsayisayac=0
secilenaltisayac=0
secilendortsayac=0
nettahminsayi=0

onsayililist=[]
altisayililist=[]
dortsayililist=[]

while secilen_onsayisayac < 10:
    rastgele_on=int(random.random()*100)
    onsayililist.append(rastgele_on)
    secilen_onsayisayac += 1


while secilenaltisayac < 6:
    sixchoice=random.choice(onsayililist)
    altisayililist.append(sixchoice)
    secilenaltisayac += 1


while secilendortsayac < 4:

    fourchoice=random.choice(altisayililist)
    if dortsayililist.count(fourchoice) == 0:

        dortsayililist.append(fourchoice)
        secilendortsayac += 1

secilen_sayi=random.choice(dortsayililist)


print("10 sayımız : ",onsayililist)
print("10 sayıdan seçilen 6 sayımız : ",altisayililist)
print("6 sayıdan seçilen 4 sayımız : ",dortsayililist)


while nettahminsayi < maxtahsayi:
    sayitahmin=int(input("lütfen sayıyı tahmin ediniz : "))
    print("{} tahmin hakkınız kaldı".format(maxtahsayi - nettahminsayi-1))
    nettahminsayi += 1
    sayitahsayac=dortsayililist.count(sayitahmin)
    
    if sayitahmin==secilen_sayi:
        print("Tebrikler sayıyı doğru bildiniz.")
        break
        
    if nettahminsayi==maxtahsayi:
        print("Bilemediniz. Oyun bitti")


