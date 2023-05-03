# Nuestra configuración inicial, importamos las librearias a utilizar, creamos
#nuestra funcion para mostras imagenes y descargamos las imagenes a utilizar
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Definimos nuestra funcion
def imshow(title = "Image", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('images/bottlecaps.jpg')
imshow('Original', image)

image = cv2.imread('images/bottlecaps.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 25)

cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # Dibujamos circulo externo 
    cv2.circle(image,(i[0], i[1]), i[2], (0, 0, 255), 5)
    
    # Dibujamos circulo intero
    cv2.circle(image, (i[0], i[1]), 2, (255, 0, 0), 8)

imshow('Detected circles', image)