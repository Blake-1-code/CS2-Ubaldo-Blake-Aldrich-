Version 2 of code 
FARE_RATE = 14

name = input("Enter passenger name: ").strip()
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

if name == "":
    print("Error: Passenger name cannot be empty.")
elif distance <= 0:
    print("Error: Distance must be a number greater than 0.")
elif passengers <= 0:
    print("Error: Passengers must be a positive whole number.")
else:
    total_fare = distance * FARE_RATE * passengers
    
    print("\nPassenger:", name)
    print("Total Fare: PHP", round(total_fare, 2))
