temperatura_celsius= int(input("diga qual a temperatura:  "))
farenheit= 0

converter= input("digite converte:  ")

if converter == "converte":
    farenheit = temperatura_celsius * 1.8 + 32
    print(f"a temperatura foi convertida de {temperatura_celsius} graus celsius para {farenheit} graus farenheit")


