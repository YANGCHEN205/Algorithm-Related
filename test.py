'''
Author: 'YANGCHEN205' '1752685711@qq.com'
Date: 2024-09-22 12:58:25
LastEditors: 'YANGCHEN205' '1752685711@qq.com'
LastEditTime: 2024-09-22 13:20:50
FilePath: \算法学习\test.py
Description: 

Copyright (c) 2024 by ${'YANGCHEN205' '1752685711@qq.com'}, All Rights Reserved. 
'''


class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val < low:
            right = self.trimBST(root.right,low,high)
            return right
        elif root.val > high:
            left = self.trimBST(root.left,low,high)
            return left
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a sample binary search tree
#         3
#        / \
#       0   4
#        \
#         2
root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

# Initialize Solution and trim the BST
solution = Solution()
trimmed_tree = solution.trimBST(root, 1, 3)

# Function to print the tree in-order for verification
def print_in_order(node):
    if node:
        print_in_order(node.left)
        print(node.val, end=' ')
        print_in_order(node.right)

# Print the result
# Print the result
print_in_order(trimmed_tree)
