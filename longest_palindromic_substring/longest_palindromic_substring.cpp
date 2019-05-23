// Dynamic programming approach O(n^2)
class Solution {
public:
    string longestPalindrome(string s) {
        int size = s.length();
        if (size == 0) return s;

        int max_len = 1;
        string max_p = s.substr(0, 1);
        int p[size][size];
        p[0][0] = 1;
        for (int i = 1; i < size; i++) {
            p[i][i] = 1;
            p[i][i - 1] = (s[i] == s[i - 1]) ? 1 : 0;
            if (max_len < 2 && p[i][i - 1]) max_len = 2, max_p = s.substr(i - 1, 2);

            for (int j = i - 2; j >= 0; j--) {
                p[i][j] = (s[i] == s[j] && p[i - 1][j + 1]) ? 1 : 0;
                if (p[i][j] && i - j + 1 > max_len) {
                    max_len = i - j + 1;
                    max_p = s.substr(j, max_len);
                }
            }
        }
        return max_p;
    }
};
