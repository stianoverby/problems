""" MERGE TWO BINARY TREES

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104

Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
source: https://leetcode.com/problems/merge-two-binary-trees/
"""

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        return bfs_merge(root1, root2)

def bfs_merge(root1, root2):
    
    node = TreeNode()

    if root1 and root2:
        
        node.val = root1.val + root2.val
        
        node.left = bfs_merge(root1.left, root2.left)
        node.right = bfs_merge(root1.right, root2.right)
        
        return node
    
    elif root1:
        return root1

    elif root2:
        return root2
