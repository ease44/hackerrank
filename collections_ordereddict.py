from collections import OrderedDict


if __name__ == '__main__':
    od = OrderedDict()
    count = int(input())
    for i in range(count):
        item, space, price = input().rpartition(' ')
        od[item] = od.get(item, 0) + int(price)

    for k, v in od.items():
        print(k, v)
