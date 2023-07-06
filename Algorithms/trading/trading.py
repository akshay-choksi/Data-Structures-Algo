'''
Akshay Choksi (ajc9yr)
10/13/2022
Module 3: Galactic Trade Routes
'''
#optimizations
#try using key = lambda planet: planet.x (sort) 

import math

#distance formula (not sqrt)
def distance(a,b):
    x0, x1 = a
    y0, y1 = b
    return (((x0-y0)*(x0-y0)) + ((x1-y1)*(x1-y1)))

#when length of array is small enough, calculate the min value(conquer)
#n^2 runtime
def brute_force(arr):
    length = len(arr)
    #value max is under 10,000 ^ 2
    min = 100000001
    for i in range(length):
        for j in range(i + 1, length):
            check = distance(arr[i], arr[j])
            if check < min:
                min = check
    return min

#calculate points across pivot
def pivot_dist(arr, dist):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[j][1] - arr[i][1] >= dist):
                dist = distance(arr[i], arr[j])
            else:
                continue
    return dist

#helper function make a new array with same elements
# n runtime
def makeCopy(arr):
    ret = []
    for val in arr:
        ret.append(val)
    return ret

def closest(points, pointsCopy, n):
    #could change for TLE
    if n <= 200:
        return brute_force(points)
    #divide and conquer
    points2 = points[:(n//2)]
    points3 = points[(n//2):]
    min1, min2 = closest(points2, pointsCopy, n//2), closest(points3, pointsCopy, n - (n//2))
    #smallest val
    dist = min(min1, min2)

    #call strip function
    strip= []
    mid = points[n//2]

    #add valid points
    for i in range(n):
        if abs(mid[0] - points[i][0]< dist):
            strip.append(points[i])
    strip.sort(key = lambda point: point[1])
    a = min(dist, pivot_dist(strip, dist))
    return a

def close_run(coordinates):
    length = len(coordinates)
    coordinates_copy = makeCopy(coordinates)
    return closest(coordinates,coordinates_copy, length)    

def read_input():
    ret = []
    while(True):
    #build coordinates list
        n = int(input())
        if n == 0:
            break
        coordinates = []
        for i in range(n):
            x,y = input().split()
            x, y = float(x), float(y)
            coordinates.append([x,y])
        coordinates.sort(key=lambda point:point[0])
        #run divide and conquer algorithm
        val = close_run(coordinates)
        ret.append(val)
    
    return ret


vals = (read_input())
for val in vals:
    val = math.sqrt(val)
    # val = round(val, 4)
    if val <= 10000:
        print(f"{val:.4f}")
    else:
        print("infinity")
    