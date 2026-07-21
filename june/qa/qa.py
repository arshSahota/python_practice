energy_usage = {
    "BuildingA": 1200,
    "BuildingB": 980,
    "BuildingC": 1450,
    "BuildingD": 850
}

#energy usage for building C?

print(energy_usage["BuildingC"])

#q2 => Building D

#q3 => building name 
# it will print Building A, BuildingC

#Q4 => Delta energy Dashboard
#It may have been a bug since this is the energy usage per building and can 't be negative
#I would write an assertion to check if every reading is greater than or equal to 0

