# Assignment for Python Step 185

class Vehicle:
    engineType = ""
    wheelsCount = 0
    doorsCount = 0
    def __init__(self, engineType, wheelsCount, doorsCount):
        self.engineType = engineType
        self.wheelsCount = wheelsCount
        self.doorsCount


class Airplane(Vehicle):
    wingCount = 2
    purpose = "Comercial"
    def __init__(self, engineType, wheelsCount, doorsCount, wingCount, purpose):
        super().__init__(engineType, wheelsCount, doorsCount)
        self.wingCount = wingCount
        self.purpose = purpose
    

class Helicopter(Vehicle):
    propellers = 1
    landingGear = ""
    def __init__(self, engineType, wheelsCount, doorsCount, propellers, landingGear):
        super().__init__(engineType, wheelsCount, doorsCount)
        self.propellers = propellers
        self.landingGear = landingGear

aCopter = Helicopter('Gasoline', 0, 2, 2, 'Hydraulic')

aPlane = Airplane('Rocket', 3, 1, 2, 'Military')

print("Helicopter: \nEngine type: {}\nWheel Count: {}\nDoor Count: {}\
        \nPropellers: {}\nLanding Gear: {}\n".format(
        aCopter.engineType, aCopter.wheelsCount, aCopter.doorsCount,
        aCopter.propellers, aCopter.landingGear))

print("Airplane: \nEngine type: {}\nWheel Count: {}\
        \nDoor Count: {}\nPropellers: {}\nLanding Gear: {}\n".format(
        aPlane.engineType, aPlane.wheelsCount, aPlane.doorsCount,
        aPlane.wingCount, aPlane.purpose))





    
    
