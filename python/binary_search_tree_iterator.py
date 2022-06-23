''' 173. BINARY SEARCH TREE ITERATOR

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Source : https://leetcode.com/problems/binary-search-tree-iterator/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.Q = deque()
        inorder(root, self.Q)
        
    def next(self) -> int:
        if self.hasNext():
            return self.Q.popleft()

        return None

    def hasNext(self) -> bool:
        return len(self.Q) > 0


def inorder_recursive(current, Q):
    '''
    Uses call stack instead of explicit stack.
    '''

    # Go as left as possible 
    if current.left:
        inorder(current.left, Q)

    # Add node
    Q.append(current.val)

    # Go as right as possible
    if current.right:
        inorder(current.right, Q)
    
    
       
def inorder(start, Q):
    
    S = []
    current = start
    
    while S or current:
        
        # Go as left as possible
        while current:
            S.append(current)
            current = current.left
        
        # Current is None, pop top element and add it to the list
        current = S.pop()
        Q.append(current.val)
        
        # Go right if possible, might be None
        current = current.right