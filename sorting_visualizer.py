import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import random

plt.ion()

def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            plt.clf()
            plt.bar(range(len(arr)), arr, color="blue")
            plt.title("Bubble Sort Visualization")
            plt.pause(0.1)

arr = [random.randint(1,100) for _ in range(20)]

plt.figure()

bubble_sort(arr)

plt.ioff()
plt.show()