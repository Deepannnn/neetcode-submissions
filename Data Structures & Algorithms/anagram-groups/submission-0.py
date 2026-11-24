class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)

        for words in strs:
            key=tuple(sorted(words))
            anagram_map[key].append(words)
        return list(anagram_map.values())    