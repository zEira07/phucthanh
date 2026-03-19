import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# =========================
# CREATE 10 CARS
# =========================
cars = []

for i in range(1, 11):
    reg = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))


# =========================
# RACE LOOP
# =========================
race_finished = False
hours = 0

while not race_finished:
    hours += 1

    for car in cars:
        # Random speed change
        change = random.randint(-10, 15)
        car.accelerate(change)

        # Drive for 1 hour
        car.drive(1)

        # Check if race ends
        if car.travelled_distance >= 10000:
            race_finished = True


# =========================
# PRINT RESULT TABLE
# =========================
print(f"\nRace finished in {hours} hours\n")

print(f"{'Reg':<10} {'MaxSpeed':<10} {'Speed':<10} {'Distance':<15}")
print("-" * 50)

for car in cars:
    print(f"{car.registration_number:<10} "
          f"{car.max_speed:<10} "
          f"{car.current_speed:<10} "
          f"{round(car.travelled_distance, 2):<15}")