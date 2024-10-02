""" 
        Desafio 2   

n1 = int(input("Deposite o primeiro numero "))
n2 = int(input("Deposite o segundo numero "))

if n1 % 2 == 0 or n2 % 2  == 0:
    print("ERRO numero digitado é par")

else: 
    r = n1 + n2
    print("o Resultado da soma dos {}, {} resulta em {}".format(n1, n2, r)) """

""" 
        Desafio 1

nm1 = int(input("Digite o primeiro numero "))
nm2 = int(input("Digite o segundo  numero "))

operacao = input("DIgite a operação ")
controle = 0
c2 = 0


if operacao == "+":
    r = nm1 + nm2 
    print(r)

elif operacao == "-":
    r = nm1 - nm2
    print(r)

elif operacao == "*":
    while controle != nm2:
        c2 = nm1 + c2
        controle = controle + 1

    print(c2)

elif operacao == "/":

    if nm2 == 0:
        print("ERRO: Divisão por zero não é permitida")
    else:
        
        while nm1 >= nm2:
            nm1 -= nm2
            controle += 1
        print("O resultado da divisão usando subtração é {}".format(controle))

else:
    print("erro")
 """

""" atividade 2 """

#1
""" 
a = int(input("DIgite o valor 1"))

if a %2 == 0:
    print("verdadeiro")
else:
    print("Falso") """








def calculadora():
    while True:     
        operacao = input("escohas quale das operetion a seguir desejas( +, -, /, * ) caso deseja sair utilize 'puta' ")
        if operacao == "puta":
            linhasb()
            print("Saindooooooo ")
            linhasb()
            break

        n1 = float(input("DIgite o primeiro valor "))
        n2 = float(input("digite o segundo valor "))


        if operacao == "+":
            r = n1 + n2
            print("Resultado é {}".format(r))

        if operacao == "-":
            r = n1 - n2
            print("Resultado é {}".format(r))

        if operacao == "*":
            r = n1 * n2
            print("Resultado é {}".format(r))

        if operacao == "/":
            if n2 == 0:
                print("Erro, n pode ser dividido por 0")


            else:
                r = n1 / n2
                print("Resultado é {}".format(r))

        else: 
            print("erro, tente novamente")


def linhasg():
    print("-" * 50 )


def linhasb():
    print("-" * 13 )






escolhas = input("desejas usares a calcu? 'sin'or'no'?  ")
if escolhas == "sin":
    calculadora()


else:
    linhasg()
    print("viado do krlh, vai chupar um canavial de rola")
    linhasg()




 


