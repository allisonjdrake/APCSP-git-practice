restaurants = ["Din Tai Fung", "Houston's", "Paulette's Pupusas", "Leah's Thai", "Taco Bell"]
new_restaurants = input("What restaurant would you like to add to the list?")
count = 4
for i in range (5):
  print(f"Do you like A) {new_restaurants} or B) {restaurants[count]} better?")
  if input() == "A":
    count -= 1
    continue;  
  else:
    break;
restaurants.insert(count+1, f'{new_restaurants}')
print(f'Your new list of restuarants is {restaurants}')   
  