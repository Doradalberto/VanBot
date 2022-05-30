import cv2
import matplotlib.pyplot as plt
import numpy as np
import MargemCP2 as mg

def MandaPontos(figura):
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.cvtColor(figura,cv2.COLOR_BGR2GRAY)

    #Size of the sheet in mm
    SizeXmm = 210
    SizeYmm = 297

    #Size of the picture in pixels
    (SizeXpx, SizeYpx) = img.shape
    branco = np.zeros((SizeXpx, SizeYpx), dtype = 'uint8')
    _, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    plt.imshow(threshold)
    plt.show()
    contours, _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    Coordenadas = []
    X = []
    Y = []

    for cnt in contours :
    
        approx = cv2.approxPolyDP(cnt, 0.001* cv2.arcLength(cnt, True), True)
    
        cv2.drawContours(figura, [approx], 0, (0, 255, 0), 2) 
    
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

                # string = str(x) + " " + str(y) 
                # cv2.putText(figura, string, (x, y), font, 0.5, (0, 255, 0)) 
                
            i = i + 1

    print('')
    print('Quantidade total de pontos: ',len(Coordenadas))

    return figura, X, Y

arquivo = 'Figuras/Assinatura.png'
folha = 'A4'
orientacao = 'Retrato'
margem = 50

figura = mg.Bordas(arquivo, folha, orientacao, margem)

# plt.imshow(figura)
# plt.show()

plt.imshow(MandaPontos(figura)[0])
plt.show()
