#!/usr/bin/python3
def fibonacci_sequence(n):
    if n<= 0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    
    sequence =[0, 1]
    for i in range(2, n):
        next_fib = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_fib)
        
    return sequence


    
    