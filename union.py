n1=int(input("enter the number of setl"))
l1=[]
for i in range(n1):
    l1.append(input("enter element into set 1"))
n2=int(input("enter a no of element for set2"))
l2=[]
for i in range(n2):
    l2.append(input("enter a no of element for set2"))
l3=[]
for i in l1:
    for j in l2:
        if(i==j):
            l3.append(i)
#for union
l4=[]
for i in l4:
    l4.append(i)
for j in l2:
     if j not in l4:
        l4.append(j)
print("union of list is ")
print(l4)
print("intersection of set is ")
print(l3)
                      
