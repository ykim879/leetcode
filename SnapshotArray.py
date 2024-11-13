from sortedcontainers import SortedDict
class SnapshotArray:
    def __init__(self, length: int):
        self.snaps = 0
        self.history = [SortedDict(int) for _ in range(length)] # index = index of array # value = dictionary where key = snapId and value = value of that time
    def set(self, index: int, val: int) -> None:
        self.history[index][self.snaps] = val
    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1
    def get(self, index: int, snap_id: int) -> int:
        history = self.history[index]
        snap_id = history.bisect_right(snap_id) - 1
        return history.values()[snap_id] if snap_id >= 0 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
