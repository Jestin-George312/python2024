print("Name: Jestin George ")
print(" Admission_number: A24MCA035")
print(" experiment number:10 \n")

from graphics.rectangle import RectPerimeter
from graphics.circle import CircleArea
from graphics.threeDGraphics.cuboid import *
from graphics.threeDGraphics.sphere import *

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle :"))

print("perimeter of rectangle:",RectPerimeter(l,b))

r=int(input("Enter the radius  of circle:"))
print("Circle Area:",CircleArea(r))

l=int(input("Enter the length of cuboid:"))
w=int(input("Enter the width of cuboid:"))
h=int(input("Enter the height of cuboid:"))
print("The cuboid area is :",CuboidArea(l,w,h))

print("The cuboid perimeter is :",CuboidPerimeter(l,w,h))

r=int(input("Enter the radius for sphere :"))
print("Sphere Area:",SphereArea(r))
print("Sphere Perimeter:",SpherePerimeter(r))