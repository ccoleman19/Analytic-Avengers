def converter(option, number):
        if option=="a":
                convertedNumber=round(number*0.3048,2)
        elif option=="b":
               convertedNumber=round(number/0.3048,2)
        return convertedNumber

def redo():
        option = input("Would you like to perform another conversion? (y/n): ").lower()
        if option == "y":
                main()
        else:
                print("\nThanks, bye!")

def main():
        print("Feet and Meters Converter\n\n")
        print("Conversion Menu:")
        print("a. Feet to Meters")
        print("b. Meters to Feet")
        select = input("Select a conversion (a/b):").lower()
        if select == 'a':
                feet = float(input("Enter feet: "))
                number = converter(select,feet)
                print(number)
                redo()
        elif select == 'b':
                meters = float(input("Enter meters: "))
                number = converter(select,meters)
                print(number)
                redo()
        else:
                print("\n\nPlease enter a valid option!\n\n")
                main()

if __name__ == '__main__':
    main() 