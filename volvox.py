# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:32:03 2021
Achmad Zacky Fairuza
Septian Ulan Dini
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import math

#%%
          
def constructVolvox(cell_number, radius, 
                    x_center, y_center, z_center):
    n = cell_number
    goldenRatio = (1 + 5**0.5)/2
    i = np.arange(0,n)
    psi = 2*np.pi*i /goldenRatio
    theta = np.arccos(1 - 2*(i + 0.5)/n)
    x = (radius*np.cos(psi)*np.sin(theta)) + x_center 
    y = (radius*np.cos(theta)) + y_center 
    z = (radius*np.sin(psi)*np.sin(theta)) - z_center
    cell_location = combineLocation(x, y, z, x_center, y_center, z_center) 
    return cell_location

def combineLocation(x, y, z, x_center, y_center, z_center):
    x_length = len(x)
    y_length = len(y)
    z_length = len(z)
    cell_location = []
    if x_length != y_length or x_length != z_length or y_length != z_length:
        print("size mismatch")
        return cell_location
    else:
        for i in range(x_length):
            location = [x[i], y[i], z[i], x_center, y_center, z_center]
            cell_location.append(location)
        return cell_location

def drawCell(cell_location, dot_radius,
             perspective):
    for cell in cell_location:
        x_pos = cell[0]
        y_pos = cell[1]
        z_pos = cell[2]        
        scale_projected = perspective/(perspective + z_pos)
        x_projected = (x_pos * scale_projected)
        y_projected = (y_pos * scale_projected)
        r_projected = (dot_radius * scale_projected)
        
        circle = plt.Circle((x_projected,y_projected), r_projected, color = 'g' )
        plt.gca().add_patch(circle)

def xRollVolvox(cell_location, angle=5):
    new_cell_location = []
    angle = math.radians(angle)
    for i in range(len(cell_location)):
        x_old = cell_location[i][0]
        y_old = cell_location[i][1]
        z_old = cell_location[i][2]
        x_center = cell_location[i][3]
        y_center = cell_location[i][4]
        z_center = cell_location[i][5]
        
        x_rel = x_old - x_center
        y_rel = y_old - y_center
        z_rel = z_old + z_center
        
        x_rel_new = x_rel
        y_rel_new = y_rel*math.cos(angle) - z_rel*math.sin(angle)
        z_rel_new = y_rel*math.sin(angle) + z_rel*math.cos(angle)
        
        x_new = x_rel_new + x_center
        y_new = y_rel_new + y_center
        z_new = z_rel_new - z_center
        
        x_new = round(x_new, 3)
        y_new = round(y_new, 3)
        z_new = round(z_new, 3)
        
        new_cell_location.append([x_new, y_new, z_new, x_center, y_center, z_center])
    return new_cell_location

def yRollVolvox(cell_location, angle=5):
    new_cell_location = []
    angle = math.radians(angle)
    for i in range(len(cell_location)):
        x_old = cell_location[i][0]
        y_old = cell_location[i][1]
        z_old = cell_location[i][2]
        x_center = cell_location[i][3]
        y_center = cell_location[i][4]
        z_center = cell_location[i][5]
        
        x_rel = x_old - x_center
        y_rel = y_old - y_center
        z_rel = z_old + z_center
        
        x_rel_new = x_rel*math.cos(angle) + z_rel*math.sin(angle)
        y_rel_new = y_rel
        z_rel_new = z_rel*math.cos(angle) - x_rel*math.sin(angle)
        
        x_new = x_rel_new + x_center
        y_new = y_rel_new + y_center
        z_new = z_rel_new - z_center
        
        x_new = round(x_new, 3)
        y_new = round(y_new, 3)
        z_new = round(z_new, 3)
        
        new_cell_location.append([x_new, y_new, z_new, x_center, y_center, z_center])
    return new_cell_location

