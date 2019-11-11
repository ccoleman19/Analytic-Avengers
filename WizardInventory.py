def printCommandMenu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
​
#print the list of all items in the inventory list
def show(inventory: list):
    index = 1
    for item in inventory:
        print(f"{index} {item}")
        index +=1
​
#adds an item to the inventory list
def grab(inventory: list):
    maxLimit = 4
    if len(inventory) < maxLimit:
        item = input("Name: ")
        inventory.append(item)
    else:
        print("You can't carry any more items. Drop something first.")
​
#change any item in the inventory list
def edit(inventory: list):
    index = int(input("Number: ")) #get the list index from user
    if index <= len(inventory):
        index = index - 1 #adjust index
        changedItem = input("Updated name: ")
        inventory[index] = changedItem
        print(f"Item number {index+1} was updated.")
    else:
        print("Inventory index is not correct")
​
#remove an item from the inventory list
def drop(inventory: list):
    index = int(input("number: "))
    if index <= len(inventory):
        index = index - 1
        inventory.remove(inventory[index])
        
# note: funtion names can be used as value in phthon dictionary strucure - aha! How cool!
# Dictionary can be used as substitue for switch/case - to avoid many else, elif statements
def executeCommand(argument, inventoryList: list):
    commandSwitch = {
        "show":show, #see definition of fuction above
        "grab":grab,
        "edit":edit,
        "drop":drop
    }
    #determin the command to use from the dictionary
    function = commandSwitch.get(argument)
    #execute the corresponting fuction and pass the inventory list
    if function != None: #exclue bad commands from user that are not in our dictionary
        function(inventoryList) 
​
def main():
    #create the initial inventory list with 3 items
    wizardInventory = ["wooden staff", "wizard hat", "potion bottle"]
    #print the main menu of the application
    printCommandMenu()  
    while True:
        command = input("Command: ")
        if command.lower() == "exit":
            break
        else:
            executeCommand(command.lower(), wizardInventory)
​
if __name__ == "__main__":
    main()