def printBinaryNum(size,res,n):
    if size==n:
        print(res)
        return 
    printBinaryNum(size+1,res+'1',n)
    printBinaryNum(size+1,res+'0',n)
n=4
printBinaryNum(0,'',n)    