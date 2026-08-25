# https://www.geeksforgeeks.org/problems/huffman-encoding3345/1

import heapq

class Node:
    def __init__(self, freq, index, char="", left=None, right=None):
        self.freq = freq
        self.index = index
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.index < other.index
        return self.freq < other.freq


class Solution:
    def huffmanCodes(self, s: str, f: list[int]) -> list[str]:
        heap = []

        for i in range(len(s)):
            heapq.heappush(heap, Node(f[i], i, s[i]))

        # Only one character
        if len(heap) == 1:
            return ["0"]

        # Build Huffman tree
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            new_node = Node(
                left.freq + right.freq,
                min(left.index, right.index)
            )

            new_node.left = left
            new_node.right = right

            heapq.heappush(heap, new_node)

        answer = []

        def generate(node, code):
            if node.char != "":
                answer.append(code)
                return

            generate(node.left, code + "0")
            generate(node.right, code + "1")

        generate(heap[0], "")

        return answer
        
'''
Time Complexity: O(n log n)
Space Complexity: O(n)
'''