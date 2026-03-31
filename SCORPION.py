import pygame  # On importe pygame pour faire un jeu / interface graphique

pygame.init()  # On démarre pygame 

# On charge l'image 
tete_mort = pygame.image.load("C:\Users\sasha\SCORPION\tetedemort.png").convert_alpha()

nouvelletaille = (100, 100)  # Nouvelle taille de l'image 

# On redimensionne l'image
tete_mort = pygame.transform.scale(tete_mort, nouvelletaille)

size = (1000, 1000)  # Taille de la fenêtre 
screen = pygame.display.set_mode(size)  # On crée la fenêtre

pygame.display.set_caption("SCORPION")  # Nom de la fenêtre 

# Rectangle qui sert de zone de texte en bas
textenter = pygame.Rect(350, 950, 300, 50)

running = True  # Variable pour faire tourner le jeu en boucle

# Boucle principale
while running:
    for event in pygame.event.get():  # On check tous les événements (clic, fermeture, etc.)
        if event.type == pygame.QUIT:  # Si on clique sur la croix
            running = False  # On arrête le jeu

    screen.fill((139, 0, 0))  #fond rouge sombre

    screen.blit(tete_mort, (100, 100))  # On affiche la tête de mort 

    pygame.draw.rect(screen, (255, 255, 255), textenter)  # On dessine un rectangle blanc

    pygame.display.flip()  # On met à jour l'écran

pygame.quit()  # On ferme pygame

