import random

#Esse código pertence ao LEIUX, PIRATARIA PERMITIDA

def jogar():
    while True:
        jogador = input("Escolha Pedra, Papel ou Tesoura (ou 'sair' se você ta com medinho e perder): ").lower()
        if jogador == 'sair':
            print("CAGÃO!")
            break
        if jogador not in ['pedra', 'papel', 'tesoura']:
            print("Ta moscando?. Escreve certo tio.")
            continue

        computador = random.choice(['pedra', 'papel', 'tesoura'])

        print(f"Você escolheu {jogador}. O exterminador do futuro escolheu {computador}.")

        if jogador == computador:
            print("zero a zero, segue o baile")
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("UFA você ganhou!")
        else:
            print("ixi, mais sorte na próxima!")

if __name__ == "__main__":
    jogar()

    #Esse código pertence ao LEIUX, PIRATARIA PERMITIDA