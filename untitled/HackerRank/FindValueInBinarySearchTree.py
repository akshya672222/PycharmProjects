class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None

def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = BSTreeNode(data)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_binarysearchtree(node.left, data);
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data);
    return node



def isPresent (root,val):
    print(val)
    bool = 0
    if not root is None:
        print ( root.value )
        if root.value == val:
            print('matched')
            bool = 1
            return bool
        else:
            if not root.left is None:
                bool = isPresent ( root.left , val )
                if bool == 1:
                    return bool
            if not root.right is None:
                bool = isPresent ( root.right , val )
                if bool == 1:
                    return bool
    return bool


_a = None
_a_size = int(input('size : '))
_a_i=0

while _a_i < _a_size:
    _a_item = input('Value : ')
    _a = _insert_node_into_binarysearchtree(_a, _a_item)
    _a_i += 1

_b = input('Search : ')

_result = isPresent (_a , _b )
print (_result)
