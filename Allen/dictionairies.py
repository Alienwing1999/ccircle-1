def numbers_squared_dict(n):
    d = dict()
    for i in range(n):
        d[i] = i**2
    return d

print(numbers_squared_dict(5))
