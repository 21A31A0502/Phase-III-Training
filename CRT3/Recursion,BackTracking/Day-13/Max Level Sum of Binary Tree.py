def maxLevelSum(root):
        if root == None:
            return 0
        Q = [root]
        resultLevel = 0 
        resultSum = -100000000
        currLevel = 1
        while len(Q) > 0:
            n = len(Q)
            currSum = 0
            for i in range(n):
                # step-1 (Deleting)
                currNode = Q.pop(0)
                
                # step-2 (Appending to subResult)
                currSum += currNode.val
                
                # step-3 (Enquing the left child)
                if currNode.left != None:
                    Q.append(currNode.left)
                    
                # step-4 (Enquing the right child)
                if currNode.right != None:
                    Q.append(currNode.right)
                
            if currSum > resultSum:
                resultSum = currSum 
                resultLevel = currLevel 
            currLevel += 1
        return resultLevel
root = [1,7,0,7,-8,None,None]
print(maxLevelSum(root))