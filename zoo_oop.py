class Animal():
    def __init__(self, name, age, isMamal): #constructor
        self.name = name
        self.age = age
        self.isMamal = isMamal
    
    def __str__(self): #return string representation
        if self.isMamal == True: 

            return f"{self.name} is {self.age} years old, and it is mamal"
        else:
            return f"{self.name} is {self.age} years old, and it is not mamal"

class Breed(Animal):
    def __init__(self, name, age, isMamal, breed):
        Animal.__init__(self, name, age, isMamal) #get inheritance from Animal parent class
        self.breed = breed

        # def __str__(self):
        #     return f"{self.name} is mamal: {self.isMamal}"
        
    def mamal(self):
        if self.isMamal == True:
            return f"{self.name} is mamal, it give birth to {self.breed} children"
        else:
            return f"{self.name} is not mamal and it give birth to {self.breed} eggs"



lion = Animal('Lion', 20, True)
eagle = Breed('Eagle', 15, False, 4)

print(lion)
print(eagle)
print(eagle.mamal())