# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        
        if list1 == None:
            return  list2

        if list2 == None:
            return list1    

        head = ListNode()
        ll = ListNode()
        head = ll
        while((list1 != None) and (list2 != None)):
            if (list1.val <= list2.val):
                ll.val = list1.val 
                list1 = list1.next
            else:
                ll.val = list2.val
                list2 = list2.next
            
            if (list1 != None) and (list2 != None):
                ll_new = ListNode()
                ll.next = ll_new 
                ll = ll_new

        if list1 != None:
            ll.next = list1
        else:
            ll.next = list2        
        return head       


