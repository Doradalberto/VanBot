import cv2
import numpy as np
import matplotlib.pyplot as plt
import CalculaTamanhoImpressao as tam

def Bordas(arquivo, folha, orientacao, margem):
    # arquivo = "imagem.png"
    print('Folha:',folha)
    print('Orientacao:',orientacao)
    print('')

    fig = cv2.imread(arquivo, cv2.IMREAD_COLOR)
    figRGB = cv2.cvtColor(fig, cv2.COLOR_BGR2RGB)
    sheet = tam.tamanhoImpressaoPX(folha, orientacao)
    comBorda = cv2.copyMakeBorder(figRGB, margem, margem, margem, margem, cv2.BORDER_CONSTANT, None, value = (255,255,255))
    
    PropPapel = sheet[1]/sheet[0]
    PropFig = figRGB.shape[1]/figRGB.shape[0]

    if PropPapel <= PropFig:
        height = int((figRGB.shape[0]/figRGB.shape[1]) * sheet[1])
        width = int(sheet[1])
    else:
        height = int(sheet[0])
        width = int((figRGB.shape[1]/figRGB.shape[0]) * sheet[0])
    
    print('Dimensoes da imagem [px]')
    print('H:', height)
    print('W:', width)
    
    resized = cv2.resize(figRGB, (width, height), interpolation= cv2.INTER_LINEAR)

    # cut = figure[y:y+h, x:x+h]
    # to fit the picture in the middle:
    mediaX = int(sheet[1]-resized.shape[1])/2
    mediaY = int(sheet[0]-resized.shape[0])/2

    if PropPapel <= PropFig:
        padding = cv2.copyMakeBorder(resized, int(mediaY), int(mediaY), 0, 0, cv2.BORDER_CONSTANT, None, value = (255,255,255))
    else:
        padding = cv2.copyMakeBorder(resized, 0, 0, int(mediaX), int(mediaX), cv2.BORDER_CONSTANT, None, value = (255,255,255))
    # plt.imshow(padding)
    # plt.show()
    return padding

arquivo = 'VanBot/Bonito.png'
folha = 'A4'
orientacao = 'Paisagem'
margem = 1000
plt.imshow(Bordas(arquivo, folha, orientacao, margem))
plt.show()



