class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height))
            events.append((right, height))
        events.sort()
        result = []
        live_buildings = [0]
        past_buildings = {}
        prev_max_height = 0
        for x, h in events:
            if h < 0:
                heapq.heappush(live_buildings, h)
            else:
                val_to_remove = -h
                past_buildings[val_to_remove] = past_buildings.get(val_to_remove, 0) + 1
            while live_buildings[0] in past_buildings:
                top = live_buildings[0]
                heapq.heappop(live_buildings)
                past_buildings[top] -= 1
                if past_buildings[top] == 0:
                    del past_buildings[top]
            curr_max_height = -live_buildings[0]
            if curr_max_height != prev_max_height:
                result.append([x, curr_max_height])
                prev_max_height = curr_max_height
        return result