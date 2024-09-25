print("selecione a operação")
print("1. Adição")
print("2. Subtração")
print("3. Divisão")
print("4. Multiplicação")
print("5. Raiz quadrada")
print("6. Potenciação")

selecionar= input("digite 1 , 2 , 3, 4, 5 ou 6:  ")
parada= 1

while(parada==1):
    if selecionar == '1':
        num1= float(input("digite o primeiro número:  "))
        num2= float(input("digite o segundo número:  "))
        num3 = num1 + num2
        print(f"{num3}")

    elif selecionar == '2':
        num1= float(input("digite o primeiro número:  "))
        num2= float(input("digite o segundo número:  "))
        num3 = num1 - num2
        print(f"{num3}")

    elif selecionar == '3':
        num1= float(input("digite o primeiro número:  "))
        num2= float(input("digite o segundo número:  "))
        num3 = num1 / num2
        print(f"{num3}")

    elif selecionar == '4':
        num1= float(input("digite o primeiro número:  "))
        num2= float(input("digite o segundo número:  "))
        num3 = num1 * num2
        print(f"{num3}")

    elif selecionar == '5':
        num1= float(input("digite o número:  "))
        num2= num1 ** (1/2)
        print(f"{num2}")

    elif selecionar == '6':
        num1= float(input("digite o número:  "))
        num2= 2
        num3= num1 ** num2
        print(f"{num3}")

    parada= int(input("Deseja continuar? Digite 1 para Sim e 0 para Não"))
