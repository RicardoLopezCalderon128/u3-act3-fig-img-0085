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


