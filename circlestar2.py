# importing nessesarrry libraries
import math
import array
import matplotlib.pyplot as plt

# declaring the radii of small and big circles
smallR = 3
bigR = 24

# find the perimiter of circle
perimiterSmall = 2 * math.pi * smallR

# start = 1
# stop = 100
# step = 1
# I added for loop for some reason...
for i in range (1, 100000, 100):

# find the arc lenght of one triangle
    triangles = i
    arcLen = perimiterSmall / triangles

# find the angle between b & c (smallR & bigR)
    theta = arcLen / ((math.pi / 180) / smallR)

# find the missing side
    sideA = math.sqrt((smallR**2) + (bigR**2) - (2* smallR* bigR) * math.cos(theta))

# find the area using Heron's Formula 
# c --> bigR
# b --> smallR
# a --> sideA
    s = (sideA + smallR + bigR) / 2
    areaHalfCrystal = math.sqrt(s*(s-sideA)*(s-smallR)*(s-bigR))

# find the full area
    fullArea = (areaHalfCrystal * 2) * triangles

# plotting the points on the graph
# x --> triangles
# y --> fullArea
#    print(" Area of this cuursed star is: ", fullArea)
    plt.plot(triangles, fullArea, marker="o", markersize=2, markeredgecolor="red", markerfacecolor="red") 

# display the graph :D
plt.show()