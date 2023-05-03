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

image = cv2.imread('images/soduku.jpg')
imshow('Original', image)

# Convertimos a escalas de grises y aplicamos filtro canny
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# Asignamos a rho 1 pixel de exactitud
# Asignamos a theta pi/180 de exactitud
# Nuestro umbral de linea se pone a 240 (el numero de puntos en nuestra linea)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 240)

# Iteramos en todas las lineas y convertimos al formato requerido por el comando
#cv2.line (punto inicial y final)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

imshow('Filtro Canny', edges)
imshow('Hough Lines', image)