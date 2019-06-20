from collections import deque

class Solution:
    # monotonic stack
    def oddEvenJumps(self, A: List[int]) -> int:

        def make_jump(sorted_list):
            jump = [0] * N
            stack = deque()
            for i in sorted_list:
                while stack and stack[-1] < i:
                    jump[stack.pop()] = i
                stack.append(i)
            return jump

        N = len(A)
        indices = list(range(N))
        indices.sort(key=lambda x: A[x])
        odd_jump = make_jump(indices)
        indices.sort(key=lambda x: A[x], reverse=True)
        even_jump = make_jump(indices)
        odd_jump[-1] = even_jump[-1] = N - 1

        for i in range(N - 2, -1, -1):
            if odd_jump[i] != 0:
                odd_jump[i] = even_jump[odd_jump[i]]
            if even_jump[i] != 0:
                even_jump[i] = odd_jump[even_jump[i]]

        count = 0
        for jump in odd_jump:
            if jump == N - 1:
                count += 1
        return count
