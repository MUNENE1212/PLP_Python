# Assignment 1: Family Class Design 👨‍👩‍👧

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi! I'm {self.name}, I'm {self.age} years old."

class Parent(Person):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    
    def work(self):
        print(f"{self.name} is working as a {self.job}")

class Child(Person):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def play(self):
        print(f"{self.name} is playing and having fun!")

# Activity 2: Polymorphism Challenge - Animals 🐾

class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f"{self.name} moves"

class Dog(Animal):
    def move(self):
        return f"🐕 {self.name} is running!"

class Cat(Animal):
    def move(self):
        return f"🐱 {self.name} is walking gracefully!"

class Bird(Animal):
    def move(self):
        return f"🐦 {self.name} is flying!"

# Demo
dad = Parent("Dad", 28, "Engineer")
mom = Parent("Mom", 24, "Teacher")
daughter = Child("Wincy", 3, "Kindergaten")
print(dad.introduce())
print(mom.introduce())
print(daughter.introduce())

dad.work()
daughter.play()

print("\nPolymorphism Demo:")
animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Tweet")]
for animal in animals:
    print(animal.move())