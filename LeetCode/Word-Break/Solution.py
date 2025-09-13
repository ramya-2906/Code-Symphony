class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        @lru_cache(None)
        def can_break(start: int) -> bool:
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and can_break(end):
                    return True
            return False
        return can_break(0)