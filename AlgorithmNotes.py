#Binary Search: time = O(logn) basically meaning that as you add more values, the time increases 
#logarithmically (slower than linear), time increases less per increased n
    #list must be sorted
    #goes through the list cutting it in half asking "is value greater than this point or less than"
    #only has to evaluate half of the set of data
    #time (number of steps) = log based 2 of number of values

#Linear Search: time = O(n) basically meaning that as you add values, time increases linearly
    #goes through each value asking "is this the one"

#binary search: first index to pull from a list is len(list)/2 - 1
    # can create a new list where the indexes are either less than the OG or more than

#When is MORE time better?
    #password generator = exponential algorithm (time exponentially increase as the number of digits increases)

#REASONABLENESS
    #superpolynomial = impossible (runs faster than n^k)
    #unreasonable runs in super polynomial time (exponential, factorial time, and anything faster
    # reasonable does not run in super polynomial time (log, linear, quadratic)

#HEURISTIC: a rule that helps guide th algorithm to find good choices (good enough)

#heuristic in real life: 
    #decision: not going on the freeway at times between 5 and 7 pm
    #heuristic: traffic is bad during those times since people are coming home from work

#heuristic narrows down the possibilities 
# (i.e. traveling salesman problem: you're not going to go to the exact opposite side of the country,
# better go to the closer cities)



#simulation
    #fake, good to test and help people get accustomed to randomness (removes bias, makes it more accurate, etc.)
        #EX: plane simulator to train pilots to do well in many situations
    #Computers are really bad at being random (they're good at being predictable and do what you tell them to)
        #they need something to create something random
            #EX: using something external: true random number generator (translate atmospheric level --> numbers)
        #or use an algorithm
            #EX: Pseudo random number generator (can be broken more easily, find the seed)