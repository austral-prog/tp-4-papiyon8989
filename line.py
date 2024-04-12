import math
def line():
    

    a= float(input(""))
    b= float(input(""))
    x1= float(input(""))
    y1= float(((a * x1) + b ))
    x2= float(input(""))
    y2= float(((a * x2) + b ))

    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}\n")
    print(f"Para la siguiente ecuación:") v  
    print(f"\tY = {a}X + {b}\n")
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})\n")
    print(f"La distancia entre ellos es: {math.sqrt((x1 - x2)**2 + (y1 - y2)**2)}")
