alto=float(input( ))
ancho=float(input( ))
profundo=float(input( ))
volumen=alto*ancho*profundo
costo=volumen*5
if alto>30:
    costo=costo+2000
if costo>10000:
     iva=costo*0.19
     costo=costo+iva
print(float(volumen))
print(float(costo))

