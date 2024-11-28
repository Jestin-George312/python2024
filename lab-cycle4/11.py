print("Name: Jestin George\n ")
print("\n Admission_number: A24MCA035")
print("\n experiment number:11")


class Rectangle:
    def __init__(self,length,breadth):

         self.length=length
         self.breadth=breadth

    def area(self):
        return self.length * self.breadth

        # Return the area of the rectangle (length * breadth)


    def show_area(self):
        print(f"The area is : {self.length * self.breadth}")



    def perimeter(self):
        return 2 * (self.length + self.breadth)

        # Return the perimeter of the rectangle (2 * (length + breadth))


    def show_perimeter(self):
        print(f"The perimeter is : {2 * (self.length + self.breadth)}")




print("\n---RECTANGLE 1----")
length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))
r1=Rectangle(length,breadth)
r1.show_area()
r1.show_perimeter()

print("\n---RECTANGLE 2----")
length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))
r2=Rectangle(length,breadth)
r2.show_area()
r2.show_perimeter()

print("\n---comparison----")

if r1.area()>= r2.area():
    print("rectangle 1 area is greater")
else :
    print("area of rectangle 2 is greater")

if r1.perimeter()>= r2.perimeter():
    print("rectangle 1 perimeter is greater")
else :
    print("perimeter of rectangle 2 is greater")