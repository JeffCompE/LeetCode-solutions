class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in intervals[1:]:
            if merged[-1][1] >= i[0]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
        return merged
