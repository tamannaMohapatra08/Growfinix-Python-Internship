print("=== TOUR PACKAGE GENERATOR ===")

destination = input("Enter Destination: ")
budget = int(input("Enter Your Budget: "))

if budget >= 50000:
    package = "Luxury Package"
    days = 7
    hotel = "5-Star Hotel"

elif budget >= 25000:
    package = "Standard Package"
    days = 5
    hotel = "3-Star Hotel"

else:
    package = "Budget Package"
    days = 3
    hotel = "Budget Hotel"

print("\n===== TOUR DETAILS =====")
print("Destination:", destination)
print("Package:", package)
print("Duration:", days, "Days")
print("Hotel:", hotel)
print("Estimated Cost:", budget)