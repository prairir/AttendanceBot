class EventList(object):

    """ an object that is an individual event to keep track of the time, place, and the
        reason for the event"""

    def __init__(self, creator, time, place, reason):

        self.time = time
        self.place = place
        self.reason = reason
        self.creator = creator

    def printDetails(self):
        
        print(self.creator)
        print(self.place)
        print(self.time)
        print(self.reason)

