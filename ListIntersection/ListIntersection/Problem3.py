class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        # Return pre_order_traversal
        return '{val},{left},{right}'.format(val=self.val, left=repr(self.left), right = repr(self.right))

def serialize(node: Node) -> str:
    return node.__repr__()
    
# Do it first without regex
def deserialize(input: str) -> Node:

    # Don't have to keep track of a global because we return the array
    def process(tokens: str) -> Node:
        val, _, remainder = tokens.partition(',')
        if val == 'None':
            return None, remainder
        n = Node(val)
        n.left, remainder = process(remainder)
        n.right, remainder = process(remainder)
        return n, remainder

    out, _ = process(input)
    return out

#Doing this recursively always generates a DFS ordering
#Serialization can be done using pre-order, in-order, post-order (all DFS), level order (BFS: queue, not recursion)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
