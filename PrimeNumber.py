def isPrimeNumber(number):
    counter = 2 #always including 1 and itself
    for n in range(2,number): 
        myNumber = number%n
        if myNumber == 0:
            counter +=1
    return counter

def isValidNumber():
    success = True
    while success == True:
        userNumber = int(input("Please enter an integer between 1 and 5000: "))
        if userNumber < 2 or userNumber > 5000:
            print("Invalid integer. Please try again.")
        else:
            success = False
    return userNumber

def redo():
    redo = input("Try again? (y/n): ").lower()
    if redo == 'y':
        main()
    else:
        print("\n\nGood Bye!")    
    
def main():
    myNumber = isValidNumber()
    if isPrimeNumber(myNumber) == 2:
        print(f"{myNumber} is a prime number.")
        redo()
    else:
        print(f"{myNumber} is NOT a prime number.\nIt has {isPrimeNumber(myNumber)} factors.")
        redo()

main()