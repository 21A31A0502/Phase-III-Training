class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST():
    #constructing a tree
    def addNode(self,root,value):
        newNode=Node(value)
        if root == None:
            return newNode
        if value<root.data:
            if root.left==None:
                root.left=newNode 
            else:
                self.addNode(root.left,value)
        else:
            if root.right==None:
                root.right=newNode 
            else:
                self.addNode(root.right,value)
    #tree traversals            
    def inorder(self,root):
        if root.left != None:
             
            self.inorder(root.left) 
        print(root.data,end=", ")
        if root.right !=None:
            self.inorder(root.right) 
    def preorder(self,root):
        print(root.data,end=", ")
        if root.left != None:         
            self.inorder(root.left)      
        if root.right !=None:
            self.inorder(root.right) 
    def postorder(self,root):
        if root.left != None:         
            self.inorder(root.left)     
        if root.right !=None:
            self.inorder(root.right) 
        print(root.data,end=", ")                              
    #levelorder traversals                           
    def level_order(self,root):
        
        q=[root]
        while len(q)!=0:
            ele=q.pop()
            print(ele.data,end=", ")
            if ele.left != None:
                q.append(ele.left)
            if ele.right != None:
                q.append(ele.right)

value=[16,9,25,4,15,83,8]
tree=BST()
root=None
root=tree.addNode(root,value[0])
print(root)
for i in range(1,len(value)):
    tree.addNode(root,value[i])
tree.inorder(root)
print()
tree.preorder(root)
print()
tree.postorder(root)
print()
tree.level_order(root)
print()
    

                