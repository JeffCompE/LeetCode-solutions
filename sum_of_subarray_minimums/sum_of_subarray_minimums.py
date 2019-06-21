from collections import deque

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10**9 + 7

        N = len(A)
        stack = deque()  # stack is monotone increasing
        right_boundary = [None] * N
        left_boundary = [None] * N
        for i in range(N):
            while stack and A[stack[-1]] > A[i]:
                right_boundary[stack.pop()] = i
            stack.append(i)
        while stack:
            right_boundary[stack.pop()] = N

        for i in range(N - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                left_boundary[stack.pop()] = i
            stack.append(i)
        while stack:
            left_boundary[stack.pop()] = -1

        ans = 0
        for i in range(N):
            ans += A[i] * (right_boundary[i] - i) * (i - left_boundary[i])
        return ans % MOD
