from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: 
                return [0, 0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)
            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)
            return [withRoot, withoutRoot]
        return max(dfs(root))
    

print(Solution().rob(TreeNode(4, left=TreeNode(1, left=TreeNode(2, left=TreeNode(3))))))



#       4 <--
#      / 
#     1
#    /
#   2
#  /
# 3  <--