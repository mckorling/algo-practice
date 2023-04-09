# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# start at root
# use recursion
# check if a subtree contains a 1
# if it contains a 1, do nothing
# if it is only 0s/None, change that child to None
def pruneTree(root):
    # if self.subtree_contains_one(root):
    #     return root
    # else:
    #     return None
    return root if subtree_contains_one(root) else None

def subtree_contains_one(node):
    # base case: leaf
    if node is None:
        return False

    left_has_one = subtree_contains_one(node.left)
    right_has_one = subtree_contains_one(node.right)

    if not left_has_one:
        node.left = None
    if not right_has_one:
        node.right = None
    
    return left_has_one or right_has_one or (node.val == 1)


root = TreeNode(1)
a = TreeNode(0)
b = TreeNode(0)
c = TreeNode(0)

d = TreeNode(1)
e = TreeNode(0)
f = TreeNode(1)
root.left = a
root.right = d
a.left = b
a.right = c
d.left = e
d.right = f

print(pruneTree(root))