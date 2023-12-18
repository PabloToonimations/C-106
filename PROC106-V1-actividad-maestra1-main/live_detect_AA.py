# importar la biblioteco OpenCv
import cv2

# Cargar el archivo clasificador en cascadas
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('C:/Users/preet/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_eye.xml')

# Definir un objeto de captura de video
vid = cv2.VideoCapture(0)

while(True):

    # Capturar el video cuadro por cuadro
    ret, frame = vid.read()

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar las caras, los ojos y la sonrisa
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)