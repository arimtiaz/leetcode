# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        new_list = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = new_list
            new_list = curr
            curr = next_node
        return new_list