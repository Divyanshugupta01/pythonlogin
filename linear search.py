def binary(l1,n):
    low=0
    high=len(l1)-1
    mod=0
    while low<=high:
        mid=(high+low)//2
        if l1[mid]<n:
            low=mid+1
        elif l1[mid]>n:
            high=mid-1
        else:
            return mid
    return -1
    for i in range(0,n):
        if()
'''n=i(input("Enter the no. of elements in list:\t"))'''
l1=list(input("Enter the elements"))
print(l1)
    


