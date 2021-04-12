"""
Selection sort 

time complexity = O(n)

"""

# Maethod 1:
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

        
# Method 2:

def selection_sort(arr):
    
    for i in range(len(arr) - 1):
        
        min_index = i
        
        for j in range(i + 1,len(arr)):
            
            if arr[j] < arr[min_index]:
                
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
 
            
                
           
            
a = [1,43,56,7,9,6,9,51,34]
selection_sort(a)
print(a)
