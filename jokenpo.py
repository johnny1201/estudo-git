from random import randint
from time import sleep
jogador = 3
print('''Escolha sua jogada:
        [0] Pedra
        [1] Papel
        [2] Tesoura
        [9] Encerrar''')
opcoes = ('Pedra', 'Papel', 'Tesoura')
vitoria = 0
derrota = 0
empates = 0
while jogador != 9 :
    jogador = int(input('Sua escolha: '))
    pc = randint(0, 2)
    if jogador == 9:
        break
    print('---'*10)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    if 0 <= jogador <= 2: 
        if pc == 0 :
            if jogador == 0:
                resultado = 'EMPATE'
                empates += 1
            elif jogador == 1:
                resultado = 'Jogador VENCEU'
                vitoria += 1
            else: 
                resultado = 'Jogador PERDEU'
                derrota += 1
        elif pc == 1:
            if jogador == 0:
                resultado = 'Jogador PERDEU'
                derrota += 1
            elif jogador == 1:
                resultado = 'EMPATE'
                empates += 1
            else :
                resultado = 'Jogador VENCEU'
                vitoria += 1
        elif pc == 2:
            if jogador == 0:
                resultado = 'Jogador VENCEU'
                vitoria += 1
            elif jogador == 1:
                resultado = 'Jogador PERDEU'
                derrota += 1
            else : 
                resultado = 'empate'
                empates += 1
        print('PC escolheu {}'.format(opcoes[pc]))
        print('Jogador escolheu {}'.format(opcoes[jogador]))
        print('---'*10)
        print('***{}***'.format(resultado))
        print('---'*10)
    else:
        print('Jogada INVÁLIDA')
        print('''Escolha sua jogada:
        [0] Pedra
        [1] Papel
        [2] Tesoura
        [9] Encerrar''')

    
    
