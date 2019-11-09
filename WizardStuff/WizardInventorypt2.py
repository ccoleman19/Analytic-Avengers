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
    except:
        print("Could not find the items file.\nExiting program.  Bye!")

# print(openFile('wizard_all_items.txt'))
inventory = openFile(fileName)

def walk():
    randomItem = random.choice(inventory)
    print(f"While walking down a path, you see {randomItem}")
    return randomItem

# def grab():
    

def show(inventory: list):
    index = 1
    for item in inventory:
        print(f"{index} {item}")
        index +=1

# show(inventory)
# print(inventory)
# def execCommand(select, inventoryList: list):
#     selection = {
#         "walk":walk,
#         "show":show,
#         "edit":edit,
#         "drop":drop
#     }

#     function = selection.get(select)

#     if function != None:
#         function(inventoryList)


def main():
    menu()
    walk()

# ​if __name__ == "__main__":
main()