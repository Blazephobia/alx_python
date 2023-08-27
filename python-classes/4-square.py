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
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

# Example usage:
try:
    square1 = Square(5)
    square1.my_print()  # Output: #####
                        #         #####
                        #         #####
                        #         #####
                        #         #####
    
    square2 = Square(3)
    square2.my_print()  # Output: ###
                        #         ###
                        #         ###
    
    square3 = Square(0)
    square3.my_print()  # Output: (empty line)
    
    square4 = Square(-2)  # This will raise a ValueError
except (TypeError, ValueError) as e:
    print(e)
