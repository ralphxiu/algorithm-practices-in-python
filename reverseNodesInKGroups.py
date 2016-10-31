# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from reverseLinkedList import ListNode, LinkedList


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dumHead = ListNode(0)
        dumHead.next = head
        curr = dumHead
        counter = 0
        while counter < k:
            if curr.next:
                curr = curr.next
                counter += 1
            else:
                break
        if counter == k: #i.e. there are at least k nodes remaining in the list
            nextNode = curr.next
            curr.next = None
            # dummy head for retriving the reversed list partial
            rvsTail = self.reverseInGroupHelper(dumHead.next, dumHead)
            rvsTail.next = self.reverseKGroup(nextNode, k)
        return dumHead.next

    def reverseInGroupHelper(self, curr, dumHead):
        if curr.next:
            rvsTail = self.reverseInGroupHelper(curr.next, dumHead)
            rvsTail.next = curr
            curr.next = None
        else:
            dumHead.next = curr
        return curr

if __name__ == "__main__":
    ls = LinkedList(ListNode(1))
    ls.add(ListNode(2))
    ls.add(ListNode(3))
    ls.add(ListNode(4))
    ls.add(ListNode(5))
    print(ls.prettyPrint())
    #ls.reverseList()
    #print(ls.prettyPrint())
    s = Solution()
    head = s.reverseKGroup(ls.head, 2)
    ls.head = head
    print(ls.prettyPrint())