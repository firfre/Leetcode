class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 is not None or l2 is not None:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val

            result_tail = ListNode((x + y) % 10 + carry)
            carry = (x + y) // 10
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            result_tail = result_tail.next

        return result


x1 = ListNode(3)
x1.next = ListNode(0)
x1.next.next = ListNode(7)

x2 = ListNode(8)
x2.next = ListNode(2)
x2.next.next = ListNode(4)
aSolution = Solution()
res = aSolution.addTwoNumbers(x1, x2)

print(res.next.val)
# while res is not None:
#     print(res.val)
#     res = res.next
