import random 
a=int(input("Kararsız kaldığınız kaç durum var: "))
  
sayac=0
durumlar=[] 

if a==1:
    print("Seçim yapılabilmesi için lütfen en az iki durum giriniz.") 
    
else:
    for i in range (sayac,a): 
        c=input(f"Kararsız kaldığınız {sayac+1}.durumu giriniz: ")
        durumlar.append(c)
        sayac+=1
    secimi_yap=random.choice(durumlar)
    print(f"Yapılan seçim: {secimi_yap}")
