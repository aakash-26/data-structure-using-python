"""
queue using python

"""

class Queue:
    
    def __init__(self):
        self.queue = []
        print("queue created")
        
    def push(self,data):
        self.queue.insert(0,data)
        print("\nElement added inside queue")
        self.print_queue()
    
    def pop(self):
        p = self.queue.pop()
        print("\npoped element is",p)
        self.print_queue()
        return p
        
    def is_empty(self):
        if len(self.queue) == 0:
            print("\nqueue is empty")
        else:
            print("\nqueue is not empty")


    def peak(self):
        print("\nPeak element inside queue is",self.queue[-1])
        return self.queue[-1]
    
    def length(self):
        l= len(self.queue)
        print("\nlength of queue is",l)
        return l
    
    def print_queue(self):
        if self.queue:
            # print("\nqueue elements are")
            for i in self.queue[::-1]:
                print(i)
                # print("↑")

            
        
        
s = Queue()

s.push(1)
s.push(2)
s.push(3)
# s.print_queue()
s.pop()
# s.print_queue()
s.peak()
s.length()
s.is_empty()










