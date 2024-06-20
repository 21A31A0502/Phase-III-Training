class TrieNode:
    def __init__(self):
        self.isEnding=False
        self.store=dict()
class Trie:
    def __init__(self):
        self.root=TrieNode() 
    def insertWord(self,word):
        currRoot=self.root
        n=len(word)
        for i in range(n):
            if word[i] not in currRoot.store:
                currRoot.store[word[i]] = TrieNode()
            currRoot=currRoot.store[word[i]]
        currRoot.isEnding=True    
        print(word,"inserted Succesfully")  
    def searchWord(self,word):
        currNode=self.root
        n=len(word)
        for i in range(n):
            ch=word[i]
            if ch not in currNode.store:
                return False    
            currNode=currNode.store[ch]
        return currNode.isEnding    
    def startsWith(self,word):
        currNode=self.root
        n=len(word)
        for i in range(n):
            ch=word[i]
            if ch not in currNode.store:
                return False 
            currNode=currNode.store[ch]
        return True 
obj = Trie()
obj.insertWord("cat")
obj.insertWord("computer")
obj.insertWord("compute")
print(obj.startsWith("com"))
print(obj.startsWith("comput"))
print(obj.startsWith("coma"))              