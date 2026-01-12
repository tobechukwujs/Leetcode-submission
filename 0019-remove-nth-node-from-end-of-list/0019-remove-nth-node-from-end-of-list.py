class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for i in range (n+1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next                 


        
        