fruits = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input("enter the  the fruit")
    fruits.append(ele)

if len(fruits) == len(set(fruits)):
    print(fruits)
    print(True)
else:
    print(fruits)
    print("False, The set should be: ")
    sets = list(set(fruits))
    print(sets)