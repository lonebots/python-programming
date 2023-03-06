class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        not_count = 0
        allowed = set(allowed)
        for word in words :
            for char in word :
                if char not in allowed :
                    not_count += 1 
                    break
        return len(words) - not_count 