class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        
        head = l1
        val = 0
        while(l1 and l2):
            new  = val + l1.val + l2.val
            l1.val = new%10
            val =  new//10
            if l1.next == None:
                pre = l1
            l1 = l1.next
            l2 = l2.next
            
        if l1 is None and l2 is None:
            if val:
                pre.next = ListNode(val)
            return head
        
        elif l1 is None:
            if l2 is not None:
                pre.next = l2
                while(l2):
                    new = l2.val  + val
                    l2.val = new%10
                    val = new//10
                    if l2.next == None and val:
                        l2.next = ListNode(val)
                        l2 = l2.next
                    l2 = l2.next
            else:
                if val:
                    pre.next = ListNode(val) 
        else:
            while(l1):
                new = l1.val  + val
                l1.val = new%10
                val = new//10
                if l1.next == None and val:
                    l1.next = ListNode(val)
                    l1 = l1.next
                l1 = l1.next
                
        return head
        
'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
'''
