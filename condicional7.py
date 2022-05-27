# hacer un programa para calcular una persona que debe ser mayor de 18 años
# y tener unos ingresos iguales o superiores a 2.000.000 mensuales
#preguntar al usuario la edad y los ingresos y determine si debe pagar impuestas si o no

edad=int(input("digite su edad: "))
ingresos=float(input("digite sus ingresos"))

if edad>=18 and ingresos>=2000000:
    print("eres mayor de edad puedes pagar tus impuestos")
    
elif edad>=18 and ingresos<2000000:
    print("eres mayor de edad pero no tienes como pagar")
else:
        print("no eres mayor de edad no puedes pagar")
