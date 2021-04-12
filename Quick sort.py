"""

Quick sort

"""

def partition(arr,start,end):
    
    pi = start
    pivot = arr[pi]
    
    while start < end:
        
        while start <= len(arr) and arr[start] <= pivot:
            start += 1
            
        while arr[end] > pivot:
            end -= 1
            
        if start < end:
            
            arr[start],arr[end] = arr[end],arr[start]
    arr[end],arr[pi] = arr[pi],arr[end]
    
    return end
    

def quick_sort(arr,start,end):
    
    if start < end:
        
        ind = partition(arr,start,end)
        
        quick_sort(arr,start,ind-1)
        quick_sort(arr,ind + 1,end)
        
        
a = [1,43,56,7,9,6,9,51,34]

quick_sort(a,0,len(a)-1)

print("sorted Array : ",a)
    
    
