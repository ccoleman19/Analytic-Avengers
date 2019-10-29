from random import randrange

def rollDice():
    firstRoll = randrange(1,7)
    secondRoll = randrange(1,7)
    return firstRoll, secondRoll

def redo():
    redo = input("Roll again? (y/n): ").lower()
    if redo == 'y':
        main()
    else:
        print("\n\nGood Bye!") 

def main():
    print("Dice Roller\n\n")
    option = input("Roll the dice? (y/n):").lower()
    if option == "y":
        firstRoll, secondRoll = rollDice()
        print(f"Die 1: {firstRoll}")
        print(f"Die 2: {secondRoll}")
        redo()

if __name__ == '__main__':
    main() 
    
