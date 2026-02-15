n = int(input())
s = [input().rstrip() for _ in range(n)]
max_len = 0
for i in s:
    if max_len < len(i):
        max_len = int(len(i))
for S in s:
    brank = int((max_len - len(S))/2)
    for _ in range(brank):
        print(".", end="")
    print(S, end="")
    for _ in range(brank):
        print(".", end="")
    print("")
