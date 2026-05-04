class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #given an array of starting and end time intervals.
        #Merge Overlapping intervals together.
        #Should be in the form of a list containing those intervals. 

        #Approach: Sort intervals based on their starting interval time
        #Insert the first interval into our final list
        #Use a for loop that sets the start and end times in intervals
        #Create a variable lastEnd that stores the ending time of the prior interval
        # use [-1][1] -> -1 stands for the previous interval, 1 stands for the 2nd value
        #Check if our starting value of our current interval is greater than the lastEnd
        #if so then we set the ending time for the last interval to our current intervals ending tiem 
        #if not we can just append it to our big list

        intervals.sort(key = lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
