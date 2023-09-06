itemString = []
total_count = {'aluminum': 135, 'plastic': 102, 'paper': 213}

itemString = input("Please enter a list of all your recycleables.")

def sortItems(itemString):
  numA = itemString.count("A")
  numP = itemString.count("P")
  numR = itemString.count("R")
  total_count["aluminum"] += numA
  total_count["plastic"] += numP
  total_count['paper'] += numR
sortItems(itemString)

print(f"The machine now has {total_count['aluminum']} aluminum recyclables, {total_count['plastic']} plastic recyclables, and {total_count['paper']} paper recyclables total.")
print("Thank you for your contributions. Have a nice day! \U0001F600")