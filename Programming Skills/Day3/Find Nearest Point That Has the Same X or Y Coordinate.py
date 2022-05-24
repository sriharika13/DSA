# Leetcode 1779.Find Nearest Point That Has the Same X or Y Coordinate

'''You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).'''


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhattan_dist=[100000,-1] #0th index is min dis, 1st index is index of point of points list
        for i, p in enumerate(points):
            if p[0]==x or p[1]==y:
                curr=abs( p[0] - x ) + abs( p[1] - y )
                if curr<manhattan_dist[0]:
                    manhattan_dist[0]=curr
                    manhattan_dist[1]=i
        return manhattan_dist[1]
    
#     time: O(n), space:O(1)
