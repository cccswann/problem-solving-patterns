
# To reverse a LinkedList, we need to reverse one node
# at a time. We will start with variable current which will
# initially point to the head of the linkedlist.

from __future__ import print_function

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
    
def reverse(head):
    prev, curr, next = None, head, None
    while curr is not None:
        next = curr.next # temporarily store the next node
        curr.next = prev # reverse the current node
        prev = curr # before we move to the next node, point previous to the current node
        curr = next # move on the next node
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()
