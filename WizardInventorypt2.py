import random
# adding the file name
fileName = r'wizard_all_items1.txt'

# Prints the menu
def menu():
    print("The Wizard Inventory progran\n\n")
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    
#This function opens the file if it exits.
def openFile(fileName):
    try:
        with open(fileName, 'r') as inFile:
            wizardItems = [line.rstrip() for line in inFile]
            return wizardItems
    except FileNotFoundError:
        print("Could not find the items file.\nExiting program.  Bye!")
        return FileNotFoundError2
    except Exception as e:
        print(type(e),e)

# This function will write and edit the new inventory file.
def editItems(inventory):
    with open('wizardInventory.txt','w',newline="") as file:
        for item in inventory:
                file.write(item + "\n")

# The walk function will select one random item from the given wizard_all_items.txt file
def walk(items, inventory):
    randomItem = random.choice(items)
    print(f"While walking down a path, you see {randomItem}.")
    grabItem = input('Do you want to grab it? (y/n): ').lower()
    if grabItem == 'y':
        grab(randomItem, inventory)

# The grab function will take the random item found from the walk function, add it 
# to the invetory list, and write it to the wizardInventory.txt file
def grab(randomItem, inventory):
    maxLimit = 4
    if len(inventory) < maxLimit:
        inventory.append(randomItem)
        editItems(inventory)
    else:
        print("You can't carry any more items. Drop something first.")
    return inventory

# The drop function will ask for an item number from invedntory list, remove it 
# from the invetory list, and remove it from the wizardInventory.txt file
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

# The show function will show the contents of the invetory list up to a max of 4 items
def show(inventory):
    if len(inventory) != 0:
        index = 1
        for item in inventory:
            print(f"{index} {item}")
            index +=1
    else:
        print('You have no items')

# The main function will ask the user for input commands and keep track of the inventory list
def main():
    inventory = []
    items = openFile(fileName)
    menu()
    while True:
        command = input('Command: ')
        if command == 'walk':
            walk(items, inventory)
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