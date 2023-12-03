# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first_run = head
        for _ in range(1,k):
            first_run = first_run.next

        second_run = head
        curr = first_run
        while curr.next:  # symmetrical displacement
            curr = curr.next
            second_run = second_run.next

        first_run.val, second_run.val = second_run.val, first_run.val
        return head