toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
    toDoList.append(item)
    return toDoList

def deleteItem(item):
    try: 
        toDoList.remove(item)
    except:
        print("This item was not found. Please enter a different one.")
    return toDoList

userAns = input("Do you want to add or remove an item from your list or quit? A/R/Q")
while userAns == "A" or "R" or "Q":
    if userAns == "A":
        item = input("What item would you like to add to the list?")
        addItem(item)
        userAns = input("Do you want to add to/remove from your list or quit? A/R/Q")
    elif userAns == "R":
        item = input("What item would you like to remove from the list?")
        deleteItem(item)
        userAns = input("Do you want to add to/remove from your list or quit? A/R/Q")
    else: 
        break;
print(toDoList)