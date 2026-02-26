# x^2 + √(x + 1) = C, x - ?

def f(x):
    res = x**2 + (x + 1)**0.5
    return res


def find_max():
    r = 1
    while f(r) < c:
        r *= 2
    return r


c = float(input())
cur_min = 0.0
cur_max = find_max()

for i in range(100):
    cur = (cur_max + cur_min) / 2
    val = f(cur)
    if val > c:
        cur_max = cur
    else:
        cur_min = cur

print(f'{cur_min:.6f}')