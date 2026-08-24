# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # split the list in half using fast and slow pointer
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half
        l2 = slow.next
        slow.next = None
        second = self.reverseList(l2)

        first = head
        while second:
            temp1,temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first,second = temp1, temp2
        return 