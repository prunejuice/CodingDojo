class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def test(self):
        print "Walk"


bmx = Bike(2000, 200, 9482)

print bmx.miles
