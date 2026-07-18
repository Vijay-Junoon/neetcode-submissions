class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        graph = dict()
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                if pattern in graph:
                    graph[pattern].append(word)
                else:
                    graph[pattern] = [word]

        
        q = [beginWord]
        cnt = 1
        visited = set()

        while q:
            for i in range(len(q)):
                word = q.pop(0)
                
                if word == endWord:
                    return cnt

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for other_word in graph.get(pattern,0):
                        if other_word not in visited:
                            visited.add(other_word)
                            q.append(other_word)

            cnt += 1
        return 0







