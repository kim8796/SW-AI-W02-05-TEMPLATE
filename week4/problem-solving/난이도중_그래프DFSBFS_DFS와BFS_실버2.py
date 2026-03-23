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

    # 적용 순서:
    # 1. 아래에 DFS용 visited/result를 만든다.
    # 2. 바로 아래 def dfs(now): 를 작성하고 dfs(v)를 호출한다.
    # 3. 그 다음 BFS용 visited/result/queue를 만든다.
    # 4. while q: 로 BFS를 돌린 뒤 두 줄 출력한다.

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
