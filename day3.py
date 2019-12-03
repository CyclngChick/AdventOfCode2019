#!/usr/bin/python

import matplotlib.pyplot as plt

infile = open("inputDay3test.txt", "r") 

lines = infile.readlines()

line1 = lines[0].rstrip()
line1 = line1.split(',')
line2 = lines[1].rstrip()
line2 = line2.split(',')

print line1

wire1current = [0,0]
points1 = []
wire2current = [0,0]
points2 = []

for value in line1:
    direction = value[0]
    length = int(value[1:len(value)])
    if direction == 'R':
        wire1current[0] += length
    elif direction == 'L':
        wire1current[0] -= length
    elif direction == 'U':
        wire1current[1] += length
    elif direction == 'D':
        wire1current[1] -= length
    print wire1current
    points1.append(wire1current[:])

print points1
points1x = []
points1y = []
for value in points1:
    points1x.append(value[0])
    points1y.append(value[1])
print points1x
print points1y

for value in line2:
    direction = value[0]
    length = int(value[1:len(value)])
    if direction == 'R':
        wire2current[0] += length
    elif direction == 'L':
        wire2current[0] -= length
    elif direction == 'U':
        wire2current[1] += length
    elif direction == 'D':
        wire2current[1] -= length
    print wire2current
    points2.append(wire2current[:])

print points2
points2x = []
points2y = []
for value in points2:
    points2x.append(value[0])
    points2y.append(value[1])
print points2x
print points2y



plt.axis([-300, 300, -300, 300])
plt.plot(0,0)
plt.plot(points1x, points1y)
plt.plot(points2x, points2y)

plt.show()