
if __name__ == '__main__':
    for i in range(int(input())):
        try:
            a, b = list(map(int, input().split(' ')))
            print(a // b)
        except ValueError as e:
            print('Error Code:', e)
        except ZeroDivisionError as e:
            print('Error Code:', e)
