def convertMiles(number):
    milesInFeet = number*5280
    return milesInFeet

def main():
    number = float(input("How many miles did you walk?: "))
    if number >= 0:
       convertedMiles = convertMiles(number)
       print(f"You walked {convertedMiles} miles")
    else:
        print("Please enter a valid milage")
    
print("Hike Calculator\n\n")
main()
