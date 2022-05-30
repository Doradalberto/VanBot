# Tamanho da impressão
def tamanhoImpressao(folha, orientacao):
    if orientacao == 'Paisagem' or orientacao == 'Horizontal':
        if folha == 'A6':
            h = 105
            w = 148
        elif folha == 'A5':
            h = 148
            w = 210
        elif folha == 'A4':
            h = 210
            w = 297
        elif folha == 'A3':
            h = 297
            w = 420
        elif folha == 'A2':
            h = 420
            w = 594
        elif folha == 'A1':
            h = 594
            w = 841
        else: 
            print('ERRO: Não há esta opção disponível. Selecione entre: A1, A2, A3, A4, A5 e A6')
            print('')
    elif orientacao == 'Retrato' or orientacao == 'Vertical':
        if folha == 'A6':
            h = 148
            w = 105
        elif folha == 'A5':
            h = 210
            w = 148
        elif folha == 'A4':
            h = 297
            w = 210
        elif folha == 'A3':
            h = 420
            w = 297
        elif folha == 'A2':
            h = 594
            w = 420
        elif folha == 'A1':
            h = 841
            w = 594
        else: 
            print('ERRO: Não há esta opção disponível. Selecione entre: A1, A2, A3, A4, A5 e A6')
            print('')
    else: 
        print('ERRO: Não há esta opção disponível. Selecione entre: Paisagem, Horizontal, Retrato ou Vertical')
        print('')
        
    print('Dimensões do papel [mm]')
    print('H:', h)
    print('W:', w)
    print('')

    return h, w

def tamanhoImpressaoPX(folha, orientacao):
    if orientacao == 'Paisagem' or orientacao == 'Horizontal':
        if folha == 'A6':
            h = 1240
            w = 1748
        elif folha == 'A5':
            h = 1748
            w = 2480
        elif folha == 'A4':
            h = 2480
            w = 3508
        elif folha == 'A3':
            h = 3508
            w = 4961
        elif folha == 'A2':
            h = 4961
            w = 7016
        elif folha == 'A1':
            h = 7016
            w = 9933
        else:
            print('ERRO: Não há esta opção disponível. Selecione entre: A1, A2, A3, A4, A5 e A6')
            print('')
    elif orientacao == 'Retrato' or orientacao == 'Vertical':
        if folha == 'A6':
            h = 1748
            w = 1240
        elif folha == 'A5':
            h = 2480
            w = 1748
        elif folha == 'A4':
            h = 3508
            w = 2480
        elif folha == 'A3':
            h = 4961
            w = 3508
        elif folha == 'A2':
            h = 7016
            w = 4961
        elif folha == 'A1':
            h = 9933
            w = 7016
        else:
            print('ERRO: Não há esta opção disponível. Selecione entre: A1, A2, A3, A4, A5 e A6')
            print('')
    else:
        print('ERRO: Não há esta opcão disponível. Selecione entre: Paisagem, Horizontal, Retrato ou Vertical')
        print('')

    print('Dimensões do papel [px]')
    print('H:', h)
    print('W:', w)
    print('')
    
    return h, w
