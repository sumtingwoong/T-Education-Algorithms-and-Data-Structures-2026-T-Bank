def merge_sort(arr):
    if len(arr) <= 1: return arr, 0

    mid = len(arr) // 2
    left, cntL = merge_sort(arr[:mid])
    right, cntR = merge_sort(arr[mid:])

    merged, cntM = merge(left, right)

    return merged, cntL + cntM + cntR


def merge(left, right):
    i = j = 0
    merged = []
    cnt = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            cnt += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return merged, cnt


n = int(input())
elements = list(map(int, input().split()))

sorted_arr, cnt = merge_sort(elements)
print(cnt)
print(*sorted_arr)


