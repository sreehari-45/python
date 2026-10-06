n=int(input("enter number of names:"))
names=[]
for i in range(n):
  name=input("enter name:")
  names.append(name)
  count=0
for name in names:
 count+=name.lower().count('a')
 print("number of occurences of 'a':",count)
