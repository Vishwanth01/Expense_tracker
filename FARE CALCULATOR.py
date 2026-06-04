# The "FARE CALCULATOR" Travel optimizer
rates = {'ECONOMY': 10, 'PREMIUM': 18, 'SUV': 25}
print("=====> Welcome to Travel Agnecy <=========")
print("RATES = ", rates)

vehicle_type = input("Enter the Vehicle type: ").upper()

if vehicle_type not in rates:
    print("Service not Available")
    exit()

hour = int(input("Enter start Hour of the day (0-23): "))
km = int(input("Enter the travelled Kilometers: "))

def calculate_Fare(vehicle_type, hour, km):
    base_price = rates[vehicle_type] * km
    if 17<= hour<=20:
        surge_price = base_price * 1.5
        return price
    else:
        return base_price
    
fare = calculate_Fare(vehicle_type, hour, km)
print(fare)