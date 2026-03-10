import sys
import math

def vertical_sum(k, n, m):
    return n * k * (m * (n - 1) + k + 1) // 2

def horizontal_sum(k, n, m):
    x = k * m
    return x * (x + 1) // 2

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
pos = 1
out = []

INF = 10**30

for _ in range(t):
    n = data[pos]
    m = data[pos + 1]
    pos += 2

    nm = n * m
    total = nm * (nm + 1) // 2

    best_v_diff = INF
    best_v_x = INF

    if m > 1:
        B = m * (n - 1) + 1
        D = B * B + 4 * (total // n)
        k0 = int((-B + math.isqrt(D)) // 2)

        for k in (k0 - 1, k0, k0 + 1, k0 + 2):
            if 1 <= k <= m - 1:
                s = vertical_sum(k, n, m)
                diff = abs(total - 2 * s)
                x = k + 1
                if diff < best_v_diff or (diff == best_v_diff and x < best_v_x):
                    best_v_diff = diff
                    best_v_x = x

    best_h_diff = INF
    best_h_x = INF

    if n > 1:
        y0 = (math.isqrt(1 + 4 * total) - 1) // 2
        k0 = y0 // m

        for k in (k0 - 1, k0, k0 + 1, k0 + 2):
            if 1 <= k <= n - 1:
                s = horizontal_sum(k, n, m)
                diff = abs(total - 2 * s)
                x = k + 1
                if diff < best_h_diff or (diff == best_h_diff and x < best_h_x):
                    best_h_diff = diff
                    best_h_x = x

    if best_v_diff <= best_h_diff:
        out.append(f"V {best_v_x}")
    else:
        out.append(f"H {best_h_x}")

sys.stdout.write("\n".join(out))