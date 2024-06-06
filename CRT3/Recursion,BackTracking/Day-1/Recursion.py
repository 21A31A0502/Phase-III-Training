'''
def fun(i,n):
    if i>=n:
        print("Base Condition")
        return 
    print("Hello",i)
    print("World",i)
    fun(i+1,n)
    print("This",i)
    print("is recursion",i)
fun(1,8)    


def fun(i,n):
    if i>=n:
        print("Base Condition")
        return 
    print("ending line",i)
    for j in range(1,i):
        print(j)
    fun(i+1,n)
    print("strating line",i)
    
fun(1,8)    

'''

def printThis(position):
    print("leaving here",position)
    if position == 0:
        print("Base condition")
        return
    if position%2 == 1:
        print("even position:",position)
    else:
        print("odd position:",position)
    printThis(position-1)
    for index in range (position,-1,-1):
        print("index is:",index)
    print("entering here",position)  
printThis(11)