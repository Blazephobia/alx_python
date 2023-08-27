def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])

# Example usage:
sentence = "Hello, world!"
result = multiple_returns(sentence)
print(result)  # Output will be: (13, 'H')

empty_sentence = ""
empty_result = multiple_returns(empty_sentence)
print(empty_result)  # Output will be: (0, None)
