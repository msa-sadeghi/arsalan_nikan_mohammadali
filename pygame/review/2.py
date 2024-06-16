# name = input("enter a name: ")
# if name == "arsalan":
#     print("hello", name)
# elif name == "nikan":
#     print("hello", name)
# elif name == "mohammadali":
#     print("hello", name)
# else:
#     print("hello", "noOne")
    

# Fahrenheit = Celsius × (9 / 5) + 32
# Celsius = (Fahrenheit - 32) × (5 / 9)
       
def convertToCelsius(Fahrenheit) :
    return (Fahrenheit - 32) * (5 / 9)


def convertToFahrenheit(Celsius):
    return Celsius * (9 / 5) + 32

print(convertToCelsius(0))
print(convertToCelsius(180))
print(convertToFahrenheit(0))
print(convertToFahrenheit(100))
print(convertToCelsius(convertToFahrenheit(15)))

