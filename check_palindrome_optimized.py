import base


def print_list(start: base.Node) -> None:
    walker = start

    while walker:
        print(walker.data, end="->")
        walker = walker.next

    print("-1")

def reverse(lst: base.SLL) -> None:
    prev = None
    curr = lst.head
    next = None

    lst.tail = curr
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next


    lst.head = prev

def construct_palindrome(lst: base.SLL) -> None:
    if lst.head is None:
        raise RuntimeError("List Empty.")
    

    temp_lst = base.SLL()

    walker = lst.head

    while walker:
        temp_lst.append(walker.data)
        walker = walker.next

    reverse(temp_lst)

    lst.tail.next = temp_lst.head
    lst.tail = temp_lst.tail

    # We don't need temp_lst now
    temp_lst.head = None
    temp_lst.tail = None





def mid(start: base.Node) -> base.Node:
    if start is None or start.next is None:
        return start
    
    turtle = start
    hare = start


    while hare.next and hare.next.next:
        turtle = turtle.next
        hare = hare.next.next

    
    return turtle




def rev(start: base.Node) -> base.Node:
    if start is None or start.next is None:
        return start
    
    prev = None
    curr = start
    next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev





def check_palindrome(start: base.Node) -> bool:
    if start is None or start.next is None:
        return True
    
    middle = mid(start)
    print(middle.data)
    print(middle.next.data)

    sec_half = middle.next
    


    middle.next = None

    reversed_head = rev(sec_half)
    print("Reversed Second Half: ", end="")
    print_list(reversed_head)

    
    left = start
    right = reversed_head



    # print("Left: ", left.data)
    # print("Right: ", right.data)

    # print("Left List: ", end="")
    # print_list(left)
    # print("Right List: ", end="")
    # print_list(right)


    while right:
        if left.data != right.data:
            return False
        
        left = left.next
        right = right.next


    return True







if __name__ == "__main__":
    test_cases = 0
    while test_cases <= 0:
        arr: list[int] = [base.random.randrange(0, 101) for _ in range(5, 15)]

        lst: base.SLL = base.SLL()

        for num in arr:
            lst.append(num)


        print(lst)
        print_list(lst.head)

        

        construct_palindrome(lst)
        print(lst)

        print("Checking Palindrome")
        print(check_palindrome(lst.head))
        print(lst)
        
        test_cases += 1

    print(test_cases)

    # 1 2 3 - 3 2 1