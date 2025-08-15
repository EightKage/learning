import random

class Animal:
    info = "a living organism that has ego"

    def __init__(self, name):
        print("an animal is crated by god")
        self.name = name


class Dog(Animal):
    info = "A domesticated animal that is mans best friend"
    def __init__(self, name):
       super().__init__(name)
       print("im alive again?")
       self.lucky_number = random.randint(1,10)
       self.fur = ""
       

    def bark(self):
        print(f"woof woof my name is {self.name} and my number is {self.lucky_number}")

   
class Bulldog(Dog):
    
    def __init__(self, name):
        super().__init__(name)
        print("a bulldog is created")






dog1 = Dog("butters")
dog2 = Dog("Sarah")

print(dog1.info)
