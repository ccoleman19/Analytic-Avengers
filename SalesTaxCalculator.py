# from calcTax import calculateTax
def calculateTax(price):
    tax = round(price*.06,2)
    total = round(price + tax,2)
    return tax, price, total
    
def runningTotal():
    lastItem = True
    total = 0
    while lastItem == True:
        price = float(input("Cost of item: "))
        if price > 0:
            total = round(price + total,2)
        elif price == 0:
            lastItem = False
    return total

def redo():
        option = input("\n\nWould you like to perform another conversion? (y/n): ").lower()
        if option == "y":
                main()
        else:
                print("\nThanks, bye!")

def main():
    print("Sales Tax Calculator\n\n")
    print("ENTER ITEMS (ENTER 0 TO END)")
    tax, price, total = calculateTax(runningTotal())
    print(f"Total:                    {price}")
    print(f"Sales Tax:                {tax}")
    print(f"Total After Tax:          {total}")
    redo()

if __name__ == '__main__':
    main() 
    

