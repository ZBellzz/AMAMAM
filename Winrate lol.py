def lol():
        
        
        vitoria = int(input("Digite o numeros de partidas ganhas "))
        derrotas = int(input("Digite o numero de derrotas "))

        game = vitoria + derrotas

        r = (vitoria / game) * 100 

        resu = ("O resultado do seu WINRATE é de : {}%".format(r))
        resu2 = len(resu)

        def lin():
            print("-" * resu2)

        lin()
        print(resu)
        lin()


def linha ():
    print("-" * title2)


while True:

    title = (" WINRATE LEAGUE OF LEGENDS ")
    title2 = len(title)

    linha()
    print(title)
    linha()

    decisao = input("Deseja continuar? para continuar digite 'si' para parar digite 'no'  ")

    if decisao == "si":
        lol()

    elif decisao == "no":
    
        print("sessao encerrada")
        break
    
    else:
         print("Error, comando nao valido")
         lol()
