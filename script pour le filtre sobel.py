from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

image = Image.open(r'/Users/sashadeschamps/Library/CloudStorage/OneDrive-Personnel/Documents/Devoirs 2nd2/PengBrew.pgm')

# Convertir l'image en tableau NumPy
np_array = np.array(image)

# Obtenir les dimensions de l'image
largeur, hauteur = image.size
print(largeur, hauteur)

# Afficher le tableau NumPy
print(np_array)
print(np_array[hauteur-1, largeur-1])

# Normalisation des valeurs de l'image entre 0 et 1
normalized_image = (np_array - np.min(np_array)) / np.max(np_array)

# Créer un noyau de filtre de flou à moyen (3x3)
kernel1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]]) 
kernel2 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]]) 


# Appliquer le filtre de sobel à une image (par exemple, une image aléatoire)
image = Image.open(r'/Users/sashadeschamps/Library/CloudStorage/OneDrive-Personnel/Documents/Devoirs 2nd2/PengBrew.pgm')# Remplacez cela par votre propre image

# Appliquer le filtre en utilisant la convolution 2D
blurred_image1 = np.abs (convolve2d(image, kernel1, mode='same', boundary='wrap'))
blurred_image2 = np.abs (convolve2d(image, kernel2, mode='same', boundary='wrap'))

# Afficher l'image originale et celle avec le filtre de sobel appliqué
plt.subplot(121), plt.imshow(normalized_image, cmap='gray'), plt.title('Image originale')
plt.subplot(122), plt.imshow(blurred_image1 + blurred_image2, cmap='gray'), plt.title('Image avec filtre sobel')
plt.show()
