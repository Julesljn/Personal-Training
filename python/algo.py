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
    target = 1000000000
    for x in range(1, target+1):
        if x == target:
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


# Integer to binary
@timer
def fourth(x):
    array = []
    while x > 0:
        array.append(x % 2)
        x = x // 2
    array.reverse()
    print(''.join(str(bit) for bit in array))
    

# Pascal's triangle
@timer
def fifth(n):
    print([1])
    last_line = [1, 1]
    actual_line = []
    print(last_line)

    for l in range(2, n):
        actual_line = []
        for i in range(1, len(last_line)):
            actual_line.append(last_line[i] + last_line[i-1])

        actual_line = [1] + actual_line + [1]
        last_line = actual_line        
        print(actual_line)


# Pascal's triangle optimized
@timer
def pascal(n):
    line = [1]
    max_width = n * 4

    print(' '.join(map(str, line)).center(max_width))

    for _ in range(1, n):
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]
        print(' '.join(map(str, line)).center(max_width))








# first()
# second()
# third(20)
# fourth(13)
fifth(40)
# pascal(20)