class Dog:
    def __init__(self, name, age, gender, sound):
        self.name = name
        self.age = age
        self.gender = gender
        self.sound = sound

    def bark(self):
        print(self.sound)
    def eat(self):
        print(f"{self.name} is eating")

dog1 = Dog("jessi", 7, "girl", "WOOF")
dog1.bark()
dog1.eat()
dog2 = Dog("petty", 8, "girl", "WOOOW")
dog2.bark()
dog2.eat()