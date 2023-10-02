import random

numList = [0,1,2,3,4,5,6,7,8,9,10]

#generate a random number between 0 and 1, not including 1
rand_0to1 = random.random()

#random integer from 10-100, including 100
rand_int = random.randint(10,100)

#random element from a given collection
rand_choice = random.choice(numList)

#random sample of size k from given collection
rand_sample = random.sample(numList, k=3)

#shuffle collection all around
rand_shuffle = random.shuffle(numList)