class Rectangle:
    default_color = "green"
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        
    def print_area(self):
        print(self.width*self.height)
        
    def area(self):
        a = self.width*self.height
        return a
        
    @classmethod
    def print_help(cls):
        print("HELP!")


#Rectangle.print_help()
#print(Rectangle.default_color)

r = Rectangle(6, 7)
b = r.area()
print(b)
print(r.area())

#print(r.width)
#r.print_area()
