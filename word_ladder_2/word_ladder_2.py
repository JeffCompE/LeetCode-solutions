from collections import deque
from typing import List
from string import ascii_lowercase


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # edge case
        endWord_node = None
        beginWord_node = None
        for i, word in enumerate(wordList):
            if word == endWord:
                endWord_node = i
                break
            elif word == beginWord:
                beginWord_node = i
        if endWord_node is None:
            return []

        if beginWord_node is None:
            wordList.append(beginWord)
            beginWord_node = len(wordList) - 1

        wordDict = {}
        for i, word in enumerate(wordList):
            wordDict[word] = i

        N = len(wordList)
        # build the graph
        graph = {}

        def get_adjacent_nodes(node):
            adjacent_nodes = graph.get(node, None)
            if adjacent_nodes:
                return adjacent_nodes
            adjacent_nodes = []
            word = wordList[node]
            # wordDict.pop(word)
            for i, old_char in enumerate(word):
                for new_char in ascii_lowercase:
                    if old_char != new_char:
                        adjacent_word = word[:i] + new_char + word[i + 1:]
                        adjacent_node = wordDict.get(adjacent_word, None)
                        if adjacent_node is not None:
                            adjacent_nodes.append(adjacent_node)
            graph[node] = adjacent_nodes
            return adjacent_nodes

        def bfs(des):
            """Calculate the minimum distances from vertices to the target until start is met
            """
            dist = [None] * N
            dist[des] = 0
            nodes = [des]
            d = 1
            while nodes:
                temp = deque()
                for node in nodes:
                    next_nodes = get_adjacent_nodes(node)
                    for next_node in next_nodes:
                        if dist[next_node] is None:
                            dist[next_node] = d
                            if next_node == beginWord_node:
                                break
                            temp.append(next_node)

                d += 1
                nodes = list(temp)
            return dist

        min_dists = bfs(endWord_node)

        ladders = []
        ladder = []
        def dfs(node):
            ladder.append(wordList[node])
            if node == endWord_node:
                ladders.append(list(ladder))
                ladder.pop()
                return
            next_nodes = get_adjacent_nodes(node)
            if not next_nodes:
                ladder.pop()
                return
            for next_node in next_nodes:
                if min_dists[next_node] is not None and min_dists[node] - min_dists[next_node] == 1:
                    dfs(next_node)
            ladder.pop()

        dfs(beginWord_node)
        return ladders
