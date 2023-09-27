grade = (int(input("How many points out of 50 did you get?"))/50)*100
actgrade = (grade**(1/2))*10
total = ((actgrade+100)/2)*0.5 + 50
print(total)