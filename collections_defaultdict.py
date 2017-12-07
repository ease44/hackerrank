from collections import defaultdict


if __name__ == '__main__':
    de = defaultdict(list)
    n, m = list(map(int, input().split(' ')))
    for i in range(n):
        k = input()
        de[k].append(i+1)

    res_list = []
    for i in range(m):
        k = input()
        res_list.append(de.get(k, -1))

    for i in res_list:
        if isinstance(i, list):
            for j in i:
                print(j, end=' ')
            print()
        else:
            print(i)
