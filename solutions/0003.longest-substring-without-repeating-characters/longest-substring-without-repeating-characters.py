#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = ''
        tmp = ''
        if not s:
            return 0
        for i in s:
            if i in tmp:
                # print('find repeat:',i,tmp,subs)
                if len(tmp) >= len(subs):
                    subs = tmp
                    # 需要把重复字母之后的字符串作为新的开始
                idx = tmp.index(i)+1
                if idx > len(subs):
                    tmp = '' + i
                else:
                    tmp = tmp[idx:] + i

            else:
                tmp += i

        # print(subs,tmp)
        if len(subs) > len(tmp): return len(subs)
        else: return len(tmp)

    tests = [
            ('', 0),
            ('abcabcbb', 3),
            ('bbbbb', 1),
            ('ab', 2),
            ('aab', 2),
            ('dvdf', 3),
            ('anviaj', 5),
            ('jbpnbwwd', 4),
            ('hkcpmprxxxqw', 5)
            ]

# @lc code=end
# leetcode submit region end(Prohibit modification and deletion)