def zRollVolvox(cell_location,  angle=5):
    new_cell_location = []
    angle = math.radians(angle)
    for i in range(len(cell_location)):
        x_old = cell_location[i][0]
        y_old = cell_location[i][1]
        z_old = cell_location[i][2]
        x_center = cell_location[i][3]
        y_center = cell_location[i][4]
        z_center = cell_location[i][5]
        
        x_rel = x_old - x_center
        y_rel = y_old - y_center
        z_rel = z_old + z_center
        
        x_rel_new = x_rel*math.cos(angle) - y_rel*math.sin(angle)
        y_rel_new = x_rel*math.sin(angle) + y_rel*math.cos(angle)
        z_rel_new = z_rel
        
        x_new = x_rel_new + x_center
        y_new = y_rel_new + y_center
        z_new = z_rel_new - z_center
        
        x_new = round(x_new, 3)
        y_new = round(y_new, 3)
        z_new = round(z_new, 3)
        
        new_cell_location.append([x_new, y_new, z_new, x_center, y_center, z_center])
    return new_cell_location

def xMoveVolvox(cell_location, distance=1):
    new_cell_location = []
    for i in range(len(cell_location)):
        x_old = cell_location[i][0]
        y_old = cell_location[i][1]
        z_old = cell_location[i][2]
        x_center = cell_location[i][3]
        y_center = cell_location[i][4]
        z_center = cell_location[i][5]
        
        x_new = x_old + distance
        y_new = y_old
        z_new = z_old
        x_center_new = x_center + distance
        y_center_new = y_center 
        z_center_new = z_center
        
        x_new = round(x_new, 3)
        y_new = round(y_new, 3)
        z_new = round(z_new, 3)
        x_center_new = round(x_center_new, 3)
        y_center_new = round(y_center_new, 3)
        z_center_new = round(z_center_new, 3)
        
        new_cell_location.append([x_new, y_new, z_new, x_center_new, y_center_new, z_center_new])
    return new_cell_location

def yMoveVolvox(cell_location, distance=1):
    new_cell_location = []
    for i in range(len(cell_location)):
        x_old = cell_location[i][0]
        y_old = cell_location[i][1]
        z_old = cell_location[i][2]
        x_center = cell_location[i][3]
        y_center = cell_location[i][4]
        z_center = cell_location[i][5]
        
        x_new = x_old
        y_new = y_old + distance
        z_new = z_old
        x_center_new = x_center
        y_center_new = y_center + distance
        z_center_new = z_center
        
        x_new = round(x_new, 3)
        y_new = round(y_new, 3)
        z_new = round(z_new, 3)
        x_center_new = round(x_center_new, 3)
        y_center_new = round(y_center_new, 3)
        z_center_new = round(z_center_new, 3)
        
        new_cell_location.append([x_new, y_new, z_new, x_center_new, y_center_new, z_center_new])
    return new_cell_location

def zMoveVolvox(cell_location, distance=1):
    new_cell_location = []
    for i in range(len(cell_location)):
       x_old = cell_location[i][0]
       y_old = cell_location[i][1]
       z_old = cell_location[i][2]
       x_center = cell_location[i][3]
       y_center = cell_location[i][4]
       z_center = cell_location[i][5]
       
       x_new = x_old
       y_new = y_old
       z_new = z_old - distance
       x_center_new = x_center
       y_center_new = y_center 
       z_center_new = z_center + distance
       
       x_new = round(x_new, 3)
       y_new = round(y_new, 3)
       z_new = round(z_new, 3)
       x_center_new = round(x_center_new, 3)
       y_center_new = round(y_center_new, 3)
       z_center_new = round(z_center_new, 3)
       
       new_cell_location.append([x_new, y_new, z_new, x_center_new, y_center_new, z_center_new])
    return new_cell_location

def drawShow(xmin=20, xmax=20, ymin=20, ymax=20):
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    
#%%   
dot_radius = 1
radius = 80
x_center = 0
y_center = 0
z_center = 0
perspective = 130
cell_number = 1000
xmin = -150
xmax = 150
ymin = -150
ymax = 150


print("start constructing")
cell_location = constructVolvox(cell_number, radius, x_center, y_center, z_center)
print("volvox has been constructed")
print("proceed to draw the volvox")
drawCell(cell_location, dot_radius, perspective)
print("drawing cell done")
drawShow(xmin, xmax, ymin, ymax)
print("showing image")

for t in range(50):
    cell_location = zRollVolvox(cell_location, 5)
    cell_location = yMoveVolvox(cell_location, 1)
    cell_location = zMoveVolvox(cell_location, 2)
    drawCell(cell_location, dot_radius, perspective)
    drawShow(xmin, xmax, ymin, ymax)



