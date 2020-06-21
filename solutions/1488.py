from __future__ import annotations
import collections
import heapq
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # 保存每个湖下雨的日期
        rain_dict = collections.defaultdict(list)
        # 返回结果 默认值有用吗？
        ret = [-1] * len(rains)
        
        for day, lake in enumerate(rains):
            rain_dict[lake].append(day)
            
        # 使用set 保存已经满了的湖 因为如果重复了就失败了
        full_lakes = set()
        # 保存需要抽水日期
        to_empty = []
        
        for day, lake in enumerate(rains):
            # 如果没下雨就去抽水
            if lake == 0:
                # 没有需要抽水的 
                if not to_empty:
                    ret[day] = 1
                else:
                    closest_day = heapq.heappop(to_empty)
                    full_lakes.remove(rains[closest_day])
                    ret[day] = rains[closest_day]
            # 下雨了
            else:
                # 如果这个湖已经满了则失败
                if lake in full_lakes:
                    return []
                full_lakes.add(lake)
                rain_days = rain_dict[lake]
                rain_days.pop(0)
                if rain_days:
                    heapq.heappush(to_empty, rain_days[0])
                    
        return ret