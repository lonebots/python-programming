'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

'''

class TrieNode :
    def __init__(self) :
        self.children = {}
        self.isWord = False

class WordDictionary:
    '''
    The best data structure for implementing a word storage and easy search is Trie
    '''
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root 
        for char in word :
            if char not in node.children :
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True
        
    def search(self, word: str) -> bool:
        node = self.root 
        self.res = False
        self.dfs(node,word) 
        return self.res
        
    def dfs (self,node,word) :
        if not word :
            if node.isWord :
                self.res = True
            return

        if word[0] == '.' :
            for child in node.children.values() :
                self.dfs (child,word[1:])

        else :
            node = node.children.get(word[0])
            if not node :
                return 
            self.dfs(node,word[1:])
 

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)