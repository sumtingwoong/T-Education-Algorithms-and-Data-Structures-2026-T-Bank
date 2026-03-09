n = int(input())
p = list(map(int, input().split()))

used = [0] * (n + 1)
a = [0] * (n + 1)

a[0] = 1
r = n

i = 0
while i < n:
    used[p[i]] = 1

    while r > 0 and used[r] == 1:
        r -= 1

    if r == 0:
        a[i + 1] = 1
    else:
        a[i + 1] = i + r - n + 2

    i += 1

print(*a)