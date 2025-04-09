# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        count = 0
        while current_node != None:
            current_node = current_node.next
            count += 1
                               # this approach has time complexity O(n)
        middle_index = count//2
        middle_node = head
        for i in range(middle_index):
            middle_node = middle_node.next 
        return middle_node

        