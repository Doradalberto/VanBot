import black
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import cv2

def Stippling(intensidade, x0, y0):
    x = []
    y = []
    z = []

    for _ in range(intensidade):
        x_ = (x0 + random.random())
        x.append(x_)
        x.append(x_)
        x.append(x_)

        y_ = (y0 + random.random())
        y.append(y_)
        y.append(y_)
        y.append(y_)

        z.append(0.003)
        z.append(0)
        z.append(0.003)

        print(z)

    return x, y, z

def Scribble(intensidade, x0, y0):
    x = []
    y = []
    z = []

    for _ in range(intensidade):
        x.append(x0 + random.random())
        y.append(y0 + random.random())
        z.append(0)

    return x, y, z

def seno(freq, amp, x0, y0):
	xi = [0.0, math.pi*0.5, math.pi*1.5, 2*math.pi]
	x = []
	y = []

	for i in range(0, freq):
		for j in xi:
			if (j != 0 and i > 0) or (i == 0):
				yi = math.sin(j)
				x.append(x0 + (j + i*2*math.pi)/(freq*2*math.pi))
				y.append(y0 + yi * amp/2)

	return x, y

def Calculos(Freq_max, Amp_max, len_y, len_x, img):
    divx = []
    divy = []

    x = []
    y = []

    lista = []
    listay = []
    for i in range(0, len_y - 1): #cada linha do desenho

        for j in range(0, len_x):
            freq = int(Freq_max - (img[i,j]/255)*Freq_max + 1) # SOMAR +1 PARA TER FREQUENCIA MÍNIMA DE 1
            amp = (Amp_max - (img[i,j]/255)*Amp_max)
            xi, yi = seno(freq, amp, j, i)
            x = np.hstack((x, xi))
            y = np.hstack((y, yi))
            
            if (j == len_x-1):
                divx.append(x)
                divy.append(y)

                x = []
                y = []

    for index in range(len(divx)):
        if index % 2 == 0:
            lista.append(divx[index])
            listay.append(divy[index])
        else:
            lista.append(divx[index][::-1])
            listay.append(divy[index][::-1])
    
    # print(lista)
    # y = y * (-1)
    lista = np.hstack(lista)
    listay = np.hstack(listay)

    listay = listay * (-1)
    
    return lista, listay

def CalculosPoint(Funcao, Freq_max, len_y, len_x, img):
    divx = []
    divy = []

    x = []
    y = []

    lista = []
    listay = []
    for i in range(0, len_y - 1): #cada linha do desenho

        for j in range(0, len_x):
            freq = int(Freq_max - (img[i,j]/255)*Freq_max + 1) # SOMAR +1 PARA TER FREQUENCIA MÍNIMA DE 1

            if Funcao == 'Scribble':
                xi, yi, zi = Scribble(freq, j, i)

            elif Funcao == 'Pontilhismo':
                xi, yi, zi = Stippling(freq, j, i)

            x = np.hstack((x, xi))
            y = np.hstack((y, yi))
            
            if (j == len_x-1):
                divx.append(x)
                divy.append(y)

                x = []
                y = []

    for index in range(len(divx)):
        if index % 2 == 0:
            lista.append(divx[index])
            listay.append(divy[index])
        else:
            lista.append(divx[index][::-1])
            listay.append(divy[index][::-1])
    
    lista = np.hstack(lista)
    listay = np.hstack(listay)

    listay = listay * (-1)
    
    return lista, listay

def Estilo(estilo, arquivo, freq_max, amp_max, n_colunas):
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

    if estilo == 'Senoide':

        x, y = Calculos(freq_max, amp_max, len_y, len_x, img)

        print('Número de pontos:', len(x))
        print('')

        plt.plot(x,y,'k', linewidth=0.2)
        plt.gca().set_aspect('equal')
        plt.axis('off')
        plt.savefig('static/figures/preview.png', bbox_inches='tight', pad_inches=0)
        plt.show()
      
        return x, y

    elif estilo == 'Pontilhismo':

        x, y = CalculosPoint('Pontilhismo',freq_max, len_y, len_x, img)

        print('Número de pontos:', len(x))
        print('')

        plt.scatter(x,y,s = 0.1)
        plt.gca().set_aspect('equal')
        plt.axis('off')
        plt.savefig('static/figures/preview.png', bbox_inches='tight', pad_inches=0)
        plt.show()

        plt.savefig('preview.png')
      
        return x, y

    elif estilo == 'Rabiscos':

        x, y = CalculosPoint('Scribble', freq_max, len_y, len_x, img)

        print('Número de pontos:', len(x))
        print('')

        plt.plot(x,y,'k',linewidth=0.3)
        plt.gca().set_aspect('equal')
        plt.axis('off')
        plt.savefig('static/figures/preview.png', bbox_inches='tight', pad_inches=0)
        plt.show()

        plt.savefig('preview.png')
      
        return x, y
    
    else:
        exit()


Cores = ['Escala de Cinza', 'Colorido']

# Arquivo = 'Figuras/reis2.png'
# Freq_max = 5
# Amp_max = 1
# Res = 220

Arquivo = 'Figuras/noite-estrelada.jpg'
Freq_max = 8
Amp_max = 1
Res = 200

estilo = ['Senoide', 'Pontilhismo', 'Rabiscos', 'TSP']
X, Y = Estilo(estilo[1], Arquivo, Freq_max, Amp_max, Res)

