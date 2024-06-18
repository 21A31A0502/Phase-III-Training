def lowestCommonAncestor( root,p,q):
        if not root:
            return None 
 
        currNode = root 
        while currNode:
            if currNode.val > p.val and currNode.val > q.val:
                currNode = currNode.left 
            elif currNode.val < p.val and currNode.val < q.val:
                currNode = currNode.right 
            else:
                return currNode 
        return None
root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8
print(lowestCommonAncestor(root,p,q))