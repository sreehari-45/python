n = int(input("Enter the number of elements: "))

d = {}

for i in range(n):
    key = int(input("Enter key: "))
    value = input("Enter value: ")
    d[key] = value

desc = dict(sorted(d.items(), reverse=True))
print("Descending order:", desc)

asc = dict(sorted(d.items()))
print("Ascending order:", asc)

