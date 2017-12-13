from collections import deque


if __name__ == '__main__':
    de = deque()
    for i in range(int(input())):
        input_list = input().split(' ')
        com, item = input_list if len(input_list) == 2 else (input_list[0], None)
        if item:
            getattr(de, com)(item)
        else:
            getattr(de, com)()

    for i in de:
        print(i, end=' ')
