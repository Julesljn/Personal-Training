import time

# time calculator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Function time : {end - start:.4f}')
    return wrapper


# 1 to 1 000 000

@timer
def first():
    for x in range(1, 1000001):
        print(x)

# multiplication table from 1 to 20

@timer
def second():
    for x in range(1, 21):
        for y in range(1, 11):
            print(f'Table of {x} : {y} x {x} = {x*y}')


# Fibonacci sequence (array)

@timer
def third(x):
    array = [0, 1]
    for f in range(0, x-1):
        array.append(array[-1] + array[-2])
    print(array[-1])
    
        
    
        





# first()
# second()
third(2000)