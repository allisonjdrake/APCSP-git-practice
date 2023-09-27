#Binary Search: time = O(logn) basically meaning that as you add more values, the time increases 
    #logarithmically (slower than linear)
    #list must be sorted
    #goes through the list cutting it in half asking "is value greater than this point or less than"
    #only has to evaluate half of the set of data

#Linear Search: time = O(n) basically meaning that as you add values, time increases linearly
    #goes through each value asking "is this the one"

#binary search: first index to pull from a list is len(list)/2 - 1
    # can create a new list where the indexes are either less than the OG or more than

#password generator = exponential algorithm (time exponentially increase as the number of digits increases)
#superpolynomial = impossible (runs faster than n^k)
    #unreasonable runs in super polynomial time (exponential, factorial time, and anything faster
    # reasonable does not run in super polynomial time (log, linear, quadratic)

#heuristic: a rule that helps guide th algorithm to find good choices (good enough)

#heuristic in real life: 
    #decision: not going on the freeway at times between 5 and 7 pm
    #heuristic: traffic is bad during those times since people are coming home from work

#heuristic narrows down the possibilities 
# (i.e. traveling salesman problem: you're not going to go to the exact opposite side of the country,
# better go to the closer cities)