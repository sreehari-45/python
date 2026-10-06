n= int(input("enter number of elements:"))
lst= []
for i in range(n):
    x=int(input("enter a value:"))
    if x> 100:
      lst.append("over")
else:
     lst.append(x)
print("list:",lst)
