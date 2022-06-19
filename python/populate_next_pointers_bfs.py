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
        return bfs_connect(root)


def bfs_connect(root):

    node = root

    # Initialize a queue for traversing the graph
    Q = [node]

    N_nodes_in_layer = 2

    # Traverse the whole graph
    while Q:

        node = Q.pop(0)

        # We are adding None elements to our queue, so we have to check so that we dont do any operations on a None object
        if node:
            Q.append(node.left)
            Q.append(node.right)

            # Check if we have reached a full layer so that we traverse the queue to set the next pointers
            if len(Q) == N_nodes_in_layer:
                N_nodes_in_layer *= 2

                # Add next to every node in layer
                for low_ptr in range(len(Q) - 1):

                    for high_ptr in range(low_ptr + 1, len(Q)):

                        # Only add node as next pointer if it is not None
                        if Q[high_ptr] != None:

                            Q[low_ptr].next = Q[high_ptr]

                            # Let us set the low_ptr to the current position of the high_ptr so that we
                            # dont loof for a next pointer for None objects
                            low_ptr = high_ptr
                            break

    return root
