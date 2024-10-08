# numero par ou impar

# numero = int(input("DIgite o numro "))


# if numero % 2 == 0:
#     print("o numero é par ")

# else:
#     print("o numero é impar")


# calculo com desconto

# valor = float(input("Digite o valor "))

# if valor < 100:
#     print("o Valor é de {}".format(valor))

# else:
#     desconto = (valor * 10)/100
#     valor = valor - desconto
#     print("o valor do produto é de: {}".format(valor))




# calculo de media


# nota1 = float(input("Digite a nota 1 "))
# nota2 = float(input("Digite a nota 2 "))
# nota3 = float(input("Digite a nota 3 "))


# r = (nota1 + nota2 + nota3) /3


# if r >= 7:
#     print(" Aprovado{}".format(r))

# else:
#     print("reprovado{}".format(r))


#     aumento de salario

# salario = float(input("Digite o seu salario "))


# if salario < 1500:
#     aumento = salario * 20 / 100
#     salario = salario + aumento
#     print("Seu salario foi para{}".format(salario))


# else:
#     aumento = salario * 10 / 100
#     salario = salario + aumento
#     print("Seu salario foi para{}".format(salario))


# verificar se sao enguals

# nm1 = float(input("Digite o primeiro valor "))
# nm2 = float(input("Digite o segundo  valor "))

# if nm1 == nm2:
#     print("os numeros sao enguas")

# else:
#     print("Os numeros sao diferentes")


# autentificar usuario

# user = "Bell"
# password = 277353

# nome = input("Digite o usuario ")
# senha = float(input("Digite a senha "))

# if user == nome:
#     if password == senha:
#         print("Login bem sucedido")
#     else:
#         print("login negado")
# else:
#     print("Login negado")


#    validar estabelecimento fechado ou aberto

# semana = ["segunda","terca", "quarta","quinta", "sexta"]

# hora = float(input("DIgite o seu horario "))
# dia = input("Digite os dia da semana ").lower()



# if dia in semana:
#     if (hora >= 8) and (hora <=18):
#         print ("Esta aberto")

#     else:
#         print("Está fechado")

# else:
#     print("está fechado")


# validar se é um triangulo

# n1 = float(input("valor nm 1 "))
# n2 = float(input("valor nm 2 "))
# n3 = float(input("valor nm 3 "))


# if n1 + n2 >  n3:
#     print("é um triangulo")

# else: 
#     print("Nao é um triangulo")


# conferir ano bisexo

# ano = int(input("DIgite o ano "))

# if (ano % 4 == 0) and (ano % 100 != 0 ) or (ano % 400 == 0):
#     print("é um ano bisexo")

# else:
#     print("Não é um ano bisexo")


# verificar temperatura

# temp = float(input("Digite a temperatura "))

# if  temp < 15:
#     print("está frio")

# elif (temp >= 15) and (temp <= 30):

#     print("O clima está ameno ")


# else:
#     print("Está quented")


# classificaçao de velocidade

# velo = float(input("iforme a velocidade"))

# if velo <= 80:
#     print("está no limite de velocidade")

# elif (velo >80) and (velo <=100):
#     print("Está acima da velocide")

# else:
#     print("está muito acima da velocidade")


# classificação de triangulo 

# lado1 = float(input("DIgite o lado 1"))

# lado2 = float(input("DIgite o lado 2"))

# lado3 = float(input("DIgite o lado 3"))


# if lado1 + lado2 > lado3 and lado1 + lado3 >lado2 and lado2 + lado3 > lado1:
#     print("Não é um triangulo")

# elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
#     print("O triangulo é equilatero")

# elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: 
#     print("O triangulo é isosceles")

# else:
#     print("È escaleno") 


#  Cálculo de Aumento Salarial com Faixas

# salario = float(input("Digite o salario"))

# if salario <= 1000:
#     salario = salario * 0.2 + salario 
#     print("O salario foi para : {}".format(salario))


# elif salario <= 3000:
#     salario = salario * 0.15 + salario
#     print("O salario foi para : {} ".format(salario))

# else:
#     salario = salario * 0.1 + salario
#     print("O salario foi para : {}".format(salario))


# nota1 = float(input("Digite a nota1 "))
# nota2 = float(input("Digite a nota2 "))
# nota3 = float(input("Digite a nota3 "))




# if nota1 < 3  or nota2 < 3 or nota3 < 3:
#     print("Reprovado !!")


# else: 
#     media = (nota1 + nota2 + nota3) / 3
    
#     if media < 5:
    
#         print("Reprovado !!")

#     elif media < 7:
#         print("Recuperação ")

#     else:
#         print("Aprovado ")


# Calculo de Imposto de Renda


# salario = float(input("Digite o salario"))


# if salario < 1900:
#     print("Isento de imposto")


# elif salario <= 2800:
#     salario = salario * 0.075
#     print("O imposto vai ser de : {}".format(salario))

# elif salario <= 3700:
#     salario = salario * 0.15
#     print("O imposto vai ser de : {}".format(salario))


# else:
#     salario = salario * 0.225
#     print("O imposto vai ser de : {}".format(salario))


# Verificação de Ano Escolar

# idade = int(input("Digite a idade"))

# if idade <4 or idade >17:
#     print("Fora da educação regular")

# if idade <6:
#     print ("pre escola")

# if idade < 11:
#     print("Ensino Fundamental I")

# if idade <15:
#     print("Ensino Fundamental II")

# if idade < 18:
#     print("Ensino Medio")



# jogo jokenpo


# import random

# joga = input("Digite 'pedra, papel ou tesoura ' ").lower()

# jokenpo = ["pedra", "papel", "tesoura"]


# sort = random.choice(jokenpo)

# if (joga =="pedra" and sort == "tesoura") or (joga =="tesoura" and sort == "papel") or (joga =="papel" and sort == "pedra"):
#     print("Parabens, voce escolheu {} e o pc escolheu {}".format(joga, sort))

# elif (joga == sort):
#     print("empate")

# else:
#     print("Voce perdeu, o pc escolheu {} e voce escolheu {}".format(sort, joga))


# # contagem regressiva


# # contador


# import time


# contador2 = int(input("Digite o segundo valor "))

# # c é uma variavel| range de contagem, pode por variaveis| um terceiro numero seria intervalo entre a contagem

# for c in range(0, contador2 + 1):
    
#     print(c)
#     #time.sleep para tempo de espera apos executar o de cima
#     time.sleep(2)
# print("BOOOOOOOOM")








