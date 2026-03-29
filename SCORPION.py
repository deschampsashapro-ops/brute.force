import pygame

pygame.init()

tete_mort = pygame.image.load("C:\Users\sasha\SCORPION\tetedemort.png").convert_alpha()

nouvelletaille = (100, 100)

tete_mort = pygame.transform.scale(tete_mort, nouvelletaille)

size = (1000, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("SCORPION")

textenter = pygame.Rect(350, 950, 300, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((139, 0, 0))

    screen.blit(tete_mort, (100, 100))

    pygame.draw.rect(screen, (255, 255, 255), textenter)

    pygame.display.flip()

pygame.quit()


