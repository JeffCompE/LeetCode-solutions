class Solution:
    def lengthOfLongestSubstring_v1(self, s: str) -> int:
        """Sliding window (hashed set)
        """
        l = 0
        r = l
        str_len = len(s)
        max_length = 0
        set_of_chars = set()
        while l < str_len:
            while r < str_len:
                char = s[r]
                if char in set_of_chars:
                    break
                set_of_chars.add(char)
                r += 1

            if len(set_of_chars) > max_length:
                max_length = len(set_of_chars)
            set_of_chars.remove(s[l])
            l += 1

        return max_length

    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        """Sliding window (hashed map)
        """
        l = 0
        r = l
        str_len = len(s)
        max_length = 0
        index = dict()
        while r < str_len:
            char = s[r]
            if char in index and l <= index[char]:
                if r - l > max_length:
                    max_length = r - l
                l = index[char] + 1
            index[char] = r
            r += 1

        if r - l > max_length:
            max_length = r - l
        return max_length
