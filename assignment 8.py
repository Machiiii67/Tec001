#1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print("Going up -> floor", self.current)

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print("Going down -> floor", self.current)

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()
e = Elevator(1, 10)
e.go_to_floor(5)
e.go_to_floor(1)
#2 +3
class Building:
    def __init__(self, bottom, top, total_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for i in range(total_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, index, target):
        if index < 0 or index >= len(self.elevators):
            print("Invalid elevator")
            return

        print("Using elevator", index)
        self.elevators[index].go_to_floor(target)

    def fire_alarm(self):
        print("!!! FIRE ALARM !!!")
        for i, e in enumerate(self.elevators):
            print("Reset elevator", i)
            e.go_to_floor(self.bottom)
#4
import random
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0
    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours

class Race:
    def __init__(self, name, total_km, cars):
        self.name = name
        self.total_km = total_km
        self.cars = cars
        self.time = 0

    def hour_passes(self):
        self.time += 1

        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.total_km:
                return True
        return False

    def print_status(self):
        print("\nTime:", self.time)
        print("Reg\tSpeed\tDistance")

        for car in self.cars:
            print(car.reg_number, "\t", car.speed, "\t", car.distance)
cars = []
for i in range(10):
    reg = "phong-" + str(i + 1)
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))
race = Race("Grand Demolition Derby", 10000, cars)
while not race.race_finished():
    race.hour_passes()
race.print_status()
print("\nRace finished in", race.time, "hours")