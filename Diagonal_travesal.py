'''Diagonal tree traversal is a way of traversing a binary tree along the diagonals. 
In a diagonal traversal, move from the left child to the right child of the same parent, 
and then move down to the next level, repeating the process. 
This traversal can be visualized as moving along the diagonals of the tree.'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diagonal_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        while node:
            result.append(node.val)

            if node.left:
                queue.append(node.left)

            node = node.right

    return result


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))

result = diagonal_traversal(root)
print(result)  
