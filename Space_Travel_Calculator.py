print("Welcome to the Space Travel Calculator!")
print("Please enter the distance to the celestial object (in light years).")
distance = float(input())

print("Now please enter the speed of the spacecraft (in fraction of the speed of light")
speed = float(input())
time = distance / speed

if time == 1:
  print(f'It will take you {time} year to reach your destination!')
elif time >= 100:
  print(f'It will take you {time} years to reach your destination!')
  print(
      "Unfortunately you probably won't make it...But maybe cryogenics will allow you to get there! Who knows!"
  )
elif time < 1:
  print(
      f'It will take you {time*365} days to reach your destination! Have a good trip!'
  )
else:
  print(f'It will take you {time} years to reach your destination!')
