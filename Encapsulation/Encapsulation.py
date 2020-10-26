# Assigment Step 234 Encapsulation

class Car:
    def __init__(self):
        self._doorCount = 2
        self.__engineType = "gas"

    def getEngineType(self):
            print(self.__engineType.title())

    def setEngineType(self, engine):
        self.__engineType = engine
    
    

if __name__ == "__main__":
    print("Created redCar and accessing and changing doorCount a protected attribute:")
    redCar = Car()
    print("Before: {}".format(redCar._doorCount))
    redCar._doorCount = 4
    print("After Changed: {}".format(redCar._doorCount))

    print("\nAccessing and changing redCar engineType a private attribute:")
    print("Before:")
    redCar.getEngineType()
    redCar.setEngineType('electric')
    print("After Changed:")
    redCar.getEngineType()
    
    
    
