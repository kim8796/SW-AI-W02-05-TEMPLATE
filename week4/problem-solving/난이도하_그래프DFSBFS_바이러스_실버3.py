# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys


def main():
    input = sys.stdin.readline

    n = int(input())  # 컴퓨터 수
    m = int(input())  # 연결된 컴퓨터 쌍의 수

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # TODO: 1번 컴퓨터부터 DFS/BFS 수행
    # print(n, m)
    # print(graph)
    visited_dfs = [False] * (n+1)
    dfs_result = []
    def dfs(now):
        visited_dfs[now] = True
        dfs_result.append(now)
        for nxt in graph[now]:
            if not visited_dfs[nxt]:
                dfs(nxt)
    dfs(1)

    print(len(dfs_result)-1)

if __name__ == "__main__":
    main()
