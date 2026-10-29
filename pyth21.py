words=input("enter words separated by spaces:").split()
longest_word=max(words,key=len)
print("longest word:", longest_word)
print("length  of the longest word:",len(longest_word))
