# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

import sys
def main():
    
    k = int(sys.stdin.readline())
    input = []
    for i in range(k):
        input.append(int(sys.stdin.readline()))
    

    pair_sum = set()

    for i in range(k):
        for j in range(k):
            pair_sum.add(input[i]+input[j])
    
    for i in range(k-1,-1,-1):
        for j in range(k):
            if (input[i]-input[j]) in pair_sum:
                print(input[i])
                return



if __name__ == "__main__":
    main()