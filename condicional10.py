#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
#traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
#A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
#La cantidad de dinero conseguida en cada nivel es de 2.400.000 multiplicada por la puntuación del nivel.
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
#Nivel	Puntuación
# Inaceptable  0.0
# Aceptabe    0.4
# Meritorio   0.6 o más
#escribir el programa que lea la puntuacion del usuario
# e indique su nivel de
# rendimiento, asi la cantidad de dinero que reciba el usuario.

bonificacion=2400000
puntos=float(input("digite su puntuacion: "))
if puntos==0.0:
    nivel="inaceptable"
    ingreso=puntos*bonificacion
elif puntos==0.4:
    nivel="aceptable"
    ingreso=puntos*bonificacion
elif puntos>=0.6:
    nivel="meritorio"
    ingreso=puntos*bonificacion
    print("tu nivel de rendimiento es: ", nivel)
    print("tu ingreso adicional es de: ", ingreso)
    



