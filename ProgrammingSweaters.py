# ProgrammingSweaters.py
# ICS201 Vashisht
# February 03 2021

sweaterCount = int(input("How many sweaters would you like to buy? ")) + 1 # Asks user to input number of sweaters they want to buy (adds 1 for proper formatting)

# Loops i)
i = 1 # Declares i as 1

for i in range(1, sweaterCount): # Loops i, number-of-sweaters times
    print(i, "sweater(s) cost $", i * 40) # Multiplies i (number of sweaters) by forty and prints out price
    i += 1 # Adds one to i each time 
