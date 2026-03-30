# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

import sys


def main():
    input = sys.stdin.readline

    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        coins = list(map(int, input().split()))
        target = int(input().strip())

        
        # TODO: solve(n, coins, target) 작성 후 결과 출력
        # answer = solve(n, coins, target)
        # print(answer)


if __name__ == "__main__":
    main()
