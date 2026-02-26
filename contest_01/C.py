from sys import stdout

n = int(input())

cur_min = 1
cur_max = n

for i in range(25):
    cur = (cur_max + cur_min + 1) // 2
    print(cur)
    stdout.flush()
    check = input()
    if check == "<":
        cur_max = cur - 1
    else:
        cur_min = cur

    if cur_min == cur_max:
        print(f'! {cur_min}')
        stdout.flush()
        break
