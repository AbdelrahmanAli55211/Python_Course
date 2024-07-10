class Myrange:
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step
        self.idx=0

    def has_next(self):
        if self.step>0:
            if self.start < self.end:
                return True
            else:
                return False
        else:
            if self.start > self.end:
                return True
            else:
                return False

    def get_next(self):
        back=self.start
        idx=self.idx
        self.idx+=1
        if self.step>0:
            self.start+=1
        else:
            self.start-=1
        return idx,back
rng=Myrange(10,5,-1)
while rng.has_next():
    print(rng.get_next(),end=' ')
    print()
