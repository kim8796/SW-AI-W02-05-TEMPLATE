# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493


import sys

def main():
    top = int(sys.stdin.readline())
    t_num = list(map(int,sys.stdin.readline().split()))
    res = [0]*top
    stack = []

    for i in range(top) :
        while stack and stack[-1][1] < t_num[i]:
            stack.pop()
        
        if stack : 
            res[i] = stack[-1][0] + 1
        stack.append((i,t_num[i]))

    print(*res)


  
    # for i in range(top-1,0,-1):
    #     j = i-1
    #     while j >= 0 :
    #         if t_num[i]<=t_num[j]:
    #             res[i] = j+1
    #             j-=1
    #             break
    #         else: 
    #             j-=1

    # print(res)
    # return res
if __name__ == "__main__":
    main()