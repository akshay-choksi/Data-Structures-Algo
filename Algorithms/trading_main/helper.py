import math

'''
Akshay Choksi (ajc9yr)
10/13/2022
Module 3: Galactic Trade Routes
helper.py: main divide and conquer algorithm
'''

def distance(star_x, star_y, i, j):
        return ((star_x[i] - star_x[j])*(star_x[i] - star_x[j])) + (star_y[i] - star_y[j])*(star_y[i] - star_y[j])

def brute_force(star_x, star_y, points):
    min_dist = float("inf")
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            min_dist = min(distance(star_x, star_y, points[i], points[j]), min_dist)
    return min_dist

def divide_and_conquer(points, star_x, star_y):
    if len(points) <= 5:
        return brute_force(star_x, star_y, points) 

    pivot = (len(points)//2) #maybe round up?
    l,r = points[:pivot], points[pivot:]

    #divide
    min_dist = min(divide_and_conquer(l, star_x, star_y), divide_and_conquer(r, star_x, star_y))

    #check strip of values across divide line (within minimum distance)
    strip = []
    for val in points:
        if abs(star_x[pivot] - star_x[val]) < min_dist:
            strip.append(val)
    return min(min_dist, brute_force(star_x, star_y, strip))