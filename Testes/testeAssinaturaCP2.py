import cv2
import matplotlib.pyplot as plt

arquivo = 'Figuras/Assinatura.png'

X = []
Y = []
  
def click_event(event, x, y, flags, params):
 
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # xprint(x, ' ', y)
        X.append(x)
        Y.append(y)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'.', (x,y), font,
                    0, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
if __name__=="__main__":

    img = cv2.imread(arquivo, 1)
 
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print(X)
print('')
print(Y)

Y2 = []

for e in Y:
    Y2.append(e*(-1))

plt.plot(X, Y2)
plt.show()