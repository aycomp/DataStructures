output = ''

def SearchForLeft(postOrder, root):
    index = len(postOrder) - 1
    for c in postOrder[len(postOrder) - 2::-1]:
        index -= 1
        if c < root:
            return index

def SearchForRight(postOrder, root):
    index = len(postOrder) - 1
    for c in postOrder[len(postOrder) - 2::-1]:
        index -= 1
        if c > root:
            return index

def Concat(node):
    global output
    if node not in output:
        output += node

def PrintPreOrder(postOrder):
    global output
    root = postOrder[len(postOrder) - 1]
    Concat(root)

    lm = SearchForLeft(postOrder, root)
    if lm != None:  # left subtree exists
        PrintPreOrder(postOrder[:lm + 1])

    rm = SearchForRight(postOrder, root)
    if rm != None:  # right subtree exists
        PrintPreOrder(postOrder[:rm + 1])

if __name__ == '__main__':
    postOrder = input('Enter post-order traversal : ')  #postOrder = 'CFEALPOJTG'
    print('The pre-order traversal is : ', end='')
    PrintPreOrder(list(postOrder))
    print(output)