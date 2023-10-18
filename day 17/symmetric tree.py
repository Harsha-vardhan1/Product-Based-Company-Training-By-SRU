# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l1=[]
        def first(root):
            if root==None:
                l1.append(None)
                return
            l1.append(root.val)
            first(root.left)
            first(root.right)
        first(root.left)
        l2=[]
        def second(root):
            if(root==None):
                l2.append(None)
                return
            second(root.left)
            second(root.right)
            l2.append(root.val)
        second(root.right)
        return l1==l2[::-1]