import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_triangle():
    vertices = [
        (0, 1),
        (-1, -1),
        (1, -1)
    ]

    glColor3f(128.0, 0.0, 128.0)
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    gluOrtho2D(-2, 2, -2, 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        draw_triangle()

        pygame.display.flip()

    pygame.quit()


main()
