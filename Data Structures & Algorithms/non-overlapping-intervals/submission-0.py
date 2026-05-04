class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #give multiple intervals
        #to remove an interval so that the list of intervals are non overlapping
        #
        #Sort the interval 
        #result value to represent how many intervals we removed already 
        #set our previous end value to a varaible 
        #we should be iterating through our intervals list for its start and ending value 
        #check if our start value is greater than our end value, set our prev to next 
        #increment our result and set our prev end value to our cur or prev value 
        #return our result 

        intervals.sort()
        res = 0 
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res