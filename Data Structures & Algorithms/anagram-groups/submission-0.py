class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        reviewed = []
        for i in range(len(strs)):
            if strs[i] in reviewed:
                continue

            anagrams = [strs[i]]
            sorteds1 = sorted(strs[i])
            reviewed.append(strs[i])
            for j in range(i+1, len(strs)):
                if sorteds1 == sorted(strs[j]):
                    anagrams.append(strs[j])
                    reviewed.append(strs[j])

            output.append(anagrams)

        return output
