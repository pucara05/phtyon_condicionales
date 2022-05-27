#hacer un ejercicio que lea 3 numeros y determine cual es elmayor de ellos

num1=float(input("digite su numero 1: "))
num2=float(input("digite el numero 2: "))
num3=float(input("digite el numero 3: "))

if num1>num2:
    if num1>num3:
        print("el numero 1 es el mayor", num1)
    else:
        print("el numero 3 es el mayor", num3)
else:
        if num2>num3:
            print("el numero 2 es el mayor", num2)
        else:
            print("el numero 3 es el mayor", num3)
            
    
