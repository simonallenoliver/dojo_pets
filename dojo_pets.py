
# Create a Pet class with the pet attributes listed above.
class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 100
        self.energy = 80

# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
# noise() - prints out the pet's sound
    def noise(self):
        print(self.sound)

# Create a Ninja class with the ninja attributes listed above.
class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats 
        self.pet_food = pet_food

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()



fluffy = Pet("Fluffy","dog","Sit","Oink")
simon = Ninja("Simon","Oliver",fluffy,"bone","pasta")

simon.feed()
simon.bathe()