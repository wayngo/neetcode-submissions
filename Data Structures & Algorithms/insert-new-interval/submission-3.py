class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #keep intervals sorted 
        #sorted in ascending order 
        #list of intervals with start and end times
        # we insert a new interval inside our list and merge overlapping intervals 

        #Lets use a Greedy Approach (step by step)

        #iterate through each interval in our given array list 
        #were gonna check if our new interval ends before our current intervals start time
            #if so we add our new interval to res and return it since everything is already sorted and non overlapping 
        #if our new interval starts after the current one ends 
            #we append our current interval to res 
        #if these conditions aren't met that means they overlap 
            # so we merge by updating our new interval
            #change its starting value to the minimum of either our current or new interval 
            #change its ending value to the max of either our current or new interval 
        # if our loop ends that means our interval is last in the list 
        #return res 

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]) , max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res