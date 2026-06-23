import random
from typing import Optional


class Node:
    def __init__(self, value: int):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.next = None
        self._size = 0

    def __str__(self) -> str:
        curr = self.head
        values:list[int] = []

        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next

        return "->".join(values)
    
    def __len__(self):
        return self._size
    
    def append(self, value:int):
        new_node = Node(value)

        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        
        self._size += 1




def merge(lst1:Optional[SLL], lst2:Optional[SLL]) -> Optional[SLL]:
    head1 = lst1.head
    head2 = lst2.head

    dummy = Node(-1)
    tail = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            new_node = Node(head1.data)
            tail.next = new_node
            head1 = head1.next
        else:
            new_node = Node(head2.data)
            tail.next = new_node
            head2 = head2.next
        tail = tail.next

    while head1:
        new_node = Node(head1.data)
        tail.next = new_node
        tail = tail.next
        head1 = head1.next

    
    while head2:
        new_node = Node(head2.data)
        tail.next = new_node
        tail = tail.next
        head2 = head2.next

    merged = SLL()
    merged.head = dummy.next

    return merged


def get_size(lst:Optional[SLL]) -> Optional[SLL]:
    walker = lst.head

    n = 0

    while walker:
        n += 1
        walker = walker.next

    return n




if __name__ == "__main__":
    arr1 = [random.randrange(0, 101) for _ in range(random.randrange(5, 21))]
    arr2 = [random.randrange(0, 101) for _ in range(random.randrange(5, 21))]

    lst1 = SLL()
    lst2 = SLL()

    for num in arr1:
        lst1.append(num)

    for num in arr2:
        lst2.append(num)

    print("List1: ", lst1)
    print("List2: ", lst2)

    lst = merge(lst1, lst2)
    print("Merged List: ", lst)

    print("Size of list1: ", len(lst1))
    print("Size of list2: ", len(lst2))
    print("Size of merged list: ", get_size(lst))