import matplotlib.pyplot as plt
import math
import numpy as np
import cv2

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


img = cv2.imread('VB/Frida.jfif', cv2.IMREAD_GRAYSCALE)
img = np.array(img, dtype = np.float32)

len_x = img.shape[1]
len_y = img.shape[0]

print('Dimensão Original:', len_x, len_y, len_x * len_y)

img = cv2.resize(img, (int(len_x/3),int(len_y/3)), interpolation=cv2.INTER_LINEAR)

len_x = img.shape[1]
len_y = img.shape[0]

print('Dimensão Redimensionada', len_x, len_y, len_x * len_y)

x = []
y = []
Freq_max = 7
Amp_max = 1

for i in range(0, len_y - 1):
	for j in range(0, len_x - 1):
		freq = int(Freq_max - (img[i,j]/255)*Freq_max + 1) # +1 PARA ~TER FREQUENCIA MÍNIMA DE 1
		amp = (Amp_max - (img[i,j]/255)*Amp_max)
		if i % 2 == 0:
			direction = 1
			xi, yi = seno(freq, amp, j, i, direction)
			x = np.hstack((x, xi))
			y = np.hstack((y, yi))
		else:
			direction = -1
			xi, yi = seno(freq, amp, j, i, direction)
			x = np.hstack((x, xi))
			y = np.hstack((y, yi))

y = y * (-1)
print(x) #multiplicar pelo fator de escala (px -> unidade)
print(y) #multiplicar pelo fator de escala (px -> unidade)

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0.1)
plt.show()


