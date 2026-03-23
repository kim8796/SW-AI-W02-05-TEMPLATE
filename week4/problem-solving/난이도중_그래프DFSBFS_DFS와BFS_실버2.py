# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
import sys
from collections import deque


def main():
    input = sys.stdin.readline

    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for node in range(1, n + 1):
        graph[node].sort()
        
    visited_dfs = [False]*(n+1)
    dfs_result = []
    def dfs(now):
        visited_dfs[now] = True
        dfs_result.append(now)
        for nxt in graph[now]:
            if not visited_dfs[nxt]:
                dfs(nxt)

    dfs(v)



    bfs_result = []
    visited_bfs = [False] * (n+1)

    q= deque([v])
    visited_bfs[v] = True

    while q:
        now = q.popleft()
        bfs_result.append(now)
        for nxt in graph[now]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                q.append(nxt)


    print(*dfs_result)
    print(*bfs_result)

if __name__ == "__main__":
    main()
