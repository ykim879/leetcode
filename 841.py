class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = [0]
        visited = set()
        l = len(rooms)
        while q and len(visited) < l:
            c = q.pop()
            if c in visited:
                continue
            visited.add(c)
            q.extend(rooms[c])
        return len(visited) >= l
