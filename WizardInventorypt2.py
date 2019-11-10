import random
fileName = r'wizard_all_items.txt'

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
    with open('wizardInventory.txt','w',newline="") as file:
        for item in inventory:
                file.write(item + "\n")

# The walk function will select one random item from the given wizard_all_items.txt file
def walk(inventory):
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

# The main 
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