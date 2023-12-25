class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.length = height

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (2 * self.length) + (2 * self.width)

    def get_diagonal(self):
        return (self.length ** 2 + self.width ** 2) ** 0.5

    def get_picture(self):
        if self.length > 50 or self.width > 50:
            return "Too big for picture."
        picture = ''
        for i in range(self.length):
            for j in range(self.width):
                picture += "*"
            picture += '\n'
        return picture

    def get_amount_inside(self, shape):
        return (self.length // shape.length) * (self.width // shape.width)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.length})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.length = side
        self.width = side

    def set_height(self, height):
        self.set_side(height)

    def set_width(self, width):
        self.set_side(width)

    def __str__(self):
        return f"Square(side={self.length})"