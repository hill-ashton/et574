#lab10_2
#Ashton Hill
from rectangle import Rectangle

r1 = Rectangle(4,5)
r2 = Rectangle()

r1.display()
print(f"Area: {r1.area()}")

r2.display()
print(f"Area: {r2.area()}")

r2.setWidth(6)
r2.setHeight(6)

print(f"Get Width: {r2.getWidth()}")
print(f"Get Height: {r2.getHeight()}")
print(f"Area: {r2.area()}")