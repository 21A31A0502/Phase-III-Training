def printThis(n, result, openOnes, closedOnes):
    
    if closedOnes > openOnes:
        
        return
    if openOnes > (n // 2) or closedOnes > (n // 2):
        return
    if len(result) == n:
        print(result)
        return 
 
    printThis(n, result + "(", openOnes + 1, closedOnes)
    printThis(n, result + ")", openOnes, closedOnes + 1)
 
 
n = 8
printThis(n, "", 0, 0)

#==> Spend some time on that solution, go through line by line. Try to do one 
#dry run (pen and paper), by drawing the recursive call stack for may n = 8 
	
