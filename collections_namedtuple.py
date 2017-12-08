from collections import namedtuple


# 法一
# if __name__ == '__main__':
#     total = int(input())
#     avg = -1
#     ind = 0
#     for i in range(total+1):
#         columns = list(filter(lambda x: len(x) != 0, input().split(' ')))
#         if avg == -1:
#             ind = columns.index('MARKS')
#             avg = 0
#         else:
#             avg += int(columns[ind]) / total
#     print(avg)


if __name__ == '__main__':
    total = int(input())
    Students = namedtuple('Students', input())
    avg = 0
    # 传参用列表解析
    for i in range(total):
        avg += int(Students(
            *list(filter(lambda x: len(x) != 0, input().split(' ')))
        ).MARKS) / total
    print(avg)
