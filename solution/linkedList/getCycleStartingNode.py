# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        return None


class Solution2:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None: return None
        hare, turtle= head, head
        while hare != None:
            turtle = turtle.next
            hare = hare.next
            if hare == None: return None
            hare = hare.next
            if hare == turtle:
                turtle = head
                while turtle != hare:
                    hare = hare.next
                    turtle = turtle.next
                return hare
        return None

class Solution3:
    def detectCycle(self, head):
        p = head
        ht = dict()
        while p:
            if id(p) in ht:
                return True
            else ht[id(p)] = True
            p = p.next
        return False

