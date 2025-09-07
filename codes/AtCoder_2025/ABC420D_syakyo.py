# 解説を写経

from collections import deque

h, w = map(int, input().split())
a = [input() for _ in range(h)]
sx, sy, gx, gy = -1, -1, -1, -1
for i in range(h):
    for j in range(h):
        if a[i][j] == "S":
            sx, sy = i, j
        if a[i][j] == "G":
            gx, gy = i, j

INF = 10**9
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
d = [[[INF] * w for _ in range(h)] for _ in range(2)]
q = deque()
q.append((0, sx, sy))
d[0][sx][xy] = 0
while q:
    c, x, y = q.popleft()
    for k in range(4):
        xx, yy = x + dx[k], y + dy[k]
        if (
            not (0 <= xx < h and 0 <= yy < w)
            or a[xx][yy] == "#"
            or (c == 0 and a[xx][yy] == "x")
            or (c == 1 and a[xx][yy] == "o")
        ):
            continue
        cc = c ^ (a[xx][yy] == "?")
        if d[cc][xx][yy] != INF:
            continue
        q.append((cc, xx, yy))
        d[cc][xx][yy] = d[c][x][y] + 1
ans = min(d[0][gx][gy], d[1][gx][gy])
print(-1 if ans == INF else ans)