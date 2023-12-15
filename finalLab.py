from collections import defaultdict, deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def vertical_traversal(root):
    if not root:
        return []

    vertical_levels = defaultdict(list)

    queue = deque([(root, 0)])

    while queue:
        node, distance = queue.popleft()

        vertical_levels[distance].append(node.value)

        if node.left:
            queue.append((node.left, distance - 1))
        if node.right:
            queue.append((node.right, distance + 1))

    sorted_levels = sorted(vertical_levels.keys())

    result = [vertical_levels[distance] for distance in sorted_levels]

    flattened_result = [node for sublist in result for node in sublist][::-1]

    return flattened_result


# Example usage:
# Construct a sample binary tree
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7
#         \    \
#          8    9

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(9)
root.right.right.left = TreeNode(8)

result = vertical_traversal(root)
print(result)
