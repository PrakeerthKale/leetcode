
class SegmentTree:
    __slots__ = ("nums", "tree", "n")
    def __init__(self, nums):
        # store original basket capacities and prepare tree size
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)  # segment tree array
        self._build(1, 0, self.n - 1)
    def _build(self, idx, left, right):
        # build tree: leaf stores capacity, internal nodes store max of children
        if left == right:
            self.tree[idx] = self.nums[left]
            return
        mid = (left + right) // 2
        self._build(idx * 2, left, mid)
        self._build(idx * 2 + 1, mid + 1, right)
        self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])
    def query(self, idx, left, right, value):
        # find leftmost basket index with capacity >= value
        if self.tree[idx] < value:
            return -1
        if left == right:
            return left
        mid = (left + right) // 2
        # search left child first if it can satisfy
        if self.tree[idx * 2] >= value:
            return self.query(idx * 2, left, mid, value)
        return self.query(idx * 2 + 1, mid + 1, right, value)
    def modify(self, idx, left, right, pos, new_val):
        # set basket at pos to new_val (0 when used) and update tree
        if left == right:
            self.tree[idx] = new_val
            return
        mid = (left + right) // 2
        if pos <= mid:
            self.modify(idx * 2, left, mid, pos, new_val)
        else:
            self.modify(idx * 2 + 1, mid + 1, right, pos, new_val)
        self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # build segment tree over basket capacities
        st = SegmentTree(baskets)
        unplaced = 0
        for qty in fruits:
            # find first available basket with capacity >= qty
            i = st.query(1, 0, st.n - 1, qty)
            if i == -1:
                unplaced += 1  # no fitting basket
            else:
                st.modify(1, 0, st.n - 1, i, 0)  # mark basket used
        return unplaced
