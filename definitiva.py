#hacer un programa que calcule la definitiva de un estudiante asi:
#leer 3 notas de quizes las cuales valen el 40%
#leer 2 notas de trabajos los cuales valen el 25%
#leer 1 nota de parcial el cual vale el 35%

quiz1=float(input("diguite la nota de quiz 1: "))
quiz2=float(input("diguite la nota de quiz 2: "))
quiz3=float(input("diguite la nota de quiz 3: "))
definitivaQuiz=(quiz1+quiz2+quiz3)/3 *0.40

trabajo1=float(input("diguite la nota del trabajo 1: "))
trabajo2=float(input("diguite la nota del trabajo 2: "))
definitivaTrabajo=((trabajo1+trabajo2)/2)*0.25

parcial=float(input("diguite la nota del parcial: "))
definitivaParcial=parcial*0.35

definitiva=definitivaQuiz+definitivaTrabajo+definitivaParcial

print("la nota definitiva del estudiante es: ", definitiva)
