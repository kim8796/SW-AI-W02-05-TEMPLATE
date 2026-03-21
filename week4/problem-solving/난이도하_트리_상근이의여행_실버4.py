# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 첫줄 테스트케이스 수 (결과값 갯수)


import sys
from collections import deque

def main():
    res_count = int(sys.stdin.readline())
    for _ in range(res_count):
        f,m = map(int,sys.stdin.readline().split())
        flight = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
        print(f-1)




if __name__ == "__main__" :
    main()