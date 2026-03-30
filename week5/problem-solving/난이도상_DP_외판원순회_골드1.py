# DP - 외판원 순회 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/2098

import sys


def solve(n, cost):
    INF = 10**15
    all_visited = (1 << n) - 1
    dp = [[-1] * (1 << n) for _ in range(n)]

    def dfs(city, visited):
        if visited == all_visited:
            if cost[city][0] == 0:
                return INF
            return cost[city][0]

        if dp[city][visited] != -1:
            return dp[city][visited]

        min_cost = INF

        for next_city in range(n):
            if visited & (1 << next_city):
                continue
            if cost[city][next_city] == 0:
                continue

            next_visited = visited | (1 << next_city)
            total_cost = cost[city][next_city] + dfs(next_city, next_visited)
            min_cost = min(min_cost, total_cost)

        dp[city][visited] = min_cost
        return min_cost

    return dfs(0, 1)


def main():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n = int(input().strip())
    cost = [list(map(int, input().split())) for _ in range(n)]

    answer = solve(n, cost)
    print(answer)


if __name__ == "__main__":
    main()
