import cv2
import matplotlib.pyplot as plt
import numpy as np
import MargemCP2 as mg

def MandaPontos(arquivo):
    font = cv2.FONT_HERSHEY_COMPLEX
    img0 = cv2.imread(arquivo, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

    #Size of the sheet in mm
    SizeXmm = 210
    SizeYmm = 297

    #Size of the picture in pixels
    (SizeXpx, SizeYpx) = img.shape
    
    _, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    
    contours, _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    Coordenadas = []
    X = []
    Y = []

    for cnt in contours :
    
        approx = cv2.approxPolyDP(cnt, 0.03* cv2.arcLength(cnt, True), True)
    
        cv2.drawContours(img0, [approx], 0, (0, 0, 255), 2) 
    
        n = approx.ravel() 
        i = 0
    
        for j in n :
            if(i % 2 == 0):
                x = n[i]
                y = n[i + 1]

                #Pixels to meter
                calcX = ((SizeXmm * x)/(SizeXpx))/1000
                calcY = ((SizeYmm * y)/(SizeYpx))/1000

                Coordenadas.append([calcX, calcY, 0, 180, 0, 0])

                X.append(calcX)
                Y.append(calcY)

                string = str(x) + " " + str(y) 
                cv2.putText(img0, string, (x, y), font, 0.5, (0, 255, 0)) 
                
            i = i + 1

    # print('Quantidade de pontos: ',len(Coordenadas))

    return img0, X, Y


# print(str(tuple(X)).encode())
# print(str(tuple(Y)).encode())

arquivo = 'VanBot/Do.png'
folha = 'A4'
orientacao = 'Retrato'
margem = 50

figura = mg.Bordas(arquivo, folha, orientacao, margem)

plt.imshow(figura)
plt.show()
# MandaPontos(figura)[0]

# print(len(MandaPontos(arquivo)[1]))

cv2.imshow('Figura', MandaPontos(figura)[0])
cv2.waitKey(0)

# print(str(tuple(MandaPontos('FigurasGeometricas/Slide11.png')[1])))
# print(str(tuple(MandaPontos('FigurasGeometricas/Slide11.png')[2])))

