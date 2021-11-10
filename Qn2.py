import itertools
x = []
y = []
n = int(input("Enter number of elements for the first set : "))
for i in range(0, n):
    ele = input("enter element of of A set")
    x.append(ele)
m = int(input("Enter number of elements for the second set : "))
for i in range(0, m):
    ele = input("enter element of of B set")
    y.append(ele)
A = set(x)
B = set(y)
if B.issubset(A):
   print(True)
else:
    print(False)
print(A - B)

cartesian_product = itertools.product(A, B)
#Calculate product of `x_list` and `y_list`

cartesian_list = set(cartesian_product)
#Convert product to a list
print(cartesian_list)