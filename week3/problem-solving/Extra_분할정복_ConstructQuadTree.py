# 분할정복 - Construct Quad Tree
# 문제 링크: https://leetcode.com/problems/construct-quad-tree/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
    

        self.grid = grid
        
        

        return self.divide(0,0,len(grid))



    def divide (self, x ,y ,size) -> Node:
        
        if size == 1 :
            return Node(self.grid[x][y],True,None,None,None,None)
        half = size//2

        tl = self.divide(x,y, half)
        tr = self.divide(x,y+half,half)
        bl = self.divide(x+half,y,half)
        br = self.divide(x+half,y+half,half)

        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and (tl.val == tr.val == br.val == bl.val) :
         
            return Node(tl.val,True,None,None,None,None)
        else: 
            return Node(0,False,tl,tr,bl,br)
        







# 사전합을 이용한 방법 



"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
    

        self.grid = grid
        size = len(grid)
        self.ps = [[0]*(size+1)for _ in range(size+1)]
        
        for i in range(size) :
            for j in range(size):
               self.ps[i+1][j+1] = self.ps[i][j+1] + self.ps[i+1][j] - self.ps[i][j] + self.grid[i][j]

                

        return self.divide(0,0,size)



    def divide (self, x ,y ,size) -> Node:
        
        if (size*size == self.ps[x+size][y+size]-self.ps[x][y+size]-self.ps[x+size][y]+self.ps[x][y]) or (self.ps[x+size][y+size]-self.ps[x][y+size]-self.ps[x+size][y]+self.ps[x][y] == 0):
            return Node(self.grid[x][y],True,None,None,None,None)
        half = size//2

        tl = self.divide(x,y, half)
        tr = self.divide(x,y+half,half)
        bl = self.divide(x+half,y,half)
        br = self.divide(x+half,y+half,half)

      
        return Node(0,False,tl,tr,bl,br)
        

        