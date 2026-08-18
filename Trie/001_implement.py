# A Trie (pronounced "try") is a tree-like data structure used to store strings.
# https://www.youtube.com/watch?v=dBGUmUQhjaM&t=121s
# 208. Implement Trie (Prefix Tree)
# Space Complexity to store Trie: (In the worst case, there is no shared prefix between the words.) 
# O(N×L): N words × L characters or in short O(number of unique prefixes)


class TrieNode:
    def __init__(self):
        # children dictionary: eg: "a":TrieNode({"p":TrieNode({},True)},False)
        self.children = {}
        self.ends_with = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
    # TC: O(L) L: length of word.
    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] =  TrieNode()
            temp = temp.children[ch]
        temp.ends_with = True
    # TC: O(L) L: length of word.
    def search(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        # if not temp.ends_with:
        #     return False
        # return True
        return temp.ends_with

    #  whether there are words starting with prefix or not
    # TC: O(L) L: length of prefix.
    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for ch in prefix:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
