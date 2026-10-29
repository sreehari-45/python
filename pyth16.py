color_lists1 = input("enter colors in list 1:").split(",")
color_lists2 = input("enter colors in list 2:").split(",")
print("colors in list 1 not in list 2:")
for color in color_lists1:
 if color not in color_lists2:
     print(color)
