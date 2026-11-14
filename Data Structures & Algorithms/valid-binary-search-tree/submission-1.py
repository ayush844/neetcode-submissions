# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidRange(node, minVal, maxVal):
            if not node:
                return True

            if node.val >= maxVal or node.val <= minVal:
                return False

            isLeftValid = isValidRange(node.left, minVal, node.val)
            isRightValid = isValidRange(node.right, node.val, maxVal)

            return isLeftValid and isRightValid

        return isValidRange(root, float('-inf'), float('inf'))