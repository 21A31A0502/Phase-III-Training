class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
        # Encode 
        token = []

        def helper(currNode):
            if currNode == None:
                token.append("N")
                return 

            token.append(str(currNode.val))
            helper(currNode.left)
            helper(currNode.right)

        helper(root)
        return "#".join(token)
        

def deserialize(data):
        token = data.split("#")
        index = [0]
        n = len(token)

        def helper():
            if index[0] >= n:
                return None 
            elif token[index[0]] == "N":
                index[0] += 1 
                return None 

            node = TreeNode(int(token[index[0]]))
            index[0] += 1
            node.left = helper()
            node.right = helper()
            return node

        return helper()
root = [1,2,3,None,None,4,5]
print(serialize(root))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))