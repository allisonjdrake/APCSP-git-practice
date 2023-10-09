#Recursion: using a function inside itself (call a function in itself)
    #binary search uses recursion 
    #EX:
        # def factorial(n):
        #     if n==1: return 1
        #     return n*factorial(n-1)
        # print(factorial(3))
    #EX2
        # def fib(n):
        #     if n==0:
        #         return 0
        #     if n==1:
        #         return 1
        #     return fib(n-1)+fib(n-2)
        # print(fib(6))
#Divide and Conquer
    #splits array into different smaller arrays
        #continues splitting into mini arrays of one value
        #use mini arrays and sort them
#Greedy
    #at each point try the next best point
    #nearest neighbor/traveling salesman
    #go to the next closest point
#Brute Force
    #find every possible solution --> find the optimal solution\
#Backtracking
    #builds candidates for possible solutions and gets rid of them when it's determined they are not viable
    #the N-queens problem