import pygame
import sys

def main():

    pygame.init()


    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption('My Canvas')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.quit()
                    sys.exit()

        screen.fill((255, 255, 255))

        pygame.display.flip()

main()
