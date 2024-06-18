class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def levelOrder(root):
        result = []
        if root == None:
            return result

        Q = []
        Q.append(root)

        while Q:
            n = len(Q)
            subResult = []
            for i in range(n):
                current = Q.pop(0)
                subResult.append(current.val)

                if current.left != None:
                    Q.append(current.left)

                if current.right != None:
                    Q.append(current.right)

            result.append(subResult)
        return result
root = [3,9,20,None,None,15,7]
print(levelOrder(root))