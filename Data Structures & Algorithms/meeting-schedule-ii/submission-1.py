"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Given an array of intervals of meeting times from start and end
        #Find the minimum number of rooms needed to schedule meets without conflicts

        #Split intervals into a list of start times and end times 
        #If a meeting starts before one ends we need a new room 
        #If a meeting ends before or at the same time another starts it opens up.
        
        #Create a start and end sorted list. 
        #Use sorted([i.start for i in intervals])

        #we need to track start times, end times, number of ongoing meetings,
        # and maximum number of rooms needed 

        #using a two pointer approach we can check if start times are less than 
        #our len of the intervals list 
        #Check if our start time index is less than our current end time we increment 
        #starting times and increase ongoing meetings 
        #if not we increment ending time index and decrease the current rooms ongoing 
        #we can track the maximum number of rooms needed by taking the max value of res 
        #for each iteration. 

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = 0
        e = 0
        ongoingRooms = 0 
        maxRooms = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                ongoingRooms += 1
            else:
                e += 1
                ongoingRooms -= 1
            maxRooms = max(maxRooms, ongoingRooms)
        return maxRooms

