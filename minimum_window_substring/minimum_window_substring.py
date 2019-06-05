class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == '' or t == '':
            return ''

        def valid_window():
            for char, count in window.items():
                if count < expected_window[char]:
                    return False
            return True

        window = dict()
        expected_window = dict()
        for char in t:
            window[char] = 0
            if char in expected_window:
                expected_window[char] += 1
            else:
                expected_window[char] = 1

        find = False
        l_ans, r_ans = 0, len(s) - 1
        l = r = 0
        if s[0] in window:
            window[s[0]] += 1
        while l <= r and r < len(s):
            if valid_window():
                find = True
                if r - l < r_ans - l_ans:
                    l_ans, r_ans = l, r
                else:
                    if s[l] in window:
                        window[s[l]] -= 1
                    l += 1
            else:
                r += 1
                if r == len(s):
                    break
                if s[r] in window:
                    window[s[r]] += 1
        return s[l_ans:r_ans + 1] if find else ''
