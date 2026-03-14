# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
import sys


def main():
    a, b, c = map(int, sys.stdin.readline().split())

    res = power(a, b, c)
    print(res)

def power(a, b, c):
    # 빠른 거듭제곱: 재귀 호출 한 번만 수행하도록 중간 결과를 저장
    if b == 1:
        return a % c

    half = power(a, b // 2, c)
    half_sq = (half * half) % c

    if b % 2 == 1:
        return (half_sq * (a % c)) % c
    else:
        return half_sq


if __name__ == "__main__":

    main()