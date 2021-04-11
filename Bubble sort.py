"""
Bubble sort 

time complexity = O(n)

"""

def bubble_sort(x):
    
    l = len(x)
    
    for i in range(l-1):
        t = None
        for j in range(l-i-1):
            
            if x[j] > x[j+1]:
                
                t = x[j+1]
                
                x[j+1] = x[j]
                x[j] = t
                
           
            
a = [1,43,56,7,9,6,9,51,34]
bubble_sort(a)
print(a)
