if __name__ == '__main__':
    for i in range(int(input())):
        le = int(input())
        my_list = list(map(int, input().split(' ')))
        direction = True
        fin = True
        # 如果为Yes，那么这一串数因该是先变小再变大，于是O(n)检查下就ok
        for j in range(1, le):
            if direction and my_list[j-1] >= my_list[j]:
                pass
            elif direction and my_list[j-1] < my_list[j]:
                direction = False
            elif not direction and my_list[j-1] <= my_list[j]:
                pass
            else:
                fin = False
                break
        if fin:
            print('Yes')
        else:
            print('No')
