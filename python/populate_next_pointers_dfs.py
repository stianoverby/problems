""" Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        return dfs(root, None)
        
def dfs(root, right):
    
    if root == None:
        return None
    
    # The next of this node has to be the right child of
    # the parent
    root.next = right
    
    # Continue traversing the children of this node
    dfs(root.left, root.right)
    
    # If the right child of the parent is a node, the left
    # child of that node has to be the next of the currents
    # node's right child
    if right:
        dfs(root.right, right.left)
    
    # If that is not the case, the next node has to be None
    else:
        dfs(root.right, None)
        
    return root
     
