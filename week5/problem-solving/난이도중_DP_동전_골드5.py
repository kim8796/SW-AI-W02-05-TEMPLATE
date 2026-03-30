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
        solve(n,coins,target)
        
def solve(n,coins,target):
    dp = [0]*(target+1)
    dp[0] = 1
    for coin in coins:
        for money in range(coin,target+1):
            dp[money] += dp[money-coin]
    print(dp[target])

if __name__ == "__main__":
    main()
