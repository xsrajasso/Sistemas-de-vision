import cv2

body_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_fullbody.xml')

video_capture = cv2.VideoCapture(1)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
    #bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (124,252,0), 10)

    # Tecla Q para cerrar la webcam
    cv2.imshow('Full Body Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
