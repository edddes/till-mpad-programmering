class Car:
    def __init__(self):
        self.car_details = {} #dictionary (ordbok)
        self.count = 0

    def add_car(self, make, model):
        if make in self.car_details:
            self.car_details[make].append(model)
        else:
            self.car_details[make] = [model]

    def remove_car(self, make, model):
        if make in self.car_details:
            if model in self.car_details[make]:
                self.car_details[make].remove(model)
                if not self.car_details[make]:
                    del self.car_details[make]
                    return True
        return False

    def list_cars(self):
        for make in self.car_details:
            print(make)

    def list_cars_detailed(self):
        self.count = 0
        for make, models in self.car_details.items():
            for model in models:
                self.count += 1
                print(f"{self.count}. {make} - {model}")

car = Car()
car.add_car("Porsche", "911 GT3")
car.add_car("Porsche", "Cayman")
car.add_car("Porsche", "Cayenne")
car.list_cars()
print("----------------------------")  #mest prydnat för att man ska se skillnad mellan de i listan och de som tas bort 
car.list_cars_detailed()
print("----------------------------") 
car.remove_car("Porsche", "Cayman")
car.list_cars_detailed()