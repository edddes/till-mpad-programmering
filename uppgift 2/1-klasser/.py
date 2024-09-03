import os


class Car:
    def __init__(self):
        self.car_list = []

    def add_car(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        
        new_car = (make, model, color)
        if new_car not in self.car_list:
            self.car_list.append(new_car)
            print(f"Tillagd: {make} {model} i färgen {color}")
        else:
            print(f"Den här bilen finns redan: {make} {model} i färgen {color}")

    def view_cars(self):
        if not self.car_list:
            print("Inga bilar i listan")
        else:
            for make, model, color in self.car_list:
                print(f"{make} - {model} - {color}")


def clear_screen():
    if os.name == "nt":
        os.system("cls")


def main():
    car_manager = Car()

    while True:
        print("Bil lista")
        print("1. Lägg till en bil")
        print("2. Visa alla bilar")
        print("3. Lämna")

        choice = input("Skriv in ditt val (1-3): ")

        if choice == '1':
            make = input("Välj bil märke: ")
            model = input("Välj bil modell: ")
            color = input("Välj färg: ")
            car_manager.add_car(make, model, color)
            input("Tryck Enter för att fortsätta")

        elif choice == '2':
            print("Bil lista:")
            car_manager.view_cars()
            input("Tryck enter för att fortsätta")

        elif choice == '3':
            print("Lämnar programmet")
            break

        else:
            print("Fel val. Försök igen")

if __name__ == "__main__":
    main()