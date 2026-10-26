"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            change = False
            for j in range(len(intervals)):
                if intervals[i].start > intervals[j].start:
                    tmp = intervals[j]
                    intervals[j] = intervals[i]
                    intervals[i] = tmp
                    change = True
            if not change:
                break
                
        
        start = 0
        for slot in intervals:
            if slot.start < start:
                return False
            else:
                start = slot.end
        return True