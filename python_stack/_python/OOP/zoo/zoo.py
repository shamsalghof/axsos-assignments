class Animal:
    def __init__(self,name,age,health_care,happiness_level):
        self.name=name
        self.age=age
        self.health_care=health_care
        self.happiness_level=happiness_level

    def display_info(self):
        print(f"This Animal is : {self.name} , Health Care is : {self.health_care} and Happiness Level is: {self.happiness_level}")

    def feed(self,health_care,happiness_level):
        self.health_care=health_care+10;
        self.happiness_level=happiness_level+10;

class Lion(Animal):
    def __init__(self, speed,name, age, health_care, happiness_level,):
        super().__init__(name, age, health_care, happiness_level)
        self.speed=speed
    
    def display_info(self):
        return super().display_info()

    def feed(self):
        self.happiness_level+=5
        self.health_care+=10

class Monkey(Animal):
    def __init__(self, favourite_food,name, age, health_care, happiness_level):
        super().__init__(name, age, health_care, happiness_level)
        self.favourite_food=favourite_food

    def display_info(self):
        return super().display_info()

    def feed(self):
        self.happiness_level+=18
        self.health_care+=20

class Bear(Animal):
    def __init__(self, weight,name, age, health_care, happiness_level):
        super().__init__(name, age, health_care, happiness_level)
        self.weight=weight

    def display_info(self):
        return super().display_info()

    def feed(self):
        self.happiness_level+=12
        self.health_care+=20
class Tiger(Animal):
    def __init__(self, color,name, age, health_care, happiness_level):
        super().__init__(name, age, health_care, happiness_level)
        self.color=color

    def display_info(self):
        return super().display_info()

    def feed(self):
        self.happiness_level+=14
        self.health_care=+15

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()

    def feed_all(self):
    # polymorphism: each animal has its own feed() behavior
        for animal in self.animals:
            animal.feed()

lion1 = Lion(100,"Nala",12,10,15)
lion2=Lion(150,"Simba",15,14,12)
tiger1 = Tiger("yellow","Rajah",21,18,17)
tiger2=Tiger("yellow","sherekhan",21,18,17)

zoo1 = Zoo("John's Zoo")
zoo1.add_animal(lion1)
zoo1.add_animal(lion2)
zoo1.add_animal(tiger1)
zoo1.add_animal(tiger2)
zoo1.print_all_info()
zoo1.feed_all()
zoo1.print_all_info()
