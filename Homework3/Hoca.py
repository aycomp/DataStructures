# Alternative 1: More OO
class TreeNode:
    def __init__(self, value):
        self._value = value
        self._children = []


# Alternative 2: Data centric
# [value,[]]

class GenTree:
    def __init__(self, data=None):
        self._root = data

    def height(self):
        return GenTree.height_from(self._root)

    def height_from(node):
        if len(node) > 2:
            print(node[0])
        value, children = node
        # Base case
        if (children == []):  # Leaf
            return 1
        # Recursive
        max_height = 0
        for child in children:
            child_height = GenTree.height_from(child)
            if child_height > max_height:
                max_height = child_height
        return max_height + 1


initial_data = [
    1, [
        [2, []],
        [3, []],
        [4,
         [
             [8, []]
         ]
         ],
        [5,
         [
             [9,
              [
                  [10, []],
                  [11, []]
              ],
              ]
         ]
         ],
        [6, []],
        [7, []]
    ]
]

mytree = GenTree(initial_data)
