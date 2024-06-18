def isValidBST(root):
        inorder = []
 
        def findInorder(root):
            if not root:
                return 
 
            findInorder(root.left)
            inorder.append(root.val)
            findInorder(root.right)
 
        findInorder(root)
        for index in range(1, len(inorder)):
            if inorder[index] <= inorder[index - 1]:
                return False 
        return True
root = [5,1,4,None,None,3,6]
print(isValidBST(root))
        