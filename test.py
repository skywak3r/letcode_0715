import collections

n = int(input())
nums = list(map(int,input().split()))
fathers = list(map(int,input().split()))

tree = collections.defaultdict(list)
for i in range(len(fathers)):
    tree[fathers[i]].append(i)

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def rob(start):
    if len(tree[start]) == 0:
        return 0
    if