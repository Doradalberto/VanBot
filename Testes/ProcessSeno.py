import matplotlib.pyplot as plt
import CalculaTamanhoImpressao as tam
import cv2
import numpy as np

def Seno(valor):
    pontos = []
    if valor > 245:
        lista = []

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
    
    resized = cv2.resize(figgray, (width, height), interpolation= cv2.INTER_LINEAR)

    # cut = figure[y:y+h, x:x+h]
    # to fit the picture in the middle:
    mediaX = int(sheet[1]-resized.shape[1])/2
    mediaY = int(sheet[0]-resized.shape[0])/2

    #DIMINUI A QUANTIDADE DE PIXELS
    resized2 = cv2.resize(resized, (int(height/20), int(width/20)), interpolation= cv2.INTER_LINEAR)
    # resized2 = cv2.resize(resized, (h,w), interpolation=cv2.INTER_LINEAR)
    print('Dimensões da imagem redimensionada [px]:')
    print('H:', resized2.shape[0])
    print('W:', resized2.shape[1])
    print('')

    m = 5

    n_linhas = int(resized.shape[0]/m)
    print('Número de linhas:', n_linhas)
    print('')

    listaLinhas = []
    print(len(resized))

    ListaX = []
    ListaY = []
    Freq = []
    Amp = []
    fm = 10 # Frequencia máxima
    am = 10 # Amplitude máxima

    for e in resized:
        for f in e:
            Freq.append([int(fm-((f/255)*fm))])
            Amp.append([int(am-((f/255)*am))])
        
    print(Freq)

    return resized2

def Processa(imagem):
    print(imagem)
    (h,w) = imagem.shape

    print('Tamanho imagem original [px]:')
    print('H:', h)
    print('W:', w)
    print('')
    
    resized = cv2.resize(imagem, (int(height/20), int(width/20)), interpolation= cv2.INTER_LINEAR)
    # resized2 = cv2.resize(resized, (h,w), interpolation=cv2.INTER_LINEAR)
    print('Tamanho imagem redimensionada [px]:')
    print('H:', resized.shape[0])
    print('W:', resized.shape[1])
    print('')

    m = 5

    n_linhas = int(resized.shape[0]/m)
    print('Número de linhas:', n_linhas)
    print('')

    listaLinhas = []
    print(len(resized))

    ListaX = []
    ListaY = []
    Freq = []
    Amp = []
    fm = 10 # Frequencia máxima
    am = 10 # Amplitude máxima

    for e in resized:
        for f in e:
            Freq.append([int(fm-((f/255)*fm))])
            Amp.append([int(am-((f/255)*am))])
        
    print(Freq)


    return resized

arquivo = 'Figuras/Maca.webp'
figura = Bordas(arquivo, 'A4', 'Retrato')
# plt.imshow(Processa(arquivo), cmap='gray')
# plt.show()

Processa(figura)