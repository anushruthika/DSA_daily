# 142. Linked List Cycle II
## TC: O(n) SC: O(1)

####### IMPORTAnT
# From meeting point: if one pointer moves toward cycle start and another starts from head both travel same distance. HOW??????
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwi-gYC8rfmUAxWM0KACHfN1My0QtwJ6BAgTEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D2Kd0KKmmHFc&usg=AOvVaw3JR6d-YNuTwlTfL4wS05oz&opi=89978449
########################################################



class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow!=head:
                    slow = slow.next
                    head = head.next
                return slow
