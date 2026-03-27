# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173


import sys

def main():

    n = int(sys.stdin.readline())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    def j_dfs(x,y):
        if graph[x][y] == -1:
            return True
        if visited[x][y] :
            return False
        visited[x][y] = True
        move = graph[x][y]
        x_move = False
        y_move = False
        if x+move < n :
            x_move = j_dfs(x+move,y)
        if y+move < n :
            y_move = j_dfs(x,y+move)
        
        return x_move or y_move

    if j_dfs(0,0):
        print("HaruHaru")
    else:
        print("Hing")

if __name__ == "__main__":
    main()