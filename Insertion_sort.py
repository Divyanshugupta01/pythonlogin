def insertion(l1):    
        for i in range(1, len(l1)):
            val = l1[i] 
            j = i - 1  
            while j >= 0 and val < l1[j]:  
                l1[j + 1] = l1[j]  
                j -= 1  
            l1[j + 1] = val  
        return l1  
  
l1 = [10, 5, 13, 8, 2]  
print("The unsorted list is:", l1)  
  
print("The sorted list1 is:", insertion(l1)) 
