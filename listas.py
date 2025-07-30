import math
def equaçao():
    a = float(input("insira o valor de A: "))
    b = float(input("insira o valor de B: "))
    c = float(input("insira o valor de C: "))
    delta = b**2 -4 * a * c 
    if delta >=0:
        #calculo da raiz real
        x = (-b +math.sqrt(delta))/2* a
        y = (-b -math.sqrt(delta))/2* a
        print("o resultado e ", x,y)
    else:
        print('''essa equaçao nao possui
               raizes reais''')
#equaçao()   
import random

animais_aleatorio = ["lobo",'macaco','joaninha','borboleta','aranha','jacu','passaro','gato','pato','galinha']
print(random.choice(animais_aleatorio))

import this0. 