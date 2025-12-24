class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)


        out = []

        for num in nums:
            res[num] += 1
            
        for num, freq in sorted(res.items(), key=lambda x: x[1], reverse=True):
            out.append(num)
            if len(out) == k:
                break

        return out