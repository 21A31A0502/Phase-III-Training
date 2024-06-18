def kthSmallest(root,k):
        inorder = []
 
        def collectInorderTraversal(currNode):
            if not currNode:
                return 
 
            collectInorderTraversal(currNode.left)
            inorder.append(currNode.val)
            collectInorderTraversal(currNode.right)
 
        collectInorderTraversal(root)
        return inorder[k - 1]
root = [3,1,4,None,2]
k = 1
print(kthSmallest(root,k))