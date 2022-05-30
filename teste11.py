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
        y_ = (y0 + random.random())

        x.append(x_)
        x.append(x_)
        x.append(x_)

        y.append(y_)
        y.append(y_)
        y.append(y_)

        z.append(0.003)
        z.append(0)
        z.append(0.003)

    return x, y, z

def Rabiscos(intensidade, x0, y0):
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
    z = []

    for i in range(0, freq):
        for j in xi:
            if (j != 0 and i > 0) or (i == 0):
                yi = math.sin(j)
                x.append(x0 + (j + i*2*math.pi)/(freq*2*math.pi))
                y.append(y0 + yi * amp/2)
                z.append(0)

    return x, y, z

def Calculos(Freq_max, len_y, len_x, img, estilo):
    Amp_max = 1

    divx = []
    divy = []
    divz = []

    x = []
    y = []
    z = []

    listax = []
    listay = []
    listaz = []

    for i in range(0, len_y - 1): #cada linha do desenho

        for j in range(0, len_x):
            freq = int(Freq_max - (img[i,j]/255)*Freq_max + 1) # SOMAR +1 PARA TER FREQUENCIA MÍNIMA DE 1
            amp = (Amp_max - (img[i,j]/255)*Amp_max)

            if estilo == 'Seno':
                xi, yi, zi = seno(freq, amp, j, i)
            elif estilo == 'Pontilhismo':
                xi, yi, zi = Stippling(freq, j, i)
            elif estilo == 'Rabiscos':
                xi, yi, zi = Rabiscos(freq, j, i)

            x = np.hstack((x, xi))
            y = np.hstack((y, yi))
            z = np.hstack((z, zi))
            
            if (j == len_x-1):
                divx.append(x)
                divy.append(y)
                divz.append(z)

                x = []
                y = []
                z = []

    for index in range(len(divx)):
        if index % 2 == 0:
            listax.append(divx[index])
            listay.append(divy[index])
            listaz.append(divz[index])
        else:
            listax.append(divx[index][::-1])
            listay.append(divy[index][::-1])
            listaz.append(divz[index][::-1])
    
    listax = np.hstack(listax)
    listay = np.hstack(listay)
    listaz = np.hstack(listay)

    listay = listay * (-1)
    
    return listax, listay, listaz

def Estilo(estilo, arquivo, freq_max, n_colunas, metros):
    img = cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)
    img = np.array(img, dtype = np.float32)
    
    len_x = img.shape[1]
    len_y = img.shape[0]
    
    print('')
    print('Dimensão Original:', len_x, len_y, len_x * len_y)

    resolucao = max(img.shape)/n_colunas

    if (metros == 'A4') or (metros == 'a4'):
        tamanho = 0.18 / (n_colunas/100)

    elif (metros == 'A3') or (metros == 'a3'):
        tamanho = 0.388 / (n_colunas/100)

    elif (metros == 'A2') or (metros == 'a2'):
        tamanho = 0.562 / (n_colunas/100)

    if (len_x/resolucao)*(len_y/resolucao) > 75000:
        print('Este desenho está com muitos pontos. Por favor diminuia o tamanho da resolução.')
        print('')
        exit()

    img = cv2.resize(img, (int(len_x/resolucao),int(len_y/resolucao)), interpolation=cv2.INTER_LINEAR)
    len_x = img.shape[1]
    len_y = img.shape[0]

    print('Dimensão Redimensionada', len_x, len_y, len_x * len_y)

    if estilo == 'Senoide':

        x, y, z = Calculos(freq_max, len_y, len_x, img, 'Seno')

        print('Número de pontos:', len(x))
        print('')
        
        with open('Pontos.txt', 'w') as f:
            f.write(str(len(x)))

        plt.clf()
        plt.plot(x,y,'k', linewidth=0.2)
        plt.gca().set_aspect('equal')
        plt.axis('off')
        plt.savefig('static/figures/preview.png', bbox_inches='tight', pad_inches=0)
        
        return (tamanho*x/100), -(tamanho*y/100), z

    elif estilo == 'Pontilhismo':

        x, y, z = Calculos(freq_max, len_y, len_x, img, 'Pontilhismo')

        print('Número de pontos:', len(x))
        print('')

        with open('Pontos.txt', 'w') as f:
            f.write(str(len(x)))

        plt.clf()
        plt.scatter(x,y,color='black',s = 0.01)
        plt.gca().set_aspect('equal')
        plt.axis('off')
        plt.savefig('static/figures/preview.png', bbox_inches='tight', pad_inches=0)
      
        return (tamanho*x/100), -(tamanho*y/100), z

    elif estilo == 'Rabiscos':

        x, y, z = Calculos(freq_max, len_y, len_x, img, 'Rabiscos')

        print('Número de pontos:', len(x))
        print('')

        with open('Pontos.txt', 'w') as f:
            f.write(str(len(x)))

        plt.clf()
        plt.plot(x,y,'k',linewidth=0.3)
        plt.gca().set_aspect('equal')
        plt.axis('off')
        plt.savefig('static/figures/preview.png', bbox_inches='tight', pad_inches=0)
      
        return (tamanho*x/100), -(tamanho*y/100), z
    
    else:
        exit()
