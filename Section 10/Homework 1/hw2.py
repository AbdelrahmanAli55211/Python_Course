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
        self.area=None
    def get_area(self):
        self.area=3.14*self.radius**2
        return 3.14*self.radius**2
class editor:
    def __init__(self):
        self.rec=None
        self.cir=None
    def create_rectangle(self,width,height):
        self.rec=rectangle(width,height)
        self.rec.get_area()
    def create_circle(self,radius):
        self.cir=circle(radius)
        self.cir.get_area()
    def change(self,factor):
        if self.rec !=None:
            self.rec.width=self.rec.width+factor
            self.rec.height = self.rec.height+factor
        if self.cir !=None:
            self.cir.radius=self.cir.radius+factor
    def printing(self):
        print(self.rec.get_area(),self.cir.get_area())
obj=editor()
obj.create_circle(5)
obj.create_rectangle(3,5)
obj.printing()
obj.change(2)
obj.printing()


