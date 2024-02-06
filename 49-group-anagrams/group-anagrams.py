class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for str in strs:
            sortedString = "".join(sorted(str))
            if sortedString in hash.keys():
              hash[sortedString].append(str)
            else:
                hash[sortedString] = [str]
        return hash.values()
