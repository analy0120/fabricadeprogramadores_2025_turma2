

def atendimento():
    valor_total = 0 
    raças = ['pug','pastor-alemao','labrador']
    raça= input('insira uma raça:')
    if (raça in raças):
        if (raça=='pug'):
            valor_total = valor_total + 70,99
            print(valor_total)
        elif (raça == 'pastor-alemao'):
            valor_total = valor_total + 120.99
            print(valor_total)
        elif (raça == 'labrador'):
            valor_total = valor_total + 110.99
            print(valor_total)
        else: 
            print('atendimento indisponivel')
atendimento()