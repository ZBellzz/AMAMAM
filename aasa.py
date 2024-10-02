
"""
            atv 96


 def area (altura, largura ):
    r = a * l 
    print("o resultado da area é :{}".format(r))


def pontos ():
    print("-" * 30)



pontos()
print("controle de terreno")
pontos()
a = float(input("Digite a altura "))
l = float(input("Digite o largura "))
     
area(a,l)


 """



'''
        desafio 97


def traco ():
    print("-" * contador  )
    print (frase)    
    print("-" * contador  )





frase = input(" Digite uma frase  ")
contador = len (frase)
traco()
'''




def calculadora():
    while True:
        try:
            # Solicita a operação
            operacao = input("Escolha uma operação (+, -, *, /) ou 'sair' para encerrar: ")
            if operacao.lower() == 'sair':
                print("Calculadora encerrada.")
                break
            
            # Solicita os números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Realiza o cálculo
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero.")
                    continue
                resultado = num1 / num2
            else:
                print("Operação inválida. Tente novamente.")
                continue

            # Exibe o resultado
            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
        
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

# Chama a função da calculadora
calculadora()