class List1:
    def __init__(self, spisok):
        self.a = spisok.copy()
    def sum(self):
        s = 0
        for x in self.a:
            s = s+x
        return s
    def mult(self):
        s = 1
        for x in self.a:
            s = s*x
        return s    
    def sum1(self,b):
        s = 0
        for x in self.a:
            if x>b:
                s = s+x
        return s
    
    
    
    
l1 = List1([2,3,4,5,6,7,8])
print(l1.sum())
print(l1.mult())
print(l1.sum1(4))
