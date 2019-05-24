class Solution:
    def myAtoi(self, s: str) -> int:
        num_set = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        s = s.lstrip(' ')
        if len(s) == 0:
            return 0

        sign = 1
        if s[0] == '+' or s[0] == '-':
            sign = 1 if s[0] == '+' else -1
            s = s[1:]
        s = s.lstrip('0')

        ans = 0
        for char in s:
            num = num_set.get(char, None)
            if num is None:
                break
            ans = ans * 10 + num
            if ans > 2147483647:
                ans = 2147483647 if sign == 1 else -2147483648
                return ans

        return sign * ans
