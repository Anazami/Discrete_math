from itertools import product
import sys
print('This programme is for testing if a given list of elements constitutes a set \n')
print('You are required to enter elements of list A separating elements with a space ')
print('And list R where R is of the form (written mathematically) x1,y1 x2,y2 xn,yn')
A = input("Please enter items in the list A ").split(" ")
R = input("Please enter items in the list R   ").split(" ")

for x in range(len(R)):
    R[x] = tuple(R[x].split(","))

if len(R) != len(set(R)):
    print("R is not a set")
else:
    print("R is a set")

cartesian_product = set(product(list(A), list(A)))
if set(R).issubset(cartesian_product):
    print("R is a subset of AxA")
    print("R is a relation on A")
else:
    print("R is not a subset of AxA ")
    print("R is not relation in A")
    exit()
reflex = []
for x in A:
    if (x, x) not in R:
        reflex.append(x)

if len(reflex) == 0:
    print("R is reflexive")
else:
    print("R is not reflexive: " + str(reflex))

trans = []
for a, b in R:
    for c, d in R:
        if b == c and (a, d) not in R:
            trans.append((a, b, c, d))
if len(trans) == 0:
    print("R is transitive")
else:
    print("R is not transitive: " + str(trans))
non_symmetric = []
symmetric = []
for x, y in R:
    if (y, x) not in R:
        symmetric.append((x, y))
if len(non_symmetric) == 0:
    print("R is symmetric")
else:
    print("R is not symmetric: " + str(non_symmetric))