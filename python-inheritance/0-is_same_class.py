def is_same_class(obj, a_class):
    return type(obj) is a_class

# Example usage:
number = 5
string = "Hello"
list_obj = [1, 2, 3]

print(is_same_class(number, int))  # Output: True
print(is_same_class(string, str))  # Output: True
print(is_same_class(list_obj, list))  # Output: True
print(is_same_class(number, str))  # Output: False
