class SnapshotArray(object):

    def __init__(self, length):
        self.nums = {}
        self.snaps = []   

    def set(self, index, val):
        self.nums[index] = val

    def snap(self):
        self.snaps.append(self.nums.copy())
        return len(self.snaps) - 1

    def get(self, index, snap_id):
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)