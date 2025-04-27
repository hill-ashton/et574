#lab10_3
#Ashton Hill
from shapes import Circle,Rectangle

r1 = Rectangle()
r1.display()
r1.setWidth(1.25)
r1.setHeight(1.25)
print(f"Get Width: {r1.getWidth()}")
print(f"Get Height: {r1.getHeight()}")
print(f"Area: {r1.area():.5f}")
print()

c1 = Circle(0)
c1.display()
c1.setRadius(10)
print(f"Get Radius: {c1.getRadius()}")
print(f"Area: {c1.area():.5f}")
print(f"Circumference: {c1.circumference():.5f}")