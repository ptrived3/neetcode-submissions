"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals = [(0,30),(5,10),(15,20)]
        # basically since 5 < 30, then it is conflicting
        # we need to see if intervals[i][1] <= intervals[i+1][0]

        intervals.sort(key=lambda i: i.start)
        
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False

        return True