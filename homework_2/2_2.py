import random

class Kitten:

    def __init__(self, name):
        self.name = name
        self.happiness = 20
        self.satiety = 0
        self.age = 1
        self.alive = True
        self.kitten = True
        self.cat = False

    def to_chill(self):
        print("Time to chill")
        self.happiness += 3
        self.age += 0.5
        self.satiety -= 0.1

    def to_eat(self):
        print("Time to eat")
        self.happiness += 5
        self.age += 0.5
        self.satiety += 2

    def to_play(self):
        print("Time to play")
        self.happiness += 2
        self.age += 0.5
        self.satiety -= 1

    def to_sleep(self):
        print("Time to sleep")
        self.happiness += 2
        self.age += 0.5
        self.satiety -= 0.2

    def to_run(self):
        print("Time to run")
        self.happiness -= 1
        self.age += 0.5
        self.satiety -= 3

    def is_kitten(self):
        if self.satiety < -0.2:
            print("Give me some milk...")
            self.kitten = False
            self.cat = False
        elif self.happiness <= 3:
            print("Need a new family...")
            self.kitten = False
            self.cat = False
        elif self.age > 2:
            print("Become a cat...")
            self.kitten = False
            self.cat = True

    def end_of_day(self):
        print(f"happiness = {self.happiness}")
        print(f"satiety = {self.satiety}")
        print(f"age = {self.age}")

    def live(self, day):
        day = "Day" + str(day) + "Of" + self.name + "Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_chill()
        elif live_cube == 2:
            self.to_eat()
        elif live_cube == 3:
            self.to_play()
        elif live_cube == 4:
            self.to_sleep()
        elif live_cube == 5:
            self.to_run()
        self.end_of_day()
        self.is_kitten()

masya = Kitten(name="Masya")

for day in range(365):
    if masya.alive == False:
        break
    masya.live(day)

