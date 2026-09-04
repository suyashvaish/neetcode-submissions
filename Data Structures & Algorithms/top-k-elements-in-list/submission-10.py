class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count frequency
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Put numbers into bucket according to frequency
        for x, count in freq.items():
            buckets[count].append(x)

        # Get top k frequent elements
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for x in buckets[i]:
                result.append(x)

                if len(result) == k:
                    return result