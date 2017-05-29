class EventList(object):

    """ an object that is an individual event to keep track of the time, place, and the
        reason for the event"""

    def __init__(self, creator, title, time, place):
        self.creator = creator
        self.title = title
        self.time = time
        self.place = place

    def printDetails(self):
        print("creator: {}".format(self.creator))
        print("title: {}".format(self.title))
        print("time: {}".format(self.time))
        print("place: {}".format(self.place))
