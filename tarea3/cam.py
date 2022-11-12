"""
Creado el 21/10/2022
Autor: Tomas Israel Jasso Ramirez
"""

#Librerias
import cv2
import numpy as np

#Se enciende la camara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #Localizar puntos de los documentos
    #u objeto a transformar

    pts1 = np.float32([[0,260], [640,260],[0, 640], [640, 400]])

    pts2 = np.float32([[0, 0],[400, 0], [0, 400], [400, 640]])

    #Aplicar el algoritmo de transformacion de perspectiva

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))

    #Envuelve la imagen transformada


    cv2.imshow("frame", frame) #Captura inicial
    cv2.imshow("frame1", result) #Captura transformada

    if cv2.waitKey(24) == 27:
        break

cap.release()
cv2.destroyAllWindows()

