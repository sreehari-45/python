s=input("enter a sentence = ")
words = s.split()
count = {}
for word in words:
  if word in count:
      count[word] += 1
  else:  
      count[word]=1
print(count)  
