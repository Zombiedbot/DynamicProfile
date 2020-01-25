import pygame
import graphics
import menu

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dynamic profile")

#n, m = [int(i) for i in input().split()]

background_image = pygame.image.load('images/background.jpg')
screen.blit(background_image, (0, 0))
pygame.display.update()

menu.menuShow(screen, background_image)

screen.blit(background_image, (0, 0))

tr = 1
while tr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tr = 0
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == "escape":
                menu.menuShow(screen, background_image)
pygame.quit()
