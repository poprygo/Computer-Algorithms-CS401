class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = 0  

        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1
            for word in dictionary:
                word_len = len(word)
                if i >= word_len and s[i - word_len:i] == word:
                    dp[i] = min(dp[i], dp[i - word_len])
        return dp[-1]

sol = Solution()

