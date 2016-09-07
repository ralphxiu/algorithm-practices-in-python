# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self, node):
        self.head = node
        self.tail = self.head

    def add(self, node):
        self.tail.next = node
        self.tail = self.tail.next

    def reverseList(self):
        revHead = ListNode(-1)
        self.reverseListHelper(self.head, revHead)
        self.head = revHead.next

    def prettyPrint(self):
        arr = []
        curr = self.head
        arr.append(curr.val)
        while curr.next:
            curr = curr.next
            arr.append(curr.val)
        return '-'.join(map(str, arr))

    def reverseListHelper(self, curr, revHead):
        if curr.next:
            revTail = self.reverseListHelper(curr.next, revHead)
            revTail.next = curr
            curr.next = None
        else:
            revHead.next = curr
        return curr

if __name__ == "__main__":
    ls = LinkedList(ListNode(1))
    ls.add(ListNode(2))
    ls.add(ListNode(3))
    ls.add(ListNode(4))
    ls.add(ListNode(5))
    print(ls.prettyPrint())
    ls.reverseList()
    print(ls.prettyPrint())