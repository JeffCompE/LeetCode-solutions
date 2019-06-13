import heapq
# Note: python bisect.insort(list, val) is O(n), not recommend here

class Solution:
    # Running time: O(n * log (n))
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = list()
        for i in range(len(quality)):
            workers.append((quality[i], wage[i] / quality[i]))
        workers = sorted(workers, key=lambda x: x[1])

        avalible_workers = list()
        units = 0
        ref_worker = workers[K - 1]
        for i in range(K - 1):
            units += workers[i][0]
            heapq.heappush(avalible_workers, -1 * workers[i][0])
        min_price = (units + ref_worker[0]) * ref_worker[1]

        for i in range(K, len(quality)):
            ref_worker = workers[i]
            units += workers[i - 1][0]
            heapq.heappush(avalible_workers, -1 * workers[i - 1][0])
            units += heapq.heappop(avalible_workers)
            price = (units + ref_worker[0]) * ref_worker[1]
            if price < min_price:
                min_price = price

        return min_price
        
