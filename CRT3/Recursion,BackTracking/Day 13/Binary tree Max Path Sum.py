def maxPathSum(root):
        result = [-1000000000]
 
        def helper(currNode):
            if currNode == None:
                return 0 
            elif currNode.left == None and currNode.right == None:
                result[0] = max(result[0], currNode.val)
                return max(0, currNode.val)
 
 
            leftMaxValue = helper(currNode.left)
            rightMaxValue = helper(currNode.right)
            # logic here
            value1 = currNode.val
            value2 = currNode.val + leftMaxValue
            value3 = currNode.val + rightMaxValue
            value4 = leftMaxValue + currNode.val + rightMaxValue
            result[0] = max([result[0], value1, value2, value3, value4])
 
            return currNode.val + max([leftMaxValue, rightMaxValue])
 
 
        helper(root)
        return result[0]
root = [-10,9,20,None,None,15,7]
print(maxPathSum(root))