#!/usr/bin/python

import math

infile = open("inputDay1.txt", "r") 

lines = infile.readlines()

totalFuelRequirement = 0;
for line in lines:
    number = float(line)
    print "Number is: " + str(number)
    fuelRequirement = math.floor(number / 3) - 2
    print "Fuel requirement is: " + str(fuelRequirement)
    totalFuelRequirement += fuelRequirement
    while fuelRequirement > 0:
        fuelRequirement = math.floor(fuelRequirement / 3) - 2
        print "Fuel requirement for the fuel is: " + str(fuelRequirement)
        if fuelRequirement > 0:
            totalFuelRequirement += fuelRequirement


print "Total Fuel Requirement is: " + str(totalFuelRequirement)

#Test outcome:
#51316