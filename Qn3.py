import itertools
A=[]
B=[]
n = int(input("Enter number of elements for the first list : "))
for i in range(0, n):
    ele = input("enter the element of list A: ")
    A.append(ele)
m = int(input("Enter number of elements for the second list : "))
for i in range(0, m):
    ele = input("enter the element of list B: ")
    B.append(ele)

if(all(x in B for x in A)):
   print("truth value of B ⊆ A:",True)
   print("B is a subset A")
else:
    print("truth value of B ⊆ A:",False)
    print("B is not subset of A")
C=[i for i in A if i not in B]
print(C)

cartesian_product = itertools.product(A, B)#Calculate product of `x_list` and `y_list`
cartesian_list = list(cartesian_product)#Convert product to a list
print("list of (A*B):")
print(cartesian_list)