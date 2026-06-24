import base


def create_cycle(lst):
    if len(lst) <= 1:
        raise RuntimeError(f"Inadequate List. List size is {len(lst)}.")

    pos = base.random.randrange(0, len(lst)-1)
    # pos = 3

    walker = lst.head
    for _ in range(pos):
        walker = walker.next

    lst.tail.next = walker
    return walker



def cycle(lst):
    if len(lst) == 0:
        return False
    
    turtle = lst.head
    hare = lst.head

    while hare and hare.next:
        hare = hare.next.next
        turtle = turtle.next

        if hare == turtle:
            return True
        
    return False

def start_cycle(lst):
    if len(lst) == 0:
        raise RuntimeError("List Empty.")

    turtle = lst.head
    hare = lst.head

    while hare and hare.next:
        hare = hare.next.next
        turtle = turtle.next

        if turtle == hare:
            break

    hare = lst.head
    while hare != turtle:
        turtle = turtle.next
        hare = hare.next

    return hare
    


if __name__ == "__main__":
    test_cases = 0
    while test_cases <= base.random.randrange(5000, 10000):
        arr = [base.random.randint(0, 100) for _ in range(base.random.randint(0, base.random.randrange(20, 200)))]

        lst = base.SLL()


        for num in arr:
            lst.append(num)

        print(lst)

        # print(start.data())
        try:
            start = create_cycle(lst)
            print(start.data)
        except RuntimeError as e:
            print(e)

        print(cycle(lst))
        try:
            print(start_cycle(lst).data)
        except RuntimeError as e:
            print(e)


        test_cases += 1

    print("Total cases run: ", test_cases)
