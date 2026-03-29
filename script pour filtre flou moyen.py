from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

image = Image.open(r'/Users/sashadeschamps/Library/CloudStorage/OneDrive-Personnel/Stage 2nd/isp_ambient_076.pgm')

# Convertir l'image en tableau NumPy
np_array = np.array(image)

# Obtenir les dimensions de l'image
largeur, hauteur = image.size
print(largeur, hauteur)

# Afficher le tableau NumPy
print(np_array)
print(np_array[hauteur-1, largeur-1])

# Normalisation des valeurs de l'image entre 0 et 1
normalized_image = (np_array - np.min(np_array)) / (np.max(np_array) - np.min(np_array))

# Afficher l'image normalisée
#image = Image.open(r'/Users/sashadeschamps/Library/CloudStorage/OneDrive-Personnel/Stage 2nd/isp_ambient_076.pgm')
#plt.imshow(normalized_image, cmap='gray')
#plt.colorbar()
#plt.show()

# Créer un noyau de filtre de flou moyen (3x3)
kernel = np.ones((3, 3)) / 9

# Appliquer le filtre de flou moyen à une image (par exemple, une image aléatoire)
image = Image.open(r'/Users/sashadeschamps/Library/CloudStorage/OneDrive-Personnel/Stage 2nd/isp_ambient_076.pgm')# Remplacez cela par votre propre image

# Appliquer le filtre en utilisant la convolution 2D
blurred_image = convolve2d(image, kernel, mode='same', boundary='wrap')

# Afficher l'image originale et celle avec le filtre de flou moyen appliqué
plt.subplot(121), plt.imshow(normalized_image, cmap='gray'), plt.title('Image originale')
plt.subplot(122), plt.imshow(blurred_image, cmap='gray'), plt.title('Image avec flou moyen')
plt.show()



# Ouvrir l'image PGM
#image.show()  # Afficher l'image (optionnel)

