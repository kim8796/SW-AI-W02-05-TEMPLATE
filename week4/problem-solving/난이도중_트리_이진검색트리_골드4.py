# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
import sys

class Node :
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
def build_bst(preorder):
    idx = 0

    def helper(lower,upper):
        nonlocal idx

        if idx >=len(preorder):
            return None
        
        value = preorder[idx]
        if value < lower or value >upper :
            return None

        idx +=1
        node = Node(value)
        node.left = helper(lower,value)
        node.right = helper(value,upper)
        return node
    
    return helper(float('-inf'),float('inf'))

def midorder(root,res) : 

    if root is None:
        return 
    
    midorder(root.left,res)
    midorder(root.right,res)
    res.append(root.value)

def main():
    nums = list(map(int, sys.stdin.read().split()))
    

    root = build_bst(nums)
    res= []
    midorder(root,res)
    for r in res :
        print(r)



if __name__ == "__main__" :
    main()