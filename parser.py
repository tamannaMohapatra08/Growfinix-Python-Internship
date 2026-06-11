import re

with open("enquiries.txt", "r") as file:
    data = file.read()

names = re.findall(r"Name:\s*(.*)", data)
emails = re.findall(r"Email:\s*(.*)", data)
destinations = re.findall(r"Destination:\s*(.*)", data)

print("\nTOUR ENQUIRY SUMMARY")
print("=" * 40)

for i in range(len(names)):
    print(f"Customer {i+1}")
    print(f"Name: {names[i]}")
    print(f"Email: {emails[i]}")
    print(f"Destination: {destinations[i]}")
    print("-" * 40)