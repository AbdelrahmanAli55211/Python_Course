class Myrange:
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step

    def has_next(self):
        if self.start<self.end:
            return True
        return False
    def get_next(self):
        back=self.start
        self.start+=1
        return back
rng=Myrange(5,10,1)
while rng.has_next():
    print(rng.get_next(),end=' ')
