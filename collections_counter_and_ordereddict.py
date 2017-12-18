from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == '__main__':
    for k, v in OrderedCounter(input()).most_common(3):
        print(k, v)
