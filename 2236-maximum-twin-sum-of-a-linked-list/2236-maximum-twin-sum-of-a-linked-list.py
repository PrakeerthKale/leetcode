class Solution:
    def pairSum(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        max_sum = 0
        left, right = 0, len(values) - 1
        while left < right:
            twin_sum = values[left] + values[right]
            max_sum = max(max_sum, twin_sum)
            left += 1
            right -= 1
        
        return max_sum
