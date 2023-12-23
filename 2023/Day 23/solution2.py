from typing import List, Tuple, Set

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, px, py, sx, sy, d):
    if (x, y) in cand and (x, y) != (sx, sy):
        adj[sx][sy].append((x, y, d))
        return
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M and g[nx][ny] != '#' and (nx, ny) != (px, py):
            dfs(nx, ny, x, y, sx, sy, d + 1)

def longest(x, y):
    global ans, cur
    if (x, y) == (N-1, M-2):
        ans = max(ans, cur)
        return
    vis[x][y] = 1
    for nx, ny, d in adj[x][y]:
        if not vis[nx][ny]:
            cur += d
            longest(nx, ny)
            cur -= d
    vis[x][y] = 0

def main() -> None:
    global N, M, g, cand, adj, vis, ans, cur
    with open("input.txt", "r") as file:
        g = [line.strip() for line in file]

    N = len(g)
    M = len(g[0])

    cand = set()
    for x in range(N):
        for y in range(M):
            if g[x][y] == '#':
                continue
            sig = sum(1 for dir in range(4) if 0 <= x + dx[dir] < N and 0 <= y + dy[dir] < M and g[x + dx[dir]][y + dy[dir]] != '#')
            if (x, y) == (0, 1) or (x, y) == (N-1, M-2):
                sig = 3
            if sig >= 3:
                cand.add((x, y))

    adj = [[[] for _ in range(M)] for _ in range(N)]

    for x, y in cand:
        dfs(x, y, x, y, x, y, 0)

    vis = [[0] * M for _ in range(N)]
    ans = 0
    cur = 0

    longest(0, 1)
    print(ans)

if __name__ == "__main__":
    main()
