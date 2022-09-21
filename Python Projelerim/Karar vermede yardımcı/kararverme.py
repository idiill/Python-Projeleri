
import random 
a=int(input("Kararsız kaldığınız kaç durum var: "))
  
sayac=0
durumlar=[]       
for i in range (sayac,a): 
    c=input(f"Kararsız kaldığınız {sayac+1}.durumu giriniz: ")
    durumlar.append(c)
    sayac+=1

secimi_yap=random.choice(durumlar)
print(f"Yapılan seçim: {secimi_yap}")
