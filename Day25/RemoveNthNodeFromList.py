# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp=head
        cnt=0
        while temp:
            cnt=cnt+1
            temp=temp.next
        print(cnt)
        dummy=ListNode()
        dummy.next=head
        temp1=dummy
        cnt2=0

        while(cnt2 != cnt-n and temp1.next.next):
            temp1=temp1.next
            cnt2=cnt2+1
        
        if(temp1.next):
            temp1.next=temp1.next.next
        else:
            temp1.next=None

        return dummy.next
        
        
        

        
