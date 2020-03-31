import random
caixa = 100
jogando = True
while caixa > 0 and jogando == True:
    print('Você tem {} dinheiros'.format(caixa))
    aposta = int(input('Aposte uma valor: '))
    if aposta != 0:
        tipo = input('Número ou paridade: ')
        sorteado = random.randint(0,36)
        if tipo == 'n':
            jogo = int(input('Digite um número de 1 a 36: '))
            if jogo == sorteado:
                print('Você ganhou')
                caixa += 35*aposta
            else: 
                print('Você perdeu')
                caixa -= aposta
        if tipo == 'p':
            jogo = input('Digite uma paridade: ')
            if sorteado%2 == 0:
         	    resultado = 'p'
            else:
                resultado = 'i'
            if jogo == resultado:
                caixa += aposta
                print('Você ganhou')
            else:
                caixa -= aposta
                print('Você perdeu')
    else:
        jogando = False
print('Perdeu tudo')