import cv2
import matplotlib.pyplot as plt

arquivo = 'Figuras/Maca.webp'
img = cv2.imread(arquivo, cv2.IMREAD_COLOR)

# lista = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9,10,11,12],
#          [13,14,15,16],
#          [17,18,19,20]]

novalista = []

for index,e in enumerate(img):
    # print(e)
    if index % 2 == 0:
        novalista.append(e)
    else:
        novalista.append(e[::-1])

plt.imshow(novalista)
plt.show()
# print(novalista)

# lista0 = [[1,2,3,4,5]]
# lista1 = [[6,7,8,9,10,11]]
# import numpy as np
# lista3 = np.hstack((lista0,lista1))

# print(lista3)