
class Node:
    
    def __init__(self,value = None,next = None,prev = None):
        
        self.value = value
        self.next = next
        self.prev = prev    
        
class List:
    
    def __init__(self):
        
        self.head = None
        
    def create_list(self,value):
        
        h = self.head
        
        if h:
            while h.next:
                h = h.next
            
            n = Node(value,None,h)
            h.next = n
            
        else:
            self.head = Node(value,self.head,None)
            
    def print_list(self):
        
        h = self.head
        
        while h.next:
            print(h.value,end = "->")
            h = h.next
            
l = List()

l.create_list(1)
l.create_list(2)
l.create_list(3)
l.create_list(4)
l.create_list(5)
l.create_list(6)
l.create_list(7)
l.print_list()


            
        
        
