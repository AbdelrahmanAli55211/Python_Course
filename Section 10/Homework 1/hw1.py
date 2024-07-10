class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.area=None
    def get_area(self):
        self.area=self.width*self.height
        return self.area

class circle:
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        return 3.14*self.radius**2
r=rectangle(2,5)
print(r.get_area())
c=circle(5)
print(c.get_area())

