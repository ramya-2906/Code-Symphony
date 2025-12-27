import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        room_cnt = [0] * n

        available = [i for i in range(n)]
        rented = []

        meetings.sort()

        for start,end in meetings:

            while rented and rented[0][0] <= start:
                already_used_room = heapq.heappop(rented)[1]
                heapq.heappush(available,already_used_room)
            
            if available:
                selected_room = heapq.heappop(available)
                heapq.heappush(rented,(end,selected_room))
                room_cnt[selected_room] += 1
            else:
                end_time,freed_room = heapq.heappop(rented)
                heapq.heappush(rented,(end_time+end-start,freed_room))
                room_cnt[freed_room] += 1

        return room_cnt.index(max(room_cnt))