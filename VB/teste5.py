import matplotlib.pyplot as plt
import numpy as np
import math
import cv2
from regex import P

def seno(freq, amp, x0, y0, direction):
	xi = [0.0, math.pi*0.5, math.pi*1.5]
	x = []
	y = []
	for i in range(0, freq):
		for j in xi:
			if (j != 0 and i > 0) or (i == 0):
				yi = math.sin(j)
				x.append(x0 + (j + i*2*math.pi)/(freq*2*math.pi))
				y.append(y0 + yi * amp/2)

	x = x[::direction]
	y = y[::direction]
	return x, y

def Calculos(Freq_max, Amp_max, len_y, len_x, img):
    x = []
    y = []
    divx = [[] for i in range(0, len_y - 1)]
    divy = [[] for i in range(0, len_y - 1)]

    print(divx)

    for i in range(0, len_y - 1):
        # print(i)

        for j in range(0, len_x - 1):
            freq = int(Freq_max - (img[i,j]/255)*Freq_max + 1) # SOMAR +1 PARA TER FREQUENCIA MÍNIMA DE 1
            amp = (Amp_max - (img[i,j]/255)*Amp_max)
            direction = 1
            xi, yi = seno(freq, amp, j, i, direction)
            x = np.hstack((x, xi))
            y = np.hstack((y, yi))

            if (j == len_y-1):
                divx[i].append(x)
                divy[i].append(y)
    # divx = np.hstack(divx)
    # divy = np.hstack(divy)

    print(divx)
    
    lx = []
    ly = []

    for index in range(len(divx)):
        
        if (index % 2 == 0) or (index == 0):
            lx.append(divx[index][0])
            ly.append(divy[index][0])
        else:
            lx.append(divx[index][0][::-1])
            ly.append(divy[index][0][::-1])

    lx = np.hstack(lx)
    ly = np.hstack(ly)
    # print(l)
    # y = y * (-1)
    
    return lx, ly

def BGR2CYMK(arquivo):
    bgr = cv2.imread(arquivo)
    bgrdash = bgr.astype(np.float)/255.
    
    K = 1-np.max(bgrdash, axis=2)

    C = (1- bgrdash[...,2] - K)/(1-K)
    Y = (1- bgrdash[...,0] - K)/(1-K)
    M = (1- bgrdash[...,1] - K)/(1-K)
    
    return C, Y, M, K

# def Resolucao(width, height, n_linhas):
    dimensoes = [width, height]
    Res = max(dimensoes)/n_linhas

    return Res

def TempoEstimado(nb_pixels):
    tempo_Est = 0.00000004*(nb_pixels^2) -(0.0007*nb_pixels) + 6.3513
    return math.ceil(abs(tempo_Est))

def Chunks(lista, size):
    chunks = [lista[f:f+size] for f in range(0, len(lista), size)]
    
    l = []
    
    for index in range(len(chunks)):
        if index % 2 == 0:
            l.append(chunks[index])
        else:
            l.append(chunks[index][::-1])

    flat_list = [item for sublist in l for item in sublist]

    return flat_list

def imagem(cor, arquivo, freq_max, amp_max, n_colunas):
    
    if cor == 'Escala de Cinza':

        img = cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)
        img = np.array(img, dtype = np.float32)

        len_x = img.shape[1]
        len_y = img.shape[0]

        print('')
        print('Dimensão Original:', len_x, len_y, len_x * len_y)

        resolucao = max(img.shape)/n_colunas

        if (len_x/resolucao)*(len_y/resolucao) > 75000:
            print('Este desenho está com muitos pontos. Por favor diminuia o tamanho da resolução.')
            print('')
            exit()

        img = cv2.resize(img, (int(len_x/resolucao),int(len_y/resolucao)), interpolation=cv2.INTER_LINEAR)
        len_x = img.shape[1]
        len_y = img.shape[0]

        print('Dimensão Redimensionada', len_x, len_y, len_x * len_y)

        print('Irá demorar aproximadamente',TempoEstimado(len_x*len_y),'segundos para processar a imagem.')
        print('') 

        x, y = Calculos(freq_max, amp_max, len_y, len_x, img)

        if (len(x) or len(y)) <= 0:
            print('Esta resolução está pequena demais e não há pontos suficientes. Por favor aumente a resolução.')
            print('')
            exit()

        print('Número de pontos:', len(x))
        print('')

        flat_listX = Chunks(x, len_x)

        plt.plot(flat_listX,y,'k', linewidth=0.2)
        plt.show()
      
        return x, y

        #Fazer uma função que estima quanto tempo irá demorar para o Robô fazer o desenho

    elif cor == 'Colorido':
        
        (imgC, imgY, imgM, imgK) = BGR2CYMK(arquivo)

        len_x = imgC.shape[1]
        len_y = imgC.shape[0]

        print('Dimensão Original:', len_x, len_y, len_x * len_y)

        imgC = cv2.resize(imgC, (int(len_x/25),int(len_y/25)), interpolation=cv2.INTER_LINEAR)
        imgY = cv2.resize(imgY, (int(len_x/25),int(len_y/25)), interpolation=cv2.INTER_LINEAR)
        imgM = cv2.resize(imgM, (int(len_x/25),int(len_y/25)), interpolation=cv2.INTER_LINEAR)
        imgK = cv2.resize(imgK, (int(len_x/25),int(len_y/25)), interpolation=cv2.INTER_LINEAR)

        len_x = imgC.shape[1]
        len_y = imgC.shape[0]

        print('Dimensão Redimensionada', len_x, len_y, len_x * len_y)

        xC, yC = Calculos(freq_max, amp_max, len_y, len_x, imgC)
        xY, yY = Calculos(freq_max, amp_max, len_y, len_x, imgY)
        xM, yM = Calculos(freq_max, amp_max, len_y, len_x, imgM)
        xK, yK = Calculos(freq_max, amp_max, len_y, len_x, imgK)

        plt.plot(xC, yC,'cyan', linewidth=0.2)
        plt.plot(xY, yY,'yellow', linewidth=0.2)
        plt.plot(xM, yM,'magenta', linewidth=0.2)
        plt.plot(xK, yK,'k', linewidth=0.2)
        plt.show()

    else:
        print('Escolha entre Escala de Cinza e Colorido')


Cores = ['Escala de Cinza', 'Colorido']
Arquivo = 'Figuras/Degrade.png'
Freq_max = 10
Amp_max = 1
Res = 20

X, Y = imagem(Cores[0], Arquivo, Freq_max, Amp_max, Res)