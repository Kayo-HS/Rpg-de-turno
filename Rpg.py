from random import randint


classes = {
    "Berserk":{
    "HP" : 150, 
    "Ataque" : 100,
    "Esquiva" : 70, 
    "Defesa" : 60
}, 
    "Espadachim":{
    "HP" : 100, 
    "Ataque" : 120,
    "Esquiva" : 80, 
    "Defesa" : 70
}, 
    "Paladino": {
    "HP" : 120, 
    "Ataque" : 120,
    "Esquiva" : 60, 
    "Defesa" : 90
}


}
print(
    "ESCOLHA COM SABEDORIA"
    "\n[0] Berserk"
    "\n[1] Espadachim"
    "\n[2] Paladino"
)


escolhaClasse = (int(input("Qual classe deseja?")))
if 0<= escolhaClasse <= 2:
    if escolhaClasse == 0:
        classeJogador = "Berserk"
        escolhaClasse = classes["Berserk"]
    elif escolhaClasse == 1:
        classeJogador = "Espadachim"
        escolhaClasse = classes["Espadachim"]        
    else: 
        classeJogador = "Paladino"
        escolhaClasse = classes["Paladino"]
    
    computador = randint(0,2)
    classesNomes = list(classes.keys())
    classesComputador = classesNomes[computador]
    escolhaComputador = classes[classesComputador]    

     
    


    print("-=-"*10)
    print(f"Jogador escolheu {classeJogador}")
    print(f"O computador escolheu {classesComputador}")
    print("-=-"*10)

    # print(escolhaClasse["HP"])
    # print(escolhaComputador["HP"])
    if escolhaClasse["HP"] < 0 and escolhaComputador["HP"] < 0:
        while True:
            jogaprimeiro = randint(0,1)

            if jogaprimeiro == 0:
                print("Jogador vai primeiro")
                acaoJogador = int(input("Escolha com sabedoria:"))
                print
                ("[0] Ataque" 
                 "[1] Defesa"
                 "[2] Esquiva")
                if acaoJogador == 0:
                    acaoDano = randint(0,escolhaClasse["Ataque"])
                    danoDado = escolhaComputador["HP"] - acaoDano
                    print (danoDado)

    elif escolhaClasse["HP"] == 0:
        print("Jogador perdeu")
    elif escolhaComputador["HP"] == 0:
        print("Oponente perdeu")
else:
    print("Ação invalida.")
