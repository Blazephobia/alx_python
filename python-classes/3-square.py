class Square:
    def __init__(self, size=0):
        self.size = size  # Use the property setter
        
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        return self.__size ** 2

# Example usage:
try:
    square1 = Square(5)
    print(square1.size)  # Output: 5
    print(square1.area())  # Output: 25

    square2 = Square()
    square2.size = 3
    print(square2.size)  # Output: 3
    print(square2.area())  # Output: 9

    square3 = Square(-2)  # This will raise a ValueError
except (TypeError, ValueError) as e:
    print(e)
