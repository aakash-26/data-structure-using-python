"""
Create linked list

"""

class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        n = Node(data, self.head)
        self.head = n
        
    def insert_at_end(self,data):
        
        if self.head == None:
            n=Node(data,self.head)
            self.head=n
        else:

            itr = self.head
            while itr.next:
                itr = itr.next
            
            n =Node(data,None)
            itr.next = n
            
    def insert_element(self,data,position):
        length = self.list_length()
        if self.head == None:
            insert_at_start(data)
            
        elif length == 1:
            insert_at_end(data)
        
        else:
            itr = self.head
            c =1
            while itr.next:
                if c==position-1:

                    node = Node(data,itr.next)
                    itr.next = node
                    break
                c += 1
                itr=itr.next
    
    
    def list_length(self):
        c = 0

        if self.head and self.head is not None:
            c=1
            itr = self.head
            while itr.next:
                c+=1
                itr=itr.next
        print("--------length------------",c)
        return c
                
            
            
    def remove_element(self,position):
        
        if self.head is not None:
            
            length = self.list_length()
            print("position to delete ",position)
            if position == 1:
                
                self.head = self.head.next
            else:

                c = 1
                itr = self.head
                while itr.next:
                    
                    if c == position - 1:
                        print("-------here--------")
                        if itr.next.next:
                            itr.next = itr.next.next
                        else:
                            itr.next = None
                        break
                    itr = itr.next

        
                    
                
        
        


    def print_linked_list(self):
        if self.head is not None:

            i = self.head
            while i:
                print("-> {} ".format(i.value),end="")
                i = i.next
            print()
        else:
            print("-------------empty----------")

l = LinkedList()
l.insert_at_start(5)
l.insert_at_start(15)
l.insert_at_start(25)
l.insert_at_start(35)

l.insert_at_start(45)
l.insert_at_start(55)

l.print_linked_list()
l.remove_element(1)
l.print_linked_list()

l.remove_element(2)

l.print_linked_list()
l.insert_element(65,3)
l.print_linked_list()




