class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == '':
            return 0
        cache = [-1] * len(s)

        def step(index):
            if index == len(s) - 1:
                cache[index] = 0
                return index
            if s[index + 1] == ')':
                cache[index] = 2
                return index + 2
            index_ = index + 1
            while s[index_] == '(':
                index__ = step(index_)
                if index__ == index_:
                    break
                index_ = index__
                if index_ == len(s):
                    break

            if index_ < len(s) and s[index_] == ')':
                cache[index] = index_ + 1 - index
                return index_ + 1
            else:
                cache[index] = 0
                return index

        i = 0
        while i < len(s):
            while i < len(s) and s[i] == ')':
                i += 1
            if i == len(s):
                break
            if cache[i] == -1:
                step(i)
            elif cache[i] == 0:
                i += 1
            else:
                j = i + cache[i]
                if j == len(s):
                    break
                if s[j] == ')':
                    i = j + 1
                else:
                    step(j)
                    if cache[j] == 0:
                        i = j + 1
                    else:
                        cache[i] += cache[j]
        max_len = max(cache)
        return max_len if max_len != -1 else 0
