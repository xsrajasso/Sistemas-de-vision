# Importamos las librerias a utilizar
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Definimos la funcion "imshow"
def imshow(title = "Image", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

def faces():
    
    # Usamos la funcio CascadeClassifier 
    # El archivo XML del clasificador se guarda en una variable
    face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_fullbody.xml')

    # Cargamos nuestra imagen y la convertimos a escala de grises
    image = cv2.imread('images/pw2.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    #El clasificador regresa el ROI de la cara detectada
    #Guarfa la coordenada de la esquina superior izquierda y la coordeada inferior derecha
    faces = face_classifier.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 2)

    # Si no se detecta niguna cara al clasificador regresa una Tupla vacia
    if faces is ():
        print("No faces found")

    #Iteramos sobre las coordenadas y dibujamos un rectangulo sobre cada cara detectada
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (124,252,0), 10)

    imshow('Persona detectada', image)

faces()
#facesEyes()