"""
@author: Tomas Jasso

"""

# importing required libraries
import cv2
from matplotlib import pyplot as plt

ubicacion = "C:/Users/xsraj/Documents/Sistemas-de-vision/practica/tarea3/"

#Imagen que vamos a transformar
img = cv2.imread(ubicacion + "Ave_2.jpg", 0)

# reads an input image
#img = cv2.imread("Ave_2.jpg",0)
#img = cv2.imread(image,0)


# find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(121)
plt.imshow(img)
plt.title('Entrada / Input')

# show the plotting graph of an image
plt.subplot(122)
plt.plot(histr)
plt.title('Salida / Output')
plt.show()

# show the plotting graph of an image
plt.hist(img.ravel(),256,[0,256])
plt.show()