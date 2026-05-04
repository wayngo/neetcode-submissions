class Solution:
    def climbStairs(self, n: int) -> int:
        #were given an amount to complete climb a set of stairs 
        #stairs can only be climbed with one or two steps 
        #our goal is find all the combinations of way to climb towards the top of the staircase

        #recursion method
            #we can recursively call i + 1 and i + 2 to till we explore all paths
            #until we reach the top

        

        #bottom method
        #work from the top and add up the solutions of prior solutions as we move down.
        #if n = 5 , 5 = 1 | 4 = 1 | 3 = (5) + (4) = 2

        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two 
            two = temp

        return one


