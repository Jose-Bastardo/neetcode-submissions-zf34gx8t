class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortednums = sorted(nums)
        count = [[1, sortednums[0]]]
        output = []
        j = 0
        for i in range(1, len(sortednums)):
            if sortednums[i] == sortednums[i-1]:
                count[j][0] += 1
            else:
                j += 1
                count.append([1, sortednums[i]])

        sortedcount = sorted(count)

        index = len(sortedcount) - 1
        while k > 0:
            output.append(sortedcount[index][1])
            k -= 1
            index -= 1

        return output