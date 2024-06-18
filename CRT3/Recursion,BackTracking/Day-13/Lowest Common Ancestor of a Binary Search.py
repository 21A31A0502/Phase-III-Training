def lowestCommonAncestor(root,p,q):
        def findPath(currRoot, value, path):
            if not currRoot:
                return False 
 
            path.append(currRoot)
            if currRoot.val == value.val:
                return True
 
            isFoundInLeftSubtree = findPath(currRoot.left, value, path)
            if isFoundInLeftSubtree:
                return True 
            isFoundInRightSubtree = findPath(currRoot.right, value, path)
            if isFoundInRightSubtree:
                return True 
 
            path.pop()
            return False
        path1 = []
        findPath(root, p, path1)
 
        path2 = []
        findPath(root, q, path2)
 
        result = None 
        index = 0 
        while index < min(len(path1), len(path2)):
            if path1[index].val == path2[index].val:
                result = path1[index]
            else:
                break 
            index += 1
 
        return result
root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8
print(lowestCommonAncestor(root,p,q))

        