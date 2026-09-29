a=input("enter a number:")
try:
int (a);
print("integer")
except:
try:
float(a)
print ("float")
except:
try:
complex(a)
print("complex")
except:
print("invalid")
