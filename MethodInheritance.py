

# Asignment Python Polymorphism Step 193

# Parent Class
class Building:
    name = "Unknown"
    style = "Unknown"
    doors = 0
    price = 0

    def rentBuilding(self):
        msg = "\nName: {}\Style: {}\nDoors: {}\nPrice: {}"
        return msg

# Child instance of Building
class Home(Building):
    name = "Johnson's House"
    style = "Ranch"
    doors = 2
    price = 1500
    bedrooms = 3
    bathrooms = 2
    

    def rentBuilding(self):
        msg = "\nRental Home: \nName: {}\nStyle: {}\Doors: {}\nBedrooms: {}\nBathrooms: {} \
                \nPrice: ${} Per Month".format(self.name, self.style, self.doors, self.bedrooms, self.bathrooms, self.price)
        return msg

# Another child instance of Building
class Gymnasium(Building):
    name = "Acme Gym"
    style = "Gym"
    doors = 4
    price = 500
    sport = "Basketball"
    courts = 1

    def rentBuilding(self):
        msg = "\nRental Gym: \nName: {}\nStyle: {}\nDoors: {}\nSport: {}\nCourts: {} \
                \nPrice: ${} Per Night".format(self.name, self.style, self.doors, self.sport, self.courts, self.price)
        return msg
    

if __name__ == "__main__":

    homeRental = Home()
    print(homeRental.rentBuilding())

    gymRental = Gymnasium()
    print(gymRental.rentBuilding())

        
