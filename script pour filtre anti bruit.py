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
#normalized_image = (np_array - np.min(np_array)) / (np.max(np_array) - np.min(np_array))

# Créer un noyau de filtre de flou moyen (3x3)
#kernel = np.ones((3, 3)) / 9
s = 40
kernel = np.array([[-1,-1,-1],[-1,s,-1],[-1,-1,-1]]) 
# Appliquer le filtre de flou moyen à une image (par exemple, une image aléatoire)
image = Image.open(r'/Users/sashadeschamps/Library/CloudStorage/OneDrive-Personnel/Documents/Devoirs 2nd2/PengBrew.pgm')# Remplacez cela par votre propre image

# Appliquer le filtre en utilisant la convolution 2D
blurred_image = np.abs(convolve2d(image, kernel, mode='same', boundary='wrap'))

# Afficher l'image originale et celle avec le filtre de flou moyen appliqué
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Image originale')
plt.subplot(122), plt.imshow(blurred_image, cmap='gray'), plt.title('Image avec filtre antit bruit')
plt.show()
