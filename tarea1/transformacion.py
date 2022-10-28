#AUTOR TOMAS ISRAEL JASSO RAMIREZ 1943530 FIME

#Librerias
import cv2
import numpy as np
print("LIBRERIAS IMPORTADAS CORRECTAMENTE")

ubicacion = "C:/Users/xsraj/Documents/Sistemas-de-vision/tarea1/"

#Imagen que vamos a transformar
image = cv2.imread(ubicacion + "ave_2.jpg")

#Almacenamos el alto y ancho de la imagen # de aspecto fila, columnas
#[0][0] es un cuadro

height, width = image.shape[0], image.shape[1]

#Variables de traslacion (posicion de la imagen)

#Original
y1, x1 = height / 2, width / 2

#Ejercicio 1 Traslacion
#y1, x1 = 250, 100

#Ejercicio 2 Traslacion
#y1, x1 = 10, 600

#Traslacion
#T = np.float32([[1,0,posicion en x],[0,1,posicion en y]])
T = np.float32([[1, 0, x1],[0, 1, y1]])

#Rotacion
#T = cv2.getRotationMatrix2D((coordenadas centro de rotacion), grados, escala)

#Original
#T = cv2.getRotationMatrix2D((x1, y1), 45, 1)

#Ejercicio 1 Rotacion
#T = cv2.getRotationMatrix2D((x1, y1), -90, 1)

#Ejercicio 2 Rotacion
T = cv2.getRotationMatrix2D((x1, y1), 180, 1)

#Se usa warpAffine para transformar
#La imagen usando la matriz, T

img_Out = cv2.warpAffine(image, T, (width, height))

#Presentacion de la imagen y espera de cancelacion de instruccion

cv2.imshow("Originalimage", image)
#cv2.imshow("Translation", img_Out)
cv2.imshow("Rotacion", img_Out)
cv2.waitKey()

cv2.destroyAllWindows()
