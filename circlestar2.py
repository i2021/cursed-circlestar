# importing necessary libraries
import math

import matplotlib.pyplot as plt

# declaring the radii of small and big circles
while True:
    smallR = input("Radius of inner circle: (default --> 3) ") or 3
    try:
        smallR = int(smallR)
        print("Radius is an integer.")
        print("Using radius: ", smallR)
        break
    except ValueError:
        try:
            float(smallR)
            print("Radius is a float.")
            print("Using inner radius: ", smallR)
            break
        except ValueError:
            print("This is not a valid radius. Please enter a valid number")

while True:
    bigR = input("Radius of outer circle: (default --> 24) ") or 24
    try:
        bigR = int(bigR)
        print("Radius is an integer.")
        print("Using radius: ", bigR)
        break
    except ValueError:
        try:
            float(bigR)
            print("Radius is a float.")
            print("Using outer radius: ", bigR)
            break
        except ValueError:
            print("This is not a valid radius. Please enter a valid number")

# find the perimeter of circle
perimeterSmall = 2 * math.pi * smallR

# start = 1
# stop = 100
# step = 1
# I added for loop for some reason...
for i in range(1, 10000, 10):
    # find the arc length of one triangle
    triangles = i
    arcLen = perimeterSmall / triangles

    # subdivide the crystal
    halfArcLen = arcLen / 2

    # find the angle between b & c (smallR & bigR)
    theta = halfArcLen / ((math.pi / 180) / smallR)

    # find the missing side
    sideA = math.sqrt((smallR ** 2) + (bigR ** 2) - (2 * smallR * bigR) * math.cos(theta))

    # find the area using Heron's Formula
    # c --> bigR
    # b --> smallR
    # a --> sideA
    s = (sideA + smallR + bigR) / 2
    areaHalfCrystal = math.sqrt(s * (s - sideA) * (s - smallR) * (s - bigR))

    # find the full area
    fullArea = (areaHalfCrystal * 2) * triangles

    # plotting the points on the graph
    # x --> triangles
    # y --> fullArea
    print(" Area of this cursed star with ", triangles, "triangles is", fullArea)
    plt.plot(triangles, fullArea, marker="o", markersize=2, markeredgecolor="red", markerfacecolor="red")

# display the graph :D
plt.show()
