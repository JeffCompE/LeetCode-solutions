class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = set()  # memorize the false case

        def helper(s_index, p_index):
            if p_index == len(p) and s_index == len(s):
                return True

            while p_index < len(p):
                if (s_index, p_index) in memo:
                    return False

                if p_index + 1 < len(p) and p[p_index + 1] == '*':
                    char = p[p_index]
                    if char == '.':
                        while s_index <= len(s):
                            if (s_index, p_index) in memo:
                                return False

                            if helper(s_index, p_index + 2):
                                return True
                            else:
                                memo.add((s_index, p_index + 2))
                            s_index += 1
                        memo.add((s_index, p_index))
                        return False

                    else:
                        while s_index <= len(s):
                            if (s_index, p_index) in memo:
                                return False

                            if helper(s_index, p_index + 2):
                                return True
                            else:
                                memo.add((s_index, p_index + 2))

                            if s_index == len(s) or s[s_index] != char:
                                break
                            if s[s_index] == char:
                                s_index += 1
                        memo.add((s_index, p_index))
                        return False

                else:
                    if s_index == len(s):
                        memo.add((s_index, p_index))
                        return False

                    if p[p_index] == '.' or p[p_index] == s[s_index]:
                        s_index += 1
                        p_index += 1
                    else:
                        memo.add((s_index, p_index))
                        return False

            if (s_index, p_index) in memo:
                return False

            if s_index == len(s):
                return True
            else:
                memo.add((s_index, p_index))
                return False

        return helper(0, 0)
