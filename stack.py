# LIFO 

class stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values= [x]+self.values
    def pop(self):
        return self.values.pop(0)
    

s=stack()
s.push(45)
s.push(42)
s.push(65)
s.push(48)
print(s.values)
s.pop()
print(s.values)