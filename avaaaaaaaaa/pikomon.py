import random

pl = 45  # Pontos de vida do jogador
cl = 45  # Pontos de vida cpu

tackle = 5
bubble = 5
ember = 5
razor = 5

ataques = ["tackle", "bubble", "ember", "razor"]

pokemon = ""
p_attack = ""
c_attack = ""

c_charmander = ["tackle", "ember"]
c_squirtle = ["tackle", "bubble"]
c_bulbasaur = ["tackle", "razor"]

pokemons = ["squirtle", "charmander", "bulbasaur"]


while pokemon not in pokemons:
    pokemon = input("Escolha um dos pokemon: squirtle, charmander, bulbasaur ").lower()

pc = random.choice(pokemons)

while pl > 0 and cl > 0:
    print(f"\nO pokemon que você escolheu é o {pokemon} e o computador escolheu {pc}")
    
    
    if pokemon == "charmander" and pc == "bulbasaur":
        p_attack = input("Escolha o ataque: tackle, ember ").lower()
        if p_attack == "tackle":
            cl -= tackle
            print(f"O computador está com {cl} pontos de vida")
        elif p_attack == "ember":  
            cl -= ember * 2
            print(f"O computador está com {cl} pontos de vida")

        
        c_attack = random.choice(c_bulbasaur)
        if c_attack == "tackle":
            pl -= tackle
            print(f"Você tomou {tackle} de dano do {pc}")
        elif c_attack == "razor":  
            pl -= razor / 2
            print(f"Você tomou {razor / 2} de dano do {pc}")

    elif pokemon == "charmander" and pc == "squirtle":
        p_attack = input("Escolha o ataque: tackle, ember ").lower()
        if p_attack == "tackle":
            cl -= tackle
            print(f"O computador está com {cl} pontos de vida")
        elif p_attack == "ember": 
            cl -= ember / 2
            print(f"O computador está com {cl} pontos de vida")

        c_attack = random.choice(c_squirtle)
        if c_attack == "tackle":
            pl -= tackle
            print(f"Você tomou {tackle} de dano do {pc}")
        elif c_attack == "bubble":  
            pl -= bubble * 2
            print(f"Você tomou {bubble * 2} de dano do {pc}")

    elif pokemon == "squirtle" and pc == "charmander":
        p_attack = input("Escolha o ataque: tackle, bubble ").lower()
        if p_attack == "tackle":
            cl -= tackle
            print(f"O computador está com {cl} pontos de vida")
        elif p_attack == "bubble":
            cl -= bubble * 2
            print(f"O computador está com {cl} pontos de vida")

        c_attack = random.choice(c_charmander)
        if c_attack == "tackle":
            pl -= tackle
            print(f"Você tomou {tackle} de dano do {pc}")
        elif c_attack == "ember":  
            pl -= ember / 2
            print(f"Você tomou {ember / 2} de dano do {pc}")

    elif pokemon == "bulbasaur" and pc == "squirtle":
        p_attack = input("Escolha o ataque: tackle, razor ").lower()
        if p_attack == "tackle":
            cl -= tackle
            print(f"O computador está com {cl} pontos de vida")
        elif p_attack == "razor":  
            cl -= razor * 2
            print(f"O computador está com {cl} pontos de vida")

        c_attack = random.choice(c_squirtle)
        if c_attack == "tackle":
            pl -= tackle
            print(f"Você tomou {tackle} de dano do {pc}")
        elif c_attack == "bubble":  
            pl -= bubble / 2
            print(f"Você tomou {bubble / 2} de dano do {pc}")


if pl <= 0:
    print("Você perdeu!")
elif cl <= 0:
    print("Você ganhou!")
