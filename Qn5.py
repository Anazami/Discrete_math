x = []
y = []
n = int(input("Enter number of elements for the first set : "))

for i in range(0, n):
    ele = input("enter the elements of X set ")
    x.append(ele)
m = int(input("Enter number of elements for the second set : "))
for i in range(0, m):
    ele = input("enter the elements of X set ")
    y.append(ele)
X = list(x)
Y = list(y)
print(X)
print(Y)
x.sort()
y.sort()
for q in range (0,n):
    for e in range (0,m):
        if int(x[q]) % int(y[e]) == 0:
            print(True)
            break
        else:
            print(False)
    break
