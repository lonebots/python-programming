class Node :
    def __init__(self, dataval) -> None:
        self.val = dataval
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.headval = None
    
    def print_list (self) :
        print_val = self.headval
        while print_val is not None :
            print(print_val.val)
            print_val = print_val.next

    def reverse_list(self) :
        if self.headval is not None :
            previous = None
            current = self.headval
            while current is not None :
                next = current.next
                current.next = previous
                previous = current
                current = next 
            self.headval = previous
        else :
            print('empty linked list')


if __name__ == '__main__' :
    ll = LinkedList() # created empty 
    e1 = Node(10)
    e2 = Node(20)
    e3 = Node(30)

    ll.headval = e1
    e1.next = e2
    e2.next = e3

ll.print_list()
ll.reverse_list()
ll.print_list()

