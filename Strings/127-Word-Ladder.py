from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        buffer = {}
        self.preProcess(beginWord, endWord, wordList, buffer)
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        while queue:
            word, level = queue.popleft()
            if word not in visited:
                if word == endWord:
                    return level
                visited.add(word)
                for i in xrange(len(word)):
                    template = word[:i] + "_" + word[i+1:]
                    if template in buffer:
                        for candidate in buffer[template]:
                            queue.append((candidate, level+1))
        return 0

    def preProcess(self, beginWord, endWord, wordList, buffer):
        wordList = wordList | set([beginWord, endWord])
        for word in wordList:
            for i in xrange(len(word)):
                template = word[:i] + "_" + word[i+1:]
                if template not in buffer:
                    buffer[template] = [word]
                else:
                    buffer[template] += [word]
            
        
    
        
