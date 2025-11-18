# 解説の写経
a = [0] * 10
a[0], a[1] = map(int, input().split())

for i in range(2, 10):
    s = str(a[i - 2] + a[i - 1])
    a[i] = int(s[::-1])

print(a[9])