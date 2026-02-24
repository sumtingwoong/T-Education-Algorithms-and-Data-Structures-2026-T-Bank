nk = list(map(int, input().split()))
elements = list(map(int, input().split()))
questions = list(map(int, input().split()))

for i in questions:
    left = 0
    right = nk[0] - 1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if elements[mid] < i:
            left = mid + 1
        elif elements[mid] > i:
            right = mid - 1
        else:
            flag = True
            break
    print('YES') if flag else print('NO')
