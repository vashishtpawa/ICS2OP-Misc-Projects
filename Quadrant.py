# Quadrant.py
# ICS201 Vashisht
# January 23 2021

# Asks for x, y coords
x = float(input("Enter an x coordinate: ")) # Asks for x coord
y = float(input("Enter a y coordinate: ")) # Asks for y coord

if(x > 0 and y > 0):
    print("\nYour point is in Quadrant 1.") # Quad. 1 if both x, y positive

elif(x > 0 and y < 0):
    print("\nYour point is in Quadrant 2.") # Quad. 2 if x positive, y negative

elif(x < 0 and y < 0):
    print("\nYour point is in Quadrant 3.") # Quad. 3 if x negative, y positive

elif(x < 0 and y > 0):
    print("\nYour point is in Quadrant 4.") # Quad. 4 if both x, y negative

elif(x = 0 and y = 0)
    print("\nYour point is the Origin.") # Origin Point if both x, y equal to 0
