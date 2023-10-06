import random
Score = {
    "house": 0,
    "player": 0
}

numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

rand_num = random.randint(0,14)

user_num = input("What color are you betting on user?")

if rand_num<=4:
    output = "black"
    print(f"{output, rand_num}")
elif rand_num>=5 and rand_num<=9:
    output = "red"
    print(f"{output, rand_num}")
else:
    output = "green"
    print(f"{output, rand_num}")

if output == user_num:
    print("Yay! You get 3 points!")
    Score["player"] += 3
elif output == "green":
    print("House wins!")
    Score["house"] += 3
else:
    print("i guess we're all losers :(")

print(Score)