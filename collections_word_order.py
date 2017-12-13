from collections import OrderedDict


if __name__ == '__main__':
    od = OrderedDict()
    for i in range(int(input())):
        key = input()
        od[key] = od.get(key, 0) + 1

    print(len(od))
    for i in od.values():
        print(i, end=' ')
