class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1
            else:
                magazine_count[char] = 1

        ransome_count = {}
        for char in ransomNote:
            if char in ransome_count:
                ransome_count[char] += 1
            else:
                ransome_count[char] = 1

        for key, value in ransome_count.items():
            if key in magazine_count and value <= magazine_count[key]:
                continue
            else:
                return False
        return True
