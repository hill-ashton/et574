#lab10_1
#Ashton Hill
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height 

    def display(self):
        print(f"Width: {self.width}\nHeight: {self.height}")

r1 = Rectangle(4,5)
r2 = Rectangle(10,10)

r1.display()
r2.display()

print(f"Width of r1: {r1.width}")
print(f"Height of r2: {r2.height}")