def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


result1 = add(4, 5)
result2 = sub(4, 1)

print(result1, result2)

if __name__ == '__main__':
    print("Addition:", add(4, 5))
    print("Subtraction:", sub(4, 5))
    print("Multiplication:", mul(4, 5))