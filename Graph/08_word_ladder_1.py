# 127. Word Ladder

## optimized me: using word dict
# Time: O(N * L) => building pattern dictionary + BFS traversal (each word processed once)

# Space: O(N * L) => pattern dictionary + queue + visited set
from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        # Step 1: Build pattern dictionary
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                word_dict[pattern].append(word)

        # Step 2: BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, step = queue.popleft()

            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]

                for nei in word_dict[pattern]:
                    if nei == endWord:
                        return step + 1

                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, step + 1))

                # Important optimization: clear list to avoid re-processing
                word_dict[pattern] = []

        return 0

## GENERAL BFS APPROACH - generally people use this logic:

# Time: O(N * L * 26) => for each word, we try all L positions and 26 possible letters,
#                       and each valid word is processed at most once (removed from set)

# Space: O(N) => wordSet stores N words, and queue can hold up to N words in worst case

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque([(beginWord,1)])

        while queue:
            word,step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    # or for i in range(len(26)):
                    # ch(ord('a')+i)
                    formed = word[:i]+letter+word[i+1:]    
                    if formed in wordSet:
                        wordSet.remove(formed)
                        queue.append((formed,step+1))
        return 0


