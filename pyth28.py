start = int(input("enter starting number:"))
end= int(input("enter ending numbers:"))
for n in range(start, end + 1):
    if 1000 <= n <= 9999:
       if all(int(d) % 2 ==0 for d in str(n)):
            root=int(n**0.5)
            if root*root==n:
                 print(n)
