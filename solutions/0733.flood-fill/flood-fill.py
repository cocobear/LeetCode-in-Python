#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
from __future__ import annotations
# @lc code=start
from queue import Queue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        if not image:
            return []
        n = len(image)
        m = len(image[0])
        start_color = image[sr][sc]
        def can_access(x, y):

            if x < 0 or x >= n or y < 0 or y >= m:
                return False
            if image[x][y] == start_color:
                return True
            else:
                return False
        q = Queue()
        q.put((sr, sc))
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while not q.empty():
            x, y = q.get()
            image[x][y] = newColor
            for dx, dy in direction:
                new_x = x + dx
                new_y = y + dy
                # print('dfs: x y ', new_x , new_y)
                if can_access(new_x, new_y):
                    q.put((new_x, new_y))

        return image

    tests = [
        ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[1,1,1],[1,1,0],[1,0,1]])
    ]

# @lc code=end

