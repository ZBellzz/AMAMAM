
def calculadora():    
    while True:
    
        operacao = input("digite o operador que deseja: (+, -, /, *) ou digite 'sair' para encerrar ")
        if operacao.lower() == "sair":
            print("Calculadora encerrada")
            break



        n1 = float(input("Digite o valor 1 "))
        n2 = float(input("Digite o valor 2 "))

        if operacao == "+":
            r = n1 + n2
            print(r)

        elif operacao == "-":
            r = n1 - n2 
            print(r)

        elif operacao == "/":
            r = n1 / n2
            print (r)

        elif operacao == "*":
            r = n1 * n2
            print(r)

        else:
            print("Erro, algo esta errado ")



escolhas = input("escolha q calculadora 'sim' ou 'n'")

if escolhas == "sim":

    calculadora()
        
else:
    print("gay")


