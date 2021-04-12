"""
Selection sort 

time complexity = O(n)

"""

def selection_sort(x):
    z = 0
    for i in range(len(x)):
        print("x",x)
        m = min(x[z:])
        print("m",m)
        ind = x[z:].index(m)
        ind = z + ind
        t = x[z]
        x[z] = m
        x[ind] = t
        
        z += 1

 
            
                
           
            
a = [1,43,56,7,9,6,9,51,34]
selection_sort(a)
print(a)
