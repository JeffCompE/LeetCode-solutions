from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # find walls of pit
        # scan from left to right
        walls = set()
        max_h = 0
        for i, h in enumerate(height):
            if h > max_h:
                max_h = h
                walls.add(i)
        # scan from right to left
        max_h = 0
        i = len(height) - 1
        while i >= 0:
            h = height[i]
            if h > max_h:
                max_h = h
                walls.add(i)
            i -= 1
        walls = sorted(walls)

        water = 0
        for i in range(len(walls) - 1):
            l = walls[i]
            r = walls[i + 1]
            h = min(height[l], height[r])
            pit_water = h * (r - l - 1)
            for j in range(l + 1, r):
                pit_water -= height[j]
            water += pit_water
        return water
