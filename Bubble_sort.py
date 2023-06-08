def bub(l1):
    for i in range(0,len(l1)-1):  
        for j in range(len(l1)-1):  
            if(l1[j]>l1[j+1]):  
                temp = l1[j]  
                l1[j] = l1[j+1]  
                l1[j+1] = temp  
    return l1  
  
l1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", l1)    
print("The sorted list is: ", bub(l1))  
