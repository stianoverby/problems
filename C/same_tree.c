/* Same tree
 * Given the roots of two binary trees p and q, write a function to check if they are the same or not.
 * Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
 *
 * The number of nodes in both trees is in the range [0, 100].
 * -104 <= Node.val <= 104
 *
 *
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 *
 * Source:  https://leetcode.com/problems/same-tree/
 */

bool isSameTree(struct TreeNode *p, struct TreeNode *q);
bool same_value(int val1, int val2);
bool same_structure(struct TreeNode *p, struct TreeNode *q);

bool isSameTree(struct TreeNode *p, struct TreeNode *q)
{
    return same_structure(p, q);
}
bool same_value(int val1, int val2)
{
    if (val1 == val2){return 1;}
    return 0;
}

bool same_structure(struct TreeNode *p, struct TreeNode *q)
{
    if (p == NULL && q == NULL){return 1;}
    if (p == NULL || q == NULL){return 0;}

    if (!same_value(p->val, q->val)){return 0;}

    return same_structure(p->left, q->left) &&
           same_structure(p->right, q->right);
}
