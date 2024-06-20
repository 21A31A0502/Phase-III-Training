class TrieNode:
    def __init__(self):
        self.isEnding = False 
        self.store = dict()

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        currRoot = self.root 
        n = len(word)
        for index in range(n):
            if word[index] not in currRoot.store:
                currRoot.store[word[index]] = TrieNode()
 
            currRoot = currRoot.store[word[index]]
        currRoot.isEnding = True 
        

    def search(self, word):
        currRoot = self.root 
        n = len(word)
        def helper(currRoot, index):
            if index == n:
                return currRoot.isEnding
            elif word[index] != '.' and word[index] not in currRoot.store:
                return False
                
            if word[index] != '.':
                return helper(currRoot.store[word[index]], index + 1)
                
            for ch in currRoot.store.keys():
                if helper(currRoot.store[ch], index + 1):
                    return True
            return False
            

        return helper(currRoot, 0)       
# Instantiate the WordDictionary
wordDictionary = WordDictionary()

# Add words to the dictionary
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.addWord("pad")

# Search for specific words and patterns
print(wordDictionary.search("pad"))   
print(wordDictionary.search("bad"))   
print(wordDictionary.search("mad"))  
print(wordDictionary.search("dad"))   
print(wordDictionary.search("..d"))   
print(wordDictionary.search("b.."))   
print(wordDictionary.search(".ad"))   
print(wordDictionary.search("p.."))   
print(wordDictionary.search("..."))   
print(wordDictionary.search("b.d"))   
print(wordDictionary.search("b..d"))  
    