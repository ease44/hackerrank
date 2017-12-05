from collections import Counter


if __name__ == '__main__':
    x = int(input())
    size_list = list(map(int, input().split(' ')))
    n = int(input())
    count_static = Counter(size_list)
    total = 0
    for i in range(n):
        size, price = list(map(int, input().split(' ')))
        legacy = count_static.get(size, 0)
        if legacy > 0:
            count_static[size] = legacy - 1
            total += price
    print(total)
