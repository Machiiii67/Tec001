#1
class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = 0
        self.distance = 0


if __name__ == "__main__":
    input_reg = input("Enter registration number: ")
    input_speed = int(input("Enter maximum speed: "))

    car_obj = Car(input_reg, input_speed)

    print(f"Registration number: {car_obj.reg_num}")
    print(f"Maximum speed: {car_obj.max_speed} km/h")
    print(f"Current speed: {car_obj.cur_speed} km/h")
    print(f"Travelled distance: {car_obj.distance} km")
#2
class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.cur_speed += change

        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        if self.cur_speed < 0:
            self.cur_speed = 0


if __name__ == "__main__":
    input_reg = input("Enter registration number: ")
    input_speed = int(input("Enter maximum speed (km/h): "))

    car_obj = Car(input_reg, input_speed)

    car_obj.accelerate(30)
    car_obj.accelerate(70)
    car_obj.accelerate(50)

    print("Current speed:", car_obj.cur_speed, "km/h")

    car_obj.accelerate(-200)

    print("Final speed after emergency brake:", car_obj.cur_speed, "km/h")
# 3
    class Car:
        def __init__(self, reg_num, max_speed):
            self.reg_num = reg_num
            self.max_speed = max_speed
            self.cur_speed = 0
            self.travel_dist = 0
        def accelerate(self, change):
            self.cur_speed += change
            if self.cur_speed > self.max_speed:
                self.cur_speed = self.max_speed
            if self.cur_speed < 0:
                self.cur_speed = 0
        def drive(self, drive_hours):
            self.travel_dist += self.cur_speed * drive_hours
    if __name__ == "__main__":
        input_reg = input("Enter registration number: ")
        input_speed = int(input("Enter maximum speed (km/h): "))
        input_dist = float(input("Enter travelled distance (km): "))
        input_cur_speed = float(input("Enter current speed (km/h): "))
        input_hours = float(input("Enter driving time (hours): "))

        car_obj = Car(input_reg, input_speed)
        car_obj.travel_dist = input_dist
        car_obj.cur_speed = input_cur_speed
        car_obj.drive(input_hours)
        print("Registration number:", car_obj.reg_num)
        print("Maximum speed:", car_obj.max_speed, "km/h")
        print("Current speed:", car_obj.cur_speed, "km/h")
        print("Travelled distance:", car_obj.travel_dist, "km")
#4
import random
class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = 0
        self.travel_dist = 0
    def accelerate(self, change):
        self.cur_speed += change
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        if self.cur_speed < 0:
            self.cur_speed = 0
    def drive(self, drive_hours):
        self.travel_dist += self.cur_speed * drive_hours
if __name__ == "__main__":
    input_car_count = int(input("Enter number of cars: "))
    input_target_dist = float(input("Enter target distance (km): "))
    car_list = []
    for index_num in range(1, input_car_count + 1):
        car_reg = "ABC-" + str(index_num)
        car_max = random.randint(150, 200)
        car_obj = Car(car_reg, car_max)
        car_list.append(car_obj)
    used_hours = 0
    race_on = True
    while race_on:
        used_hours += 1
        for car_obj in car_list:
            random_change = random.randint(-10, 15)
            car_obj.accelerate(random_change)
            car_obj.drive(1)
            if car_obj.travel_dist >= input_target_dist:
                race_on = False
    print("Race finished in", used_hours, "hours")
    print()
    print(f"{'Registration':<15}{'Max speed':<15}{'Current speed':<15}{'Distance':<15}")
    for car_obj in car_list:
        print(f"{car_obj.reg_num:<15}{car_obj.max_speed:<15}{car_obj.cur_speed:<15}{car_obj.travel_dist:<15.1f}")
#5
if __name__ == "__main__":
    input_time_used = input("Enter the time you used for this assignment (numerical value only): ")
    file_name = "time_used.txt"

    with open(file_name, "w") as save_file:
        save_file.write(input_time_used)

    print("Your answer has been saved to", file_name)