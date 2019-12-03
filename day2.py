#!/usr/bin/python

import sys

infile = open("inputDay2.txt", "r") 

filestr = infile.read()
numbers = filestr.split(',')

lines = []
for word in numbers:
    lines.append(int(word))

length = len(lines) 
i = 0
   
# Iterating using while loop 
while i < length: 
    print lines[i]
    if lines[i] == 1:
        print "position 1: " + str(lines[i + 1]) + " value: " + str(lines[lines[i + 1]]) + " position 2: " + str(lines[i + 2]) + " value: " + str(lines[lines[i + 2]])
        add = lines[lines[i + 1]] + lines[lines[i + 2]]
        print "together they make " + str(add) + " and go in position: " + str(lines[i + 3])
        lines[lines[i + 3]] = add
    elif lines[i] == 2:
        print "position 1: " + str(lines[i + 1]) + " value: " + str(lines[lines[i + 1]]) + " position 2: " + str(lines[i + 2]) + " value: " + str(lines[lines[i + 2]])
        multiply = lines[lines[i + 1]] * lines[lines[i + 2]]
        print "together they make " + str(multiply) + " and go in position: " + str(lines[i + 3])
        lines[lines[i + 3]] = multiply
    else:
        print "Uh oh, something went wrong..."
        break
    print lines
    i += 4

print "Finished: \n"
print lines