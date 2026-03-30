# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys


def main():
    input = sys.stdin.readline

    expression = input().strip()

    li = expression.split('-')
    base = li[0].split('+')
    b_sum = 0
    for b in base:
        b_sum += int(b)
    for l in li[1:] :
        nums = l.split('+')
        sums = 0
        for n in nums:
            sums += int(n)
        b_sum -= sums

    print(b_sum)
if __name__ == "__main__":
    main()
