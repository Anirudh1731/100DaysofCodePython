# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        head2=dummy

        

        temp1=l1
        temp2=l2
        carry=0
        while temp1 or temp2 or carry:
            v1=temp1.val if temp1 else 0
            v2=temp2.val if temp2 else 0
            sum=v1+v2+carry
            s=sum%10
            sum=sum//10
            carry=sum%10
                
            head2.next=ListNode(s)
            head2=head2.next
            temp1=temp1.next if temp1 else None
            temp2=temp2.next if temp2 else None
           

        return dummy.next

            


                

        
