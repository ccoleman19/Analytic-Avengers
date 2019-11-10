import random
fileName = r'WizardStuff\wizard_all_items.txt'

def menu():
    print("The Wizard Inventory progran\n\n")
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")

def openFile(fileName):
    try:
        with open(fileName, 'r') as inFile:
            wizardItems = [line.rstrip() for line in inFile]
            return wizardItems
    except FileNotFoundError:
        print("Could not find the items file.\nExiting program.  Bye!")
    except Exception as e:
        print(type(e),e)

items = openFile(fileName)

def editItems(inventory):
    with open('WizardStuff\wizardInventory.txt','w',newline="") as file:
        for item in inventory:
                file.write(item + "\n")

def walk(inventory):
    randomItem = random.choice(items)
    print(f"While walking down a path, you see {randomItem}.")
    grabItem = input('Do you want to grab it? (y/n): ').lower()
    if grabItem == 'y':
        grab(randomItem, inventory)

def grab(randomItem, inventory):
    maxLimit = 4
    if len(inventory) < maxLimit:
        inventory.append(randomItem)
        editItems(inventory)
    else:
        print("You can't carry any more items. Drop something first.")
    return inventory

def drop(inventory):
    try:
        index = int(input("number: "))
        if index <= len(inventory):
            index = index - 1
            inventory.remove(inventory[index])
            editItems(inventory)
        else:
            print('No item in that slot. Pick another!')
    except ValueError:
        print('Invalid item number')

def show(inventory):
    if len(inventory) != 0:
        index = 1
        for item in inventory:
            print(f"{index} {item}")
            index +=1
    else:
        print('You have no items')

def main():
    inventory = []
    menu()
    while True:
        command = input('Command: ')
        if command == 'walk':
            walk(inventory)
        elif command == 'show':
            show(inventory)
        elif command == 'drop':
            drop(inventory)
        elif command == 'exit':
            break
        else:
            print('Not a valid command. Please Try again!')

if __name__ == '__main__':
    main()