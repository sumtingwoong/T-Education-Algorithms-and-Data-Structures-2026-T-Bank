import sys

input = sys.stdin.buffer.readline
n = int(input())
stack = []
ans = []

for _ in range(n):
    act = input().split()
    if act[0] == b'1':
        cur = int(act[1])
        if not stack:
            stack.append((cur, cur))
        else:
            cur_min = stack[-1][1]
            if cur < cur_min:
                stack.append((cur, cur))
            else:
                stack.append((cur, cur_min))
    elif act[0] == b'2':
        stack.pop()
    else:
        ans.append(str(stack[-1][1]))

sys.stdout.write('\n'.join(ans))