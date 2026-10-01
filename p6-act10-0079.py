import numpy as np
import cv2
#Vision Artificial act 10 NC 0079
# Lee la imagen en escala de grises
img = cv2.imread("ton618.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("ton618 0079", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Linea 
print("La Linea 0079")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)
# Abre la ventana con la imagen
cv2.imshow("Line 0079", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Circulo

# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)
# Abre la ventana con la imagen
cv2.imshow("Circle 0079", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Texto
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "El texto con la line", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)
# Abre la ventana con la imagen
cv2.imshow("Texto 0079", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#TrackBars
def on_trackbar(val):
    print(val)

# Crear imagen negra y la ventana
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Los trackers')

# Crear los trackbars
cv2.createTrackbar('R', 'Los trackers', 0, 255, on_trackbar)
cv2.createTrackbar('G', 'Los trackers', 0, 255, on_trackbar)
cv2.createTrackbar('B', 'Los trackers', 0, 255, on_trackbar)

while True:
    cv2.imshow('Los trackers', img)
    
    k = cv2.waitKey(1) & 0xFF
    # Salir si se presiona la tecla ESC (27)
    if k == 27:
        break

    # Validar si el usuario cerró la ventana presionando la (X)
    if cv2.getWindowProperty('Los trackers', cv2.WND_PROP_VISIBLE) < 1:
        break

    # Obtener las posiciones de los trackbars
    r = cv2.getTrackbarPos('R', 'Los trackers')
    g = cv2.getTrackbarPos('G', 'Los trackers')
    b = cv2.getTrackbarPos('B', 'Los trackers')

    # Actualizar el color de la imagen (OpenCV usa formato BGR)
    img[:] = [b, g, r]

cv2.destroyAllWindows()

#Thresholding

img = cv2.imread('ton618.jpg',0)

ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thr2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thr3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thr4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thr5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY',thr1)
cv2.imshow('BINARY_INV',thr2)
cv2.imshow('TRUNC',thr3)
cv2.imshow('TOZERO',thr4)
cv2.imshow('TOZERO_INV',thr5)


cv2.waitKey(0)
cv2.destroyAllWindows()
