# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        new_list = None

        while head:

            next_node = head.next 
            # Step 1: next_node save link on "2"
            # Step 2: next_node save link on "3"
            # Step 3: next_node save link on "4"
            # Step 4: next_node save link on "5
            # Step 5: next_node save link on "None"


            head.next = new_list
            # Step 1: None <- 1 -> 2 -> 3 -> 4 -> 5-> None
            # Step 2: None <- 1 <- 2 -> 3 -> 4 -> 5-> None
            # Step 3: None <- 1 <- 2 <- 3 -> 4 -> 5-> None
            # Step 4: None <- 1 <- 2 <- 3 <- 4 -> 5-> None
            # Step 5: None <- 1 <- 2 <- 3 <- 4 <- 5

            new_list = head 
            # Step 1: new_list save link on "1"
            # Step 2: new_list save link on "2"
            # Step 3: new_list save link on "3"
            # Step 4: new_list save link on "4"
            # Step 5: new_list save link on "5" -> finish

            head = next_node 
        
        return new_list