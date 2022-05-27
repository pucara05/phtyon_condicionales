#hacer un programa que lea tres calificaciones de un estudiante y
#calcule su definitiva.
#si la definitiva es mayor a 4.5 debe imprimir "sobresaliente"
#si la definitiva es mayor a 4 debe imprimir "excelente"
#si la definitiva es mayor a 3 debe imprimir "regular"
#si la definitiva es menor a 3 debe imprimir "deficiente"


nota1=float(input("digite la nota1: "))
nota2=float(input("digite la nota2: "))
nota3=float(input("digite la nota3: "))
definitiva=(nota1+nota2+nota3)/3

if definitiva>4.5:
    print("su definitiva es: ", definitiva, " por lo tanto es sobresaliente")
elif definitiva>=4:
    print("su definitiva es: ", definitiva, " por lo tanto es excelente")
elif definitiva>=3:
     print("su definitiva es: " , definitiva, " por lo tanto es regular")
else:
     print("su definitiva es: " , definitiva, " por lo tanto es deficiente")
