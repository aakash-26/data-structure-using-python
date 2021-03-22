"""
stack using python

"""

class Stack:
    
    def __init__(self):
        self.stack = []
        print("stack created")
        
    def push(self,data):
        self.stack.append(data)
        print("\nElement added inside stack")
        self.print_stack()
    
    def pop(self):
        p = self.stack.pop()
        print("\npoped element is",p)
        self.print_stack()
        return p
        
    def is_empty(self):
        if len(self.stack) == 0:
            print("\nstack is empty")
        else:
            print("\nstack is not empty")


    def peak(self):
        print("\nPeak element inside stack is",self.stack[-1])
        return self.stack[-1]
    
    def length(self):
        l= len(self.stack)
        print("\nlength of stack is",l)
        return l
    
    def print_stack(self):
        if self.stack:
            # print("\nstack elements are")
            for i in self.stack[::-1]:
                print(i)
                print("↑")

            
        
        
s = Stack()

s.push(1)
s.push(2)
s.push(3)
# s.print_stack()
s.pop()
# s.print_stack()
s.peak()
s.length()
s.is_empty()










