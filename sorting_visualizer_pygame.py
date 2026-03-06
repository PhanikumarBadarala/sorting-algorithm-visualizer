import pygame
import random
import time

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

arr = [random.randint(10, 350) for _ in range(50)]

def draw(arr, color_pos={}):
    screen.fill((0,0,0))

    bar_width = WIDTH // len(arr)

    for i,val in enumerate(arr):
        color = (0,255,0)

        if i in color_pos:
            color = color_pos[i]

        pygame.draw.rect(screen,color,(i*bar_width,HEIGHT-val,bar_width,val))

    pygame.display.update()


def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

            draw(arr,{j:(255,0,0),j+1:(255,0,0)})
            time.sleep(0.03)

running = True

while running:

    draw(arr)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bubble_sort(arr)

pygame.quit()