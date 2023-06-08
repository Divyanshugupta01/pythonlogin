'''import numpy as np
l1=[1,2,3]
l2=[4,5,6]
l3=[l1,l2]
d=np.matrix(l3)
l3=[7,8,9]
l4=[1,5,9]
l5=[l3,l4]
e=np.matrix(l5)
f=np.dot(l3,l5)
print(f)
print(type(f))'''




R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))


matrix = []
print("Enter the entries rowwise:")


for i in range(R):		
	a =[]
	for j in range(C):	 
		a.append(int(input()))
	matrix.append(a)


for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()


r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))


matrix2 = []
print("Enter the entries rowwise:")


for i in range(r):		
	a2 =[]
	for j in range(c):	 
		a.append(int(input()))
	matrix2.append(a2)


for i in range(r):
	for j in range(c):
		print(matrix2[i][j], end = " ")
	print()

