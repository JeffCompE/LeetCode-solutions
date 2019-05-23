class Solution:
    # Manacher's algorithm O(n)
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return ''
        s_ = self.add_boundary(s)
        p = [0] * len(s_)  # array to store the maximum Palindrome length center around each index
        r = 0  # the next element to be examined
        c = 0  # the largest/left-most palindrome whose right boundary is r - 1
        i = 0  # the next palindrome to be calculated

        # The ending condition will allow us not to compute the remaining elements of p is r is already at the end
        # as the rest of the p must have length less than p[c].
        # If we want to compute all the p elements, change the condition to `i < len(s_)`
        while r < len(s_) - 1:
            # step 1: determine the case
            case_1 = False  # boolean value to indicate whether the case is case 1
            if i <= r:  # case 1 and 2
                i_mirror = c * 2 - i
                if p[i_mirror] < r - i - 1:
                    case_1 = True
                    p[i] = p[i_mirror]  # case 1
                else:
                    p[i] = r - i
            else:  # case 3
                p[i] = 0

            # step 2: expand (skipped if case 1)
            while not case_1 and i - p[i] - 1 >= 0 and i + p[i] + 1 < len(s_) and s_[i-p[i]-1] == s_[i+p[i]+1]:
                p[i] += 1

            # step 3: try to find the new largest/left-most palindrome and update c and r
            if i + p[i] > r:
                c = i
                r = i + p[i]
            i += 1

        max_length = 0
        center = 0
        for i, length in enumerate(p):
            if length > max_length:
                max_length = length
                center = i
        return self.remove_boundary(s_[center-max_length:center+max_length+1])

    def add_boundary(self, s: str) -> str:
        s_ = '#'
        for c in s:
            s_ += f'{c}#'
        return s_

    def remove_boundary(self, s: str) -> str:
        s_ = ''
        i = 0
        while i < len(s) - 1:
            i += 1
            s_ += s[i]
            i += 1
        return s_
