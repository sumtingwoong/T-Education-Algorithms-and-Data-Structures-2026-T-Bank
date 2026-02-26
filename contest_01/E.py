# a*(x**3) + b*(x**2) + cx + d = 0

def f(x):
    return ((a*x + b)*x + c)*x + d


a, b, c, d = map(int, input().split())

l = -1e6
r = 1e6

for i in range(100):
    cur = (l + r) / 2
    if f(l) * f(cur) <= 0:
        r = cur
    else:
        l = cur

print(f'{(l + r) / 2:.4f}')

