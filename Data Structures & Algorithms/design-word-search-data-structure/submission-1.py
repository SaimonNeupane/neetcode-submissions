class Node:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=Node()

        

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=Node()
            curr=curr.children[c]
        curr.end=True
        

        

    def search(self, word: str) -> bool:
        def dfs(m,root):
            curr=root
            for i in range(m,len(word)):
                if word[i] in curr.children:
                    curr=curr.children[word[i]]
                else:
                    if word[i]!='.':
                        return False
                    else:
                        for node in curr.children.values():
                            if dfs(i+1,node):
                                return True
                        return False
            return curr.end
        return dfs(0,self.root)
                    



      
                
        
