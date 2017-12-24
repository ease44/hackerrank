def fibonacci(n):
    if n == 0:
        return []
    a, b = 0, 1
    yield a
    for i in range(n-1):
        a, b = b, a+b
        yield a


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x ** 3, fibonacci(n))))
