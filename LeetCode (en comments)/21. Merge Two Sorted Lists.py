class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        merge_head = head
        while list1 and list2:
            if list1.val <= list2.val:
                merge_head.next = list1
                list1 = list1.next
            else:
                merge_head.next = list2
                list2 = list2.next
            merge_head = merge_head.next
        merge_head.next = list1 or list2
        return head.next