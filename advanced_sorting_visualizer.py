import pygame
import random
import sys
import time

pygame.init()

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

FONT = pygame.font.SysFont("Arial",20)

array = []
n = 80

def generate_array():
    global array
    array = [random.randint(10,400) for _ in range(n)]

def draw_array(color_pos={}):
    screen.fill((0,0,0))

    bar_width = WIDTH//n

    for i,val in enumerate(array):

        color = (0,255,0)

        if i in color_pos:
            color = color_pos[i]

        pygame.draw.rect(screen,color,(i*bar_width,HEIGHT-val,bar_width,val))

    text = FONT.render("B-Bubble | I-Insertion | S-Selection | R-Randomize",True,(255,255,255))
    screen.blit(text,(20,20))

    pygame.display.update()


def bubble_sort():

    for i in range(len(array)):
        for j in range(len(array)-i-1):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

            draw_array({j:(255,0,0),j+1:(255,0,0)})
            time.sleep(0.01)


def insertion_sort():

    for i in range(1,len(array)):
        key = array[i]
        j = i-1

        while j>=0 and key < array[j]:

            array[j+1] = array[j]
            j -= 1

            draw_array({j:(255,0,0)})
            time.sleep(0.01)

        array[j+1] = key


def selection_sort():

    for i in range(len(array)):

        min_idx = i

        for j in range(i+1,len(array)):

            if array[j] < array[min_idx]:
                min_idx = j

            draw_array({j:(255,0,0),min_idx:(0,0,255)})
            time.sleep(0.01)

        array[i],array[min_idx] = array[min_idx],array[i]


generate_array()

running = True

while running:

    draw_array()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_b:
                bubble_sort()

            if event.key == pygame.K_i:
                insertion_sort()

            if event.key == pygame.K_s:
                selection_sort()

            if event.key == pygame.K_r:
                generate_array()

pygame.quit()