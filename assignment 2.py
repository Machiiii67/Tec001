#1
length = float(input("Enter the length of the zander (cm): "))

if length >= 42:
    print("The zander meets the size limit.")
else:
    diff = 42 - length
    print("Release the fish back into the lake.")
    print(f"The fish is {diff} cm below the size limit.")
# 2
    cabin = input("Enter cabin class: ").upper()

    if cabin == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin == "B":
        print("Windowless cabin above the car deck.")
    elif cabin == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")
#3
    sex = input("Enter biological sex (male/female): ").lower()
    hb = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        if hb < 117:
            print("Hemoglobin level is low.")
        elif hb <= 155:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")

    elif sex == "male":
        if hb < 134:
            print("Hemoglobin level is low.")
        elif hb <= 167:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")
    else:
        print("Invalid sex input.")

#4
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")
#5
import math

# Pizza 1
d1 = float(input("Enter diameter of pizza 1 (cm): "))
p1 = float(input("Enter price of pizza 1: "))

# Pizza 2
d2 = float(input("Enter diameter of pizza 2 (cm): "))
p2 = float(input("Enter price of pizza 2: "))

# Tính diện tích (đổi cm -> m)
area1 = math.pi * (d1 / 2 / 100) ** 2
area2 = math.pi * (d2 / 2 / 100) ** 2

# Giá trên mỗi mét vuông
value1 = p1 / area1
value2 = p2 / area2

# So sánh
if value1 < value2:
    print("Pizza 1 provides better value for money.")
elif value2 < value1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same value.")

