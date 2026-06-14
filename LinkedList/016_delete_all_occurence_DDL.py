# https://www.naukri.com/code360/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461?leftPanelTabValue=PROBLEM
## TC: O(n) : number of nodes in LL SC:O(1)prev, cur storing 
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
        cur = head
        prev = None
        while cur:
            if cur.data ==k:
                if not prev and not cur.next:
                    return None
                elif not prev:
                    head = cur.next
                    cur = cur.next
                    cur.prev = None
                    continue
                elif not cur.next:
                    prev.next = None
                else:
                    prev.next = cur.next
                    cur = cur.next
                    cur.prev = prev
                    continue
            prev = cur
            cur = cur.next
        return head
