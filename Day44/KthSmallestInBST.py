# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        l1=[]
        self.inorder(root,l1,k)
        return l1[k-1]
        
    def inorder(self,root,l1,k):
        if not root:
            return
        self.inorder(root.left,l1,k)
        l1.append(root.val)
        self.inorder(root.right,l1,k)
