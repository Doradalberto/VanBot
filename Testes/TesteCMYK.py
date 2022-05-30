import cv2
import numpy as np

def BGR2CYMK(arquivo):
    bgr = cv2.imread(arquivo)
    bgrdash = bgr.astype(np.float)/255.
    
    K = 1- np.max(bgrdash, axis=2)

    C = (bgrdash[...,2] - K)/(1-K)
    Y = (bgrdash[...,0] - K)/(1-K)
    M = (bgrdash[...,1] - K)/(1-K)

    CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)

    return C, Y, M, 1-K


arquivo = 'Figuras/Maca.webp'
(C,Y,M,K) = BGR2CYMK(arquivo)

cv2.imshow('C',C)
cv2.waitKey(0)

cv2.imshow('Y',Y)
cv2.waitKey(0)

cv2.imshow('M',M)
cv2.waitKey(0)

cv2.imshow('K',K)
cv2.waitKey(0)