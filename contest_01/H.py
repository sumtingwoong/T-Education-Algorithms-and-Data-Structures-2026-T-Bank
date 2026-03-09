n = int(input())
s = input()

seen = {}

for ch in s:
    if ch not in seen:
        seen[ch] = 1
    else:
        seen[ch] += 1

left = ''
mid = ''

for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if ch in seen:
        left += ch * (seen[ch] // 2)
        if mid == '' and seen[ch] % 2 == 1:
            mid = ch

answer = left + mid + left[::-1]

print(answer)