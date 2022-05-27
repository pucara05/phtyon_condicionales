#hacer un ejercicio que lea 3 numeros y determine cual es el mayor de ellos
# cual es el del medio y cual es el menor

num1=float(input("digite el numero 1: "))
num2=float(input("digite el numero 2: "))
num3=float(input("digite el numero 3: "))

if num1==num2 or num1==num3 or num2==num3:
        print("hay dos o mas numeros iguales. cambielos")
else:

if num1>=num2:
    if num1>num3:
     print("el mayor es el numero 1", num1)
    if num2>num3:
        print("el del medio es el num 2", num2)
        print("el menor es el numero 3", num3)
    else:
    print("el del medio es el numero 3: ", num3)
    print("el menor es el numero 2", num2)
    
  else:
        print("el mayor es el numero 3", num3)
        print("el del medio es el numero 1", num1)
        print("el menor es el numero 2", num2)

else:
    if num2>num3:
        print("el mayor es el numero 2", num2)
        if num1>num3:
            print("el del medio es el numero 1", num1)
            print("el menor es el numero 3", num3)
        else:
            print("el mayor es el numero 3", num3)
            print("el del medio es el numero 2", num2)
            print("el menor es el numero 1", num1)
