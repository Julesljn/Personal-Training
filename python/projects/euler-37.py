def square_root(n):
    x = n / 2
    prev = 0

    while abs(x - prev) > 1e-6: # On continue jusqu'à ce que la différence soit minime /// 1e-6 = 0.000001
        prev = x
        x = 0.5 * (x + n / x)

    return x

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(square_root(n)) +1):
        if n % i == 0:
            return False
    return True

def response():
    final_numbers = []
    i = 8
    while len(final_numbers) < 11:
        num_str = str(i)
        cut_number = [int(num_str[j:]) for j in range(len(num_str))] + [int(num_str[:j]) for j in range(len(num_str)-1, 0, -1)]
        is_break = False
        for element in cut_number:
            if is_prime(element) == False:
                is_break = True
                break
        if is_break == False:
            final_numbers.append(i)
        i+=1
        
    
    return sum(final_numbers)


print(response())
