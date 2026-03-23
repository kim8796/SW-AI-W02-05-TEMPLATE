# 그래프, DFS, BFS - 아침 산책 (백준 골드3)
# 문제 링크: https://www.acmicpc.net/problem/21606
import sys

def main():
    input = sys.stdin.readline

    n = int(input())
    is_indoor = [False] + [state == "1" for state in input().strip()]

    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
 
    visited = [False] * (n + 1)
    answer = 0
    def dfs(now):
        visited[now] = True
        indoor_count = 0
    
        for nxt in graph[now]:
            if is_indoor[nxt]:
                indoor_count += 1
            elif not visited[nxt]:
                indoor_count += dfs(nxt)
    
        return indoor_count
    
    for v in range(1, n + 1):
        if is_indoor[v]:
            for nxt in graph[v]:
                if is_indoor[nxt]:
                    answer += 1
        elif not visited[v]:
            k = dfs(v)
            answer += k * (k - 1)
    
    print(answer)



if __name__ == "__main__" :
    main()
