import matplotlib.pyplot as plt
import CalculaTamanhoImpressao as tam
import cv2
import numpy as np

def Bordas(arquivo, folha, orientacao):
    print('Folha:',folha)
    print('Orientacao:',orientacao)
    print('')

    fig = cv2.imread(arquivo, cv2.IMREAD_COLOR)
    figgray = cv2.cvtColor(fig, cv2.COLOR_BGR2GRAY)
    sheet = tam.tamanhoImpressaoPX(folha, orientacao)

    PropPapel = sheet[1]/sheet[0]
    PropFig = fig.shape[1]/figgray.shape[0]

    if PropPapel <= PropFig:
        height = int((figgray.shape[0]/figgray.shape[1]) * sheet[1])
        width = int(sheet[1])
    else:
        height = int(sheet[0])
        width = int((figgray.shape[1]/figgray.shape[0]) * sheet[0])
    
    print('Dimensoes da imagem [px]')
    print('H:', height)
    print('W:', width)
    print('')
    
    resized = cv2.resize(figgray, (width, height), interpolation= cv2.INTER_LINEAR)

    # to fit the picture in the middle:
    mediaX = int(sheet[1]-resized.shape[1])/2
    mediaY = int(sheet[0]-resized.shape[0])/2

    #DIMINUI A QUANTIDADE DE PIXELS
    resized2 = cv2.resize(resized, (int(height/40), int(width/40)), interpolation= cv2.INTER_LINEAR)

    print('Dimensões da imagem redimensionada [px]:')
    print('H:', resized2.shape[0])
    print('W:', resized2.shape[1])
    print('')

    print('Número de linhas:', len(resized2))
    print('')

    FreqAmp = []

    fm = 1 # Frequencia máxima
    am = 1 # Amplitude máxima

    pxtocm = 1   # Relação de 1 pixel para 1 cm

    #POSICAO INICIAL
    # ListaX.append([index + mediaX])
    # ListaY.append([index + (pxtocm/2) + mediaY])

    for e in resized2:
        for index, f in enumerate(e):
            FreqAmp.append([(fm-((f/255)*fm)), (am-((f/255)*am))])
            initialX = [index + mediaX]
            initialY = [index + (pxtocm/2) + mediaY]
            
            for index2, px in enumerate(range(len(FreqAmp))):
                print(FreqAmp[px][0]*index2)
                # ListaX.append(initialX + (1/FreqAmp[px][0])*index2)
                # ListaX.append(initialX + (1/FreqAmp[0])*index2)
                

                # for i in range(len(FreqAmp[0])):
                   
                #     if i % 2 == 0:
                #         ListaY.append(initialY + (FreqAmp[1]/2)/100)
                #     else:
                #         ListaY.append(initialY - (FreqAmp[1]/2)/100)
        
    print(len(FreqAmp))
    plt.imshow(resized2)
    plt.show()
    return resized2


arquivo = 'Figuras/Maca.webp'

Bordas(arquivo, 'A4', 'Retrato')