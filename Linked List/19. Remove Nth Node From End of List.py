# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_count = -n
        fast = head
        slow = head
        if not head or not head.next:
            return None

        while fast:
            if fast.next == None:
                if slow_count < 0:
                    return head.next
                slow.next = slow.next.next
                return head
            if slow_count >= 0:
                slow = slow.next
            fast = fast.next
            slow_count += 1
