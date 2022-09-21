#Celsius        ->     Fahrenheit   ->      °F = °C × 1.8 + 32
#Fahrenheit     ->     Celsius	    ->      °C = (°F – 32) / 1.8
#Celsius	    ->     Kelvin       ->  	°K = °C + 273.15
#Kelvin         -> 	   Celsius	    ->      °C = °K – 273.15
#Fahrenheit     ->     Kelvin       ->      °K = (°F − 32) × 5 ⁄ 9 + 273.15
#Kelvin         ->     Fahrenheit   ->      °F = (°K – 273.15) × 9 ⁄ 5 + 32


def CelsiusToFahrenheit(celsius):
    Fahrenheit = celsius * 1.8 + 32
    return Fahrenheit

def FahrenheitToCelsius(Fahrenheit):
    Celsius = (Fahrenheit - 32) / 1.8
    return Celsius

def CelsiusToKelvin(celsius):
    Kelvin = celsius + 273.15
    return Kelvin

def KelvinToCelsius(Kelvin):
    Celsius = Kelvin - 273.15
    return Celsius

def FahrenheitToKelvin(Fahrenheit):
    Kelvin=(Fahrenheit-32)*(5/9)+ 273.15
    return Kelvin

def KelvinToFahrenheit(Kelvin):
    Fahrenheit=(Kelvin-273.15)*(9/5)+32
    return Fahrenheit


derece_al=float(input("Lütfen sıcaklık derecenizi giriniz: "))
a=input("Dönüştürmek istediğiniz sıcaklık birimi nedir: ")
if a=="Celsius":
    b=input("Hangi sıcaklık birimine dönüştürmek istersiniz: ")
    if b=="Fahrenheit":
        print(f"{CelsiusToFahrenheit(derece_al)} °F")
    elif b=="Kelvin":
        print(f"{CelsiusToKelvin(derece_al)} °K")
    else:
        print("Böyle bir sıcaklık birimi bulunmamaktadır. Doğru yazdığınızdan emin olunuz")        

elif a=="Fahrenheit":
    b=input("Hangi sıcaklık birimine dönüştürmek istersiniz: ")
    if b=="Celsius":
        print(f"{FahrenheitToCelsius(derece_al)} °C")
    elif b=="Kelvin":
        print(f"{FahrenheitToKelvin(derece_al)} °K")
    else:
        print("Böyle bir sıcaklık birimi bulunmamaktadır. Doğru yazdığınızdan emin olunuz")        
            
elif a=="Kelvin":
    b=input("Hangi sıcaklık birimine dönüştürmek istersiniz: ")
    if b=="Celsius":
        print(f"{KelvinToCelsius(derece_al)} °C")
    elif b=="Fahrenheit":
        print(f"{KelvinToFahrenheit(derece_al)} °F")
    else:
        print("Böyle bir sıcaklık birimi bulunmamaktadır. Doğru yazdığınızdan emin olunuz")        

else:
    print("Böyle bir sıcaklık birimi bulunmamaktadır. Doğru yazdığınızdan emin olunuz")
            
    