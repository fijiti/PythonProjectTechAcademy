

# Abstraction Assignment Step 235

from abc import ABC, abstractmethod

class Pet(ABC):
    def typeOfPet(self, pet):
        print("Your pet is a", pet)
    # Astract method
    @abstractmethod
    def petSays(self, speak):
        pass

class YourPet(Pet):
    #Define implimentation of the abstract petSays method from the parent Pet class.
    def petSays(self, speak):
        print("Your pet says {}!".format(speak))

if __name__ == "__main__" :

    pet1 = YourPet()
    pet1.typeOfPet("Dog")
    pet1.petSays("Woof")

    pet2 = YourPet()
    pet2.typeOfPet("Cat")
    pet2.petSays("Meow")
              

    
