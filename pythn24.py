dict1 = {}
dict2 = {}

n = int(input("Enter number of elements in first dictionary: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

m = int(input("Enter number of elements in second dictionary: "))
for i in range(m):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

dict1.update(dict2)

print("Merged dictionary:", dict1)
