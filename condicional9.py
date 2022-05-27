#hacer un programa que tenga en cuenta los rangos impositivos
#para la declaracion de renta:
#menos de 1000.0000 millones 5%
#entre 1000.000 y 20.000.000 15%
#entre 20.000.000 y 35.000.000 20%
#entre 35.000.000 y 60.000.000 30%
#mas de 60.000.000 45%
# el usuario debe digitar su renta anual y muestre por pantalla
#el tipo impositivo y el valor a pagar

renta=float(input("digite la renta anual: "))
if renta<10000000:
    tipo="5%"
    valorPagar=renta*0.05
elif renta<20000000:
        tipo="15%"
        valorPagar=renta*0.15
elif renta<35000000:
            tipo="20%"
            valorPagar=renta*0.20
elif renta<60000000:
                tipo="30%"
                valorPagar=renta*0.30
else:
     tipo="45%"
     valorPagar=renta*0.45
     #mostrar por pantalla
     print("renta es: ",renta, "el tipo es de: ", tipo, "el valor a pagar es de: ", valorPagar)
    
