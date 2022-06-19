"""
Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
"""


class Solution:
    def in_order_traversal(self, root: Optional[TreeNode]) -> List[int]:

        traversal = list()
        stack = list()
        visited = set()

        if root is not None:
            traversal = iterative_dfs(root, traversal, stack, visited)

        return traversal


def iterative_dfs(
    root: Optional[TreeNode],
    traversal: List[int],
    stack: List[TreeNode],
    visited: Set[TreeNode],
) -> List[TreeNode]:

    """
    Adding root to stack so that we can start the iteration.
    """
    stack.append(root)

    while len(stack) > 0:

        """
        The element on the top of the stack is the node we are visiting.
        """
        visiting = stack[len(stack) - 1]

        # We want to go as far left as possible in the binary tree.
        if visiting.left is not None and visiting.left not in visited:
            stack.append(visiting.left)
            continue

        """
        We have went as far left as possible. Time to add what is on top of the
        stack to our traversal.
        """
        node = stack.pop()
        traversal.append(node.val)
        visited.add(node)

        """
        If we now can go right, we do that.
        """
        if visiting.right is not None and visiting.right not in visited:
            stack.append(visiting.right)
            continue

    return traversal
