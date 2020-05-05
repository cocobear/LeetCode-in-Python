#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#
        
from __future__ import annotations
from typing import List
# @lc code=start
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans_dict = {}
        pre_char = S[0]
        res = []
        for i in range(1, len(S)):
            if S[i] == pre_char:
                if S[i] in ans_dict:
                    ans_dict[S[i]].append(i)
                else:
                    ans_dict[S[i]] = [i-1, i]
            else:
                if ans_dict and len(ans_dict[pre_char]) >= 3:
                    res.append([ans_dict[pre_char][0], ans_dict[pre_char][-1]])
                ans_dict.clear()
                pre_char = S[i]
        # print(ans_dict)

        if ans_dict and len(ans_dict[pre_char]) >= 3:
            res.append([ans_dict[pre_char][0], ans_dict[pre_char][-1]])
        return res

    tests = [
        ("abcdddeeeeaabbbcd", [[3,5],[6,9],[12,14]]),
        ('aaa',[[0,2]]),
        ('abc', []),
        ("abbabaabba", [])
    ]


# @lc code=end

