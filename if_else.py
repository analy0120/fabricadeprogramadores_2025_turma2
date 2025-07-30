"""
saldo = int(input("digite o saldo bancario"))
saque = int(input("digiteo valor do saque"))

if saldo >= saque:
    saldo -= saque
    print ("voce realizou um saque com sucesso.", saldo)
else:
    print("voce nao pussui saldo para realizar essa operaçao.", saldo)
"""
"""
nome = input("digite o nome do aluno")
nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
media = (nota1+nota2)/2
if media >= 6 and media <=7:
    print("o aluno ",nome ,"foi aprovado com a nota" , media)
elif media >= 8:
    print("o aluno ",nome ,"foi aprovado com louvor com a nota" , media)
else:
    print("o aluno",nome, "foi reprovado com a nota" , media)

"""
valor_parte = float(input("insira o valor parte:"))
porcentagem= float(input("insira o valor da porcentagem"))
if porcentagem <=0.0:
    print("insira um valor maior que zero.")
else:
    valor_total = valor_parte * (porcentagem/100)
    print(valor_total)
