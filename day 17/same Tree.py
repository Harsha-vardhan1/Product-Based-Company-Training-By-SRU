# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1=[]
        def first(root):
            if(root==None):
                l1.append(None)
                return
            l1.append(root.val)
            first(root.left)
            first(root.right)
        first(p)
        l2=[]
        def second(root):
            if(root==None):
                l2.append(None)
                return
            l2.append(root.val)
            second(root.left)
            second(root.right)
        second(q)
        print(l1,l2,sep=",")
        return l1==l2
        