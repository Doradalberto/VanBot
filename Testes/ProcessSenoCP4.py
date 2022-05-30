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
    mediaX = int((sheet[1]-resized.shape[1])/2)
    mediaY = int((sheet[0]-resized.shape[0])/2)

    #DIMINUI A QUANTIDADE DE PIXELS
    resized2 = cv2.resize(resized, (int(height/40), int(width/40)), interpolation= cv2.INTER_LINEAR)

    print('Dimensões da imagem redimensionada [px]:')
    print('H:', resized2.shape[0])
    print('W:', resized2.shape[1])
    print('')
    # print(resized2)
    print('Número de linhas:', len(resized2))
    print('')

    FreqAmp = []
    ListaX = []
    ListaY = []

    fm = 10 # Frequencia máxima
    am = 1 # Amplitude máxima

    pxtocm = 1   # Relação de 1 pixel para 1 cm
    # print(resized2)
    for e in resized2:
        for index, f in enumerate(e):
            FreqAmp.append([int(fm-((f/255)*fm)+1), (am-((f/255)*am))])
            initialX = index*pxtocm + mediaX
            initialY = index*pxtocm + (pxtocm/2)+mediaY
            # print(FreqAmp)
            
            for index2, px in enumerate(range(len(FreqAmp))):
                ListaX.append(initialX)
                ListaY.append(initialY)
                parcelaX = pxtocm/(FreqAmp[px][0])
                parcelaY = FreqAmp[px][1]/2
                print(parcelaX)
                while parcelaX <= pxtocm:

                    #Pontos em X
                    pontoX = initialX + parcelaX
                    ListaX.append(pontoX)
                    parcelaX+=parcelaX
                    
                    #Pontos em Y
                    if index2 % 2 == 0:
                         ListaY.append(initialY + parcelaY)
                    else:
                         ListaY.append(initialY - parcelaY)

    # print(len(ListaX))
    # print((ListaY))
                # ListaX.append(initialX + pxtocm/(FreqAmp[px][0] + 1))              
                # #print(pxtocm/(FreqAmp[px][0] + 1))
                # for i in range(len(FreqAmp[0])-1):
                #     if i % 2 == 0:
                #         ListaY.append(initialY + (FreqAmp[i][1]/2))
                #     else:
                #         ListaY.append(initialY - (FreqAmp[i][1]/2))
     
    # print(len(ListaX))

    plt.plot(ListaX,ListaY,'o')
    plt.show()

    # print(len(FreqAmp))
    # plt.imshow(resized2)
    # plt.show()
    return resized2


arquivo = 'Figuras/Maca.webp'

Bordas(arquivo, 'A4', 'Retrato')