#Librerias
import cv2
import numpy as np

#Imagen que vamos a transformar
image = cv2.imread("Ave_1.png")

#Almacenamos el alto y ancho de la imagen # de aspecto fila, columnas
#[0][0] es un cuadro

height, width = image.shape[0], image.shape[1]

#Variables de traslacion (posicion de la imagen)

y1, x1 = height/2, width/2

#Traslacion
#T = np.float32([[1,0,posicion en x],[0,1,posicion en y]])
T = np.float32([[1, 0, x1],[0, 1, y1]])

#Se usa warpAffine para transformar
#La imagen usando la matriz, T

img_Out = cv2.warpAffine(image, T, (width, height))

#Presentacion de la imagen y espera de cancelacion de instruccion

cv2.imshow("Originalimage", image)
cv2.imshow("Translation", img_Out)
cv2.waitKey()

cv2.destroyAllWindows()
