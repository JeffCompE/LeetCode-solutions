class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        str_len = len(s)
        ans = ''
        space = numRows - 1  # spacing between adjacent vertical lines

        l_space = space
        r_space = space - l_space
        for i in range(numRows):

            if i < str_len:
                ans += s[i]
            else:
                break

            j = i
            while j < str_len:
                if l_space != 0:
                    j += l_space * 2
                    if j < str_len:
                        ans += s[j]
                    else:
                        break

                if r_space == 0:
                    continue
                j += r_space * 2
                if j < str_len:
                    ans += s[j]
                else:
                    break
            l_space -= 1
            r_space += 1
        return ans
