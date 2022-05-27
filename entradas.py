#hacer un programa que lea el nombre de un estudiante, lea 3 notas
#y calcule la definitiva. imprima  el nombre y la definitiva


nombre=str(input("diguite el nombre del estudiante : "))
nota1=float(input("diguite la nota 1: "))
nota2=float(input("diguite la nota2: "))
nota3=float(input("diguite la nota3: "))
definitiva=(nota1+nota2+nota3)/3
print("el nombre del estudiante es: " + nombre)
print("la definitiva del estudiante es: " + str(definitiva)) # str convierte la definitiva en una cadena para poder visualizarlo
# otro modo es print("el nombre de la definitiva es: " , nombre)
# o otro metodo es print("la definitiva del estudiante es: " , definitiva)
#otro modo es print("el nombre de la definitiva es: " + nombre + " la definitiva del estudiante es:" + str(definitiva))
 
 
            
            