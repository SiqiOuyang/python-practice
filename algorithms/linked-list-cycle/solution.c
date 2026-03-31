class ListNode:
    def_init_(self,x):
        self.val=x
        self.next=None
def hasCycle(head):
    slow=fast=head
    while fast and fast.next 
         slow=slow.next
         fast=fast.next.next.next
         if slow=fast:
              return True
    return False
