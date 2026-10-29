colors = input("enter color names separated by commas: ").split(",")
colors = [color.strip() for color in colors]
print("first color:", colors[0])
print("first color:", colors[-1])
