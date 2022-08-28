maxParkingSpots = 5  # Constant   - should be 20 in final program
minAccessibleSpots = 2  # Constant  - should be 5

spotsAvailable = [1 for j in range(15)]  # Task1
spotsAccessible = [1 for j in range(15)]  # Task2
spotsGeneral = [maxParkingSpots for j in range(15)]  # Task2
bookedParking = [["--" for j in range(15)] for j in range(21)]  # Task1 and 2


def displayGrid2():  # Ignore this code - it is only used to display content of arrays so far - not needed for exam
    global spotsGeneral, spotsAccessible, bookedParking, maxParkingSpots 
    print("NEXT SPOT AVAILABLE PER DAY")
    print(" "*2, end="|")
    for col in range(1, 15):
        print("DAY %2d" % col, end="  |")
    print("\n", "-"*130, "\n  |", end="")
    for col in range(1, 15):
        print(" "*2, "%3d" % spotsGeneral[col], end="  |")
    print("\n  |", end="")
    for col in range(1, 15):
        print(" "*2, "%3d" % spotsAccessible[col], end="  |")

    print("\n\nBOOKED PARKING")
    print(" "*2, end="|")
    for col in range(1, 15):
        print("%6d" % col, end="  |")
    print("\n", "-"*130)
    for row in range(1, maxParkingSpots+1):
        print("%2d" % row, end="|")
        for col in range(1, 15):
            print(" ", bookedParking[row][col], " " *
                  (5 - len(bookedParking[row][col])), end="|")
        print()


def displayGrid1():
    global spotsAvailable
    print("NEXT SPOT AVAILABLE PER DAY")
    print(" "*2, end="|")
    for col in range(1, 15):
        print("DAY %2d" % col, end="  |")
    print("\n", "-"*130, "\n  |", end="")
    for col in range(1, 15):
        print(" "*2, "%3d" % spotsAvailable[col], end="  |")
    print("\n\nBOOKED PARKING")
    print(" "*2, end="|")
    for col in range(1, 15):
        print("%6d" % col, end="  |")
    print("\n", "-"*130)
    for row in range(1, maxParkingSpots):
        print("%2d" % row, end="|")
        for col in range(1, 15):
            print(" ", bookedParking[row][col], " " *
                  (5 - len(bookedParking[row][col])), end="|")
        print()


def readFromFile():
    global spotsAccessible, spotsGeneral
    file = open("parking.txt", "r")
    for j in range(5):
        line = file.readline()
        line = line.strip()
        day, spot, name = line.split(",")
        bookedParking[int(spot)][int(day)] = name

    line = file.readline()
    line = line.strip()
    spotsAccessible = line.split(",")
    line = file.readline()
    line = line.strip()
    spotsGeneral = line.split(",")
    for j in range(15):
        spotsAccessible[j] = int(spotsAccessible[j])
        spotsGeneral[j] = int(spotsGeneral[j])
    file.close()
