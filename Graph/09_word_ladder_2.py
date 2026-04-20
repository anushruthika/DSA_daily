# Time: O(N * M * 26 * P)
# Space: O(N * P)
# N → number of words in wordList
# M → length of each word
# 26 → all character replacements
# P → number of shortest paths
# 126. Word Ladder II

#####
# BFS
####
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            new_layer = collections.defaultdict(list)
            # to get all keys
            for w in layer:
                if w ==endWord:
                    res.extend(layer[w])
                else:
                    for ind in range(len(w)):
                        for let in "abcdefghijklmnopqrstuvwxyz":
                            new_word = w[:ind]+let+w[ind+1:]
                            if new_word in wordList:
                                new_layer[new_word] += [l+[new_word] for l in layer[w]]
                                wordList.remove(new_word)
            wordList-=set(new_layer.keys())
            layer = new_layer 
        return res
import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {beginWord: [[beginWord]]}

        while layer:
            new_layer = collections.defaultdict(list)

            # 🔥 remove visited words early (reduces memory)
            wordList -= set(layer.keys())

            for w in layer:
                if w == endWord:
                    res.extend(layer[w])
                else:
                    for ind in range(len(w)):
                        for let in "abcdefghijklmnopqrstuvwxyz":
                            new_word = w[:ind] + let + w[ind+1:]

                            if new_word in wordList:
                                # 🔥 limit growth by appending carefully
                                for path in layer[w]:
                                    new_layer[new_word].append(path + [new_word])

            # 🔥 early stop (VERY IMPORTANT)
            if res:
                return res

            layer = new_layer

        return res
