cars = ["M5 Comp", "RS7 Performance", "C63 AMG", 
        "Carrera GTS", "Audi RS6"]

print("Innan sortering:")
for car in cars:
    print(car)

cars.sort()

print("Bilar sorterade alfabetiskt:")
for car in cars:
    print(car)

cars.sort(reverse=True)

print("Bilar i omvändordning:")
for car in cars:
    print(car)