class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        # print animal details
        print(f"{self.name} | Health: {self.health} | Happiness: {self.happiness}")

    def feed(self):
        # default behavior (can be overridden)
        self.health += 5
        self.happiness += 5


class Lion(Animal):
    def __init__(self, name, age, health, happiness, speed):
        super().__init__(name, age, health, happiness)
        self.speed = speed

    def feed(self):
        self.health += 10
        self.happiness += 5


class Monkey(Animal):
    def __init__(self, name, age, health, happiness, favorite_food):
        super().__init__(name, age, health, happiness)
        self.favorite_food = favorite_food

    def feed(self):
        self.health += 20
        self.happiness += 18


class Bear(Animal):
    def __init__(self, name, age, health, happiness, weight):
        super().__init__(name, age, health, happiness)
        self.weight = weight

    def feed(self):
        self.health += 20
        self.happiness += 12


class Tiger(Animal):
    def __init__(self, name, age, health, happiness, color):
        super().__init__(name, age, health, happiness)
        self.color = color

    def feed(self):
        self.health += 15   
        self.happiness += 14


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []# store animals

    def add_animal(self, animal):
            # add animal to zoo
        self.animals.append(animal)

    def show_animals(self):
        print(f"\n--- {self.name} ---")
        for animal in self.animals:
            animal.display_info()

    def feed_all(self):
    
        print("\nFeeding all animals...\n")
        for animal in self.animals:
            animal.feed()   #polymorphism happens here



zoo = Zoo("John's Zoo")

zoo.add_animal(Lion("Simba", 5, 50, 40, 80))
zoo.add_animal(Monkey("George", 3, 40, 60, "Banana"))
zoo.add_animal(Bear("Baloo", 7, 70, 50, 300))
zoo.add_animal(Tiger("Rajah", 6, 65, 45, "Orange"))

zoo.show_animals()
zoo.feed_all()
zoo.show_animals()