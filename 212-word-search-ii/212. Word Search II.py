from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        rows, cols = len(board), len(board[0])
        result = set() 

        def dfs(r, c, node, path):
            if node.isEndOfWord:
                result.add(path)
            
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "#":
                return
            
            temp = board[r][c]
            if temp not in node.children:
                return
            
            board[r][c] = "#"
            if temp not in node.children:
                return
            
            board[r][c] = "#"

            for dr, dc in [(-1, 0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, node.children[temp], path + temp)
            
            board[r][c] = temp
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root, "")
        
        return list(result)