1class Solution:
2    def maxTwoEvents(self, events: List[List[int]]) -> int:
3        events.sort(key=lambda x: x[1])
4        first_event_end = [0]
5        first_event_val = [0] # Best up to corresponding end time
6        max_seen = 0
7        for start, end, val in events:
8            max_seen = max(max_seen, val)
9            first_event_end.append(end)
10            first_event_val.append(max_seen)
11
12        events.sort(key=lambda x: x[0])
13        cur = 0
14        ans = 0
15
16        for start, end, val in events:
17            while first_event_end[cur + 1] < start:
18                cur += 1
19            ans = max(ans, val + first_event_val[cur])
20
21        return ans