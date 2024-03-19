#线段树
class RangeModule:

    def __init__(self):
        self.tree = defaultdict(int)

    def pushdown(self, idx: int):
        if self.tree[idx]:
            self.tree[idx << 1] = self.tree[idx]
            self.tree[idx << 1 | 1] = self.tree[idx]

    def update(self, vl: int, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree[idx] = vl
        else:
            mid = (l + r) >> 1
            self.pushdown(idx)
            self.update(vl, start, end, l, mid, idx << 1)
            self.update(vl, start, end, mid + 1, r, idx << 1 | 1)
            self.tree[idx] = self.tree[idx << 1] & self.tree[idx << 1 | 1]

    def query(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return True
        if start <= l and r <= end:
            return self.tree[idx] == 1
        else:
            mid = (l + r) >> 1
            self.pushdown(idx)
            return self.query(start, end, l, mid, idx << 1) and self.query(start, end, mid + 1, r, idx << 1 | 1)

    def addRange(self, left: int, right: int) -> None:
        self.update(1, left, right - 1, 1, 10 ** 9, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.query(left, right - 1, 1, 10 ** 9, 1)

    def removeRange(self, left: int, right: int) -> None:
        self.update(2, left, right - 1, 1, 10 ** 9, 1)


# 715. Range 模块.py