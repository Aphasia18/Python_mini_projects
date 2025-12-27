import math

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,value):
        self.width = value

    def set_height(self,value):
        self.height = value
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return math.sqrt(self.height**2 + self.width**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return ("Too big for picture.")
        result = ''
        result = ("*" * self.width + "\n") * self.height
        return result

    def get_amount_inside(self,fit):
        fits_across = self.width  // fit.width
        fits_down   = self.height // fit.height
        total_fits = fits_across * fits_down
        return total_fits

    def __str__(self):
        return (f"Rectangle(width={self.width}, height={self.height})")


class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        

    def set_side(self,side):
        self.set_width(side)
        self.set_height(side)

    def set_width(self,value):
        super().set_width(value)
        super().set_height(value)
    
    def set_height(self, value):
        super().set_width(value)
        super().set_height(value)


    def __str__(self):
        return (f"Square(side={self.width})")

square  = Square(5)