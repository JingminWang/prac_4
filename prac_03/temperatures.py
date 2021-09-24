"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            Celsius_to_Fahrenheit(celsius)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            Fahrenheit_to_Celsius(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
def Celsius_to_Fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))
def Fahrenheit_to_Celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 1.8
    print("Result: {:.2f} C".format(celsius))
main()