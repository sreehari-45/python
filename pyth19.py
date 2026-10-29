string = input("enter a string:")
frequency = {}
for char in string:
    frequency[char] = frequency.get(char,0)+1
print("character frequency:")
for char,count in frequency.items():
    print (char,":",count)
