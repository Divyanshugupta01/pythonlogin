def select(a):  
    l=len(a)  
      
    for i in range(l-1):  
        minInd= i  
          
        for j in range(i+1, l):  
            if a[j]<a[minInd]:  
                minInd = j  
                  
        a[i], a[minInd] = a[minInd], a[i]  
          
          
    return a     
a = [21,6,9,33,3]  
  
print("The sorted array is: ", select(a))  
