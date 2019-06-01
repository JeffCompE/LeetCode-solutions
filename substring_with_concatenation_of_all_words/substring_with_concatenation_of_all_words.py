class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(s) == 0:
            return []

        counts = dict()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        word_len = len(words[0])
        window = dict()
        ans = list()

        for i in range(word_len):
            l = r = i
            while r <= len(s):
                cur_word = s[r:r + word_len]

                if cur_word not in counts:
                    l = r = r + word_len
                    window.clear()
                else:
                    if window.get(cur_word, 0) < counts[cur_word]:
                        window[cur_word] = window.get(cur_word, 0) + 1
                        r += word_len
                    else:
                        while s[l:l + word_len] != cur_word:
                            window[s[l:l + word_len]] -= 1
                            l += word_len
                        l += word_len
                        r += word_len
                    if window == counts:
                        ans.append(l)
        return ans
