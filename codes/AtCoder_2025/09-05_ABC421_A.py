# A - Misdeliveryの解説コードを写経
N = int(input())
S = [input() for _ in range(N)]
X, Y = input().split()
X = int(X)

print("Yes" if S[x-1] == Y else "No")