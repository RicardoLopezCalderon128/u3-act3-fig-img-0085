import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Lopez Calderon Ricardo NC = 0085
print("Lopez Calderon Ricardo NC = 0085")
print("UIII act3 colocar puntos a una imagen en blanco y negro")
mi_imagen = cv2.imread('tiburon.jpg')
plt.imshow(mi_imagen)
plt.title('tiburon y Lopez Ricardo 0085')
plt.show()
print("-+-+-+-+-+puntos de la imagen-+-+-+-+-+-+-")
plt.imshow(mi_imagen)
x = [120,100,300,300]
y = [120,400,420,300]
plt.scatter(x,y, s=20 , c="red")
plt.show()
print("-+-+-+-+-+cuadro de la imagen-+-+-+-+-+-+-")
imgtb=cv2.imread("tiburon.jpg")
plt.imshow(imgtb)
# x = [50,50,300,300,50]
# y = [70,400,400,70,70]
x = [50,50,300,300,50]
y = [70,400,400,70,70]
plt.plot(x,y,c="blue")
plt.show()

print("-+-+-+-+-+cuadro de la imagen-+-+-+-+-+-+-")
imgtb=cv2.imread("tiburon.jpg")
plt.imshow(imgtb)
# x = [50,50,300,300,50]
# y = [70,400,400,70,70]

# Mover el cuadro 50 cuadros y reducirlo aún más (al 50%)
x = [50 + v * 0.5 for v in [50,50,300,300,50]]
y = [50 + v * 0.5 for v in [70,400,400,70,70]]

plt.plot(x,y,c="blue")
plt.show()
print("-+-+-+-+-+cuadro de la imagen-+-+-+-+-+-+-")
imgtb=cv2.imread("tiburon.jpg")
plt.imshow(imgtb)

# Círculo verde desplazado 50 cuadros con radio más grande
centro_x = 50 + 175 * 0.5
centro_y = 50 + 235 * 0.5
radio = 100  # Se aumenta el radio del círculo

circulo = plt.Circle((centro_x, centro_y), radio, color="green", fill=False, linewidth=2)
plt.gca().add_patch(circulo)

plt.show()


