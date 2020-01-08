import numpy as np
import matplotlib.pyplot as plt 
import random as rd

n = 1000 #1000 moves
x = np.zeros(n) 
y = np.zeros(n) 
  
food_x = []
food_y = []

point = 0

for i in range(10):
    a = rd.randint(-10,10)
    b = rd.randint(-10,10)
    food_x.append(a)
    food_y.append(b)

# The predator moves in 4 direction 
for i in range(1, n): 
    move = rd.randint(1, 4) 
    if move == 1: 
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
    elif move == 2: 
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    elif move == 3: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + 1
    else: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
    
    for j in range(len(food_x)):
        if ((x[i] == food_x[j]) and (y[i] == food_y[j])):
            point += 1
        
    
            
        
    plt.title("Random Walk = " + str(i)) 
    plt.scatter(food_x, food_y, label = 'food: ' + str(point))
    plt.scatter(x[i], y[i], color = 'r', label = 'predator') 
    plt.legend()
    plt.savefig("image/rand_walk"+str(i)+".png") 
    plt.show() 

import os
import imageio

directory = 'image/'
images = []
for file_name in os.listdir(directory):
    if file_name.endswith('.png'):
        file_path = os.path.join(directory, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('movie.gif', images)