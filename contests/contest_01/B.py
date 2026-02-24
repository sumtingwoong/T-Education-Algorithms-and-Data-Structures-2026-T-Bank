n, k = map(int, input().split())
elements = list(map(int, input().split()))
request = list(map(int, input().split()))

for x in request:
    left = 0
    right = n - 1
    flag = False
    if x <= elements[0] or n == 1: print(elements[0])
    elif x >= elements[-1]: print(elements[-1])
    else:
        while left != right - 1:
            mid = (left + right) // 2
            if elements[mid] < x:
                left = mid
            elif elements[mid] > x:
                right = mid
            else:
                print(elements[mid])
                flag = True
                break

        if flag: continue

        a = abs(elements[left] - x)
        b = abs(elements[right] - x)
        if a < b: print(elements[left])
        elif a > b: print(elements[right])
        else: print(elements[left])
