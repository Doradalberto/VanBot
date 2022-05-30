import matplotlib.pyplot as plt
import CalculaTamanhoImpressao as tam
import cv2
import numpy as np
import json

# NewFig = []

def ZigZag(lista):
    NewFig = []
    for index, e in enumerate(lista):
        if index % 2 == 0:
            NewFig.append(e)
        else:
            NewFig.append(e[::-1])
    print(NewFig)
    cv2.imwrite('Figuras/Inversa.png', NewFig)  
    print('ok')
    # plt.imshow(NewFig)
    # plt.show()
    # foto = json.dumps(NewFig)
    # with open('D:/Documentos/OneDrive - Insper - Institudo de Ensino e Pesquisa/7 Semestre/Visão de Máquina/VanBot/valor.json','w') as fh:
        # fh.write(foto)

    # print(NewFig)



def Bordas(arquivo, folha, orientacao):
    print('')
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
    
    print('Dimensões da imagem [px]')
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

    print('Número de pixels:', resized2.shape[0]*resized2.shape[1])
    print('')
    
    Freq   = []
    Amp    = []
    ListaX = []
    ListaY = []
    novoX = []
    novoY =[]
    listaK = []

    fm = 10 # Frequencia máxima
    am = 1 # Amplitude máxima

    pxtocm = 1   # Relação de 1 pixel para 1 cm

    ZigZag(resized2)
    
    # for index0, e in enumerate(resized2): #INDEX0 = 0 ATÉ N° DE LINHAS, e = [],[],[]
        
    #     for index, f in enumerate(e):     #INDEX = 0 ATÉ N° DE COLUNAS, f = valores de cada pixel
    #         Freq = int(fm-((f/255)*fm)+1)
    #         Amp = am-((f/255)*am)
    #         initialX = index*pxtocm + mediaX
    #         initialY = index*pxtocm + (pxtocm/2)+mediaY

    #         ListaX.append(initialX)
    #         ListaY.append(initialY)
            
    #         parcelaX = pxtocm/Freq
    #         parcelaY = Amp/2

    #         while parcelaX <= pxtocm:
    #             #Pontos em X
    #             pontoX = initialX + parcelaX
    #             ListaX.append(pontoX)
                
    #             #Pontos em Y
    #             if index % 2 == 0:
    #                     ListaY.append(initialY + parcelaY)
    #             else:
    #                     ListaY.append(initialY - parcelaY)
    #             parcelaX += parcelaX

    #     if index0 > 1:
    #         break
    # # print(Freq)
    # print(len(ListaX))

    # # # print('Número de pontos:', len(ListaX))
    # # # print('')
    # # print((listaK))
    # plt.plot(ListaX,ListaY,'o')
    # plt.show()

    return resized2


arquivo = 'Figuras/Maca.webp'

Bordas(arquivo, 'A4', 'Retrato')