import random
import math
import matplotlib.pyplot as plt


def Stippling(intensidade):
    x = []
    y = []
    for _ in range(intensidade):
        x.append(random.random())
        y.append(random.random())

    return x, y


def seno(freq, amp, x0, y0, direction):
	xi = [0.0, math.pi*0.5, math.pi*1.5, 2*math.pi]
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

# x, y = seno(15,1,0,0,1)

# plt.plot(x,y)
# plt.show()

x0, y0 = Stippling(255)
plt.scatter(x0, y0)
plt.show()

# import random
# import math

# npoints = 50
# mindist = 0.2

# def genpt():
#     return (random.random(), random.random())

# def distance(p1,p2):
#     return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# sample = []

# while len(sample) < npoints:
#    newp = genpt()
#    for p in sample:
#       if distance(newp,p) < mindist: break
#    else:
#      sample.append(newp)

# print(sample)

# plt.plot(sample,'o')
# plt.show()