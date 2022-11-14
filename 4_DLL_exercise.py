# Implement doubly linked list

# prototype of nodes
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next

# prototype of doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    # insert at the beginning
    def insert_at_beginning(self, data):
        if self.head == None:
            node=Node(data, None, self.head)
            self.head=node
        else:
            node=Node(data, None, self.head)
            self.head.prev=node
            self.head=node

    # insert at the end
    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_beginning(data)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data, itr, None)

    # insert at a particular index
    def insert_at(self, data, index):
        if self.head==None:
            self.insert_at_beginning(data)
        else:
            count=0
            itr=self.head
            while itr:
                if count==index-1:
                    node=Node(data, itr, itr.next)
                    if itr.next!=None:
                        itr.next.prev=node
                    itr.next=node
                itr=itr.next
                count=count+1

    # inserting data after a particular value
    def insert_after_value(self, data_after, data_insert):
        if self.head==None:
            raise Exception("Empty list")
        else:
            itr=self.head
            while itr!=None and itr.data!=data_after:
                itr=itr.next

            if itr==None:
                raise Exception("Invalid data")
            else:
                node=Node(data_insert, itr, itr.next)
                if itr.next!=None:
                    itr.next.prev=node
                itr.next=node

    # remove from the beginning
    def remove_from_beginning(self):
        if self.head==None:
            raise Exception("empty list")
        else:
            self.head=self.head.next
            if self.head!=None:
                self.head.prev=None

    # remove from the end
    def remove_from_end(self):
        if self.head==None:
            raise Exception("empty list")
        else:
            itr=self.get_last_node()
            if self.head.next==None:
                self.head=None
            else:
                itr.prev.next=None

    # remove at
    def remove_at(self, index):
        if index<0:
            raise Exception("negative index")
        if self.head==None:
            raise Exception("empty list")
        else:
            count=0
            itr=self.head
            while itr:
                if index==count:
                    if itr==self.head:
                        self.remove_from_beginning()
                        return
                    elif itr.next==None:
                        self.remove_from_end()
                        return
                    else:
                        itr.prev.next=itr.next
                        itr.next.prev=itr.prev
                        itr.next=None
                        itr.prev=None
                        return
                
                count=count+1
                itr=itr.next
            
            if itr==None:
                raise Exception("invalid index")


    # removing element by value
    def remove_by_value(self, value):
        if self.head==None:
            raise Exception("Empty list")
        elif self.head.data==value:
            self.head=self.head.next
            self.head.prev=None
        else:
            itr=self.head
            while itr:
                if itr.data == value:
                    if itr.next:
                        itr.next.prev=itr.prev
                    itr.prev.next=itr.next
                    itr=None
                    return
                itr=itr.next
            if itr == None:
                raise Exception("invalid value")


    # creating a new linked list with a few values
    def insert_values(self, data_list):
        self.head=None # previously created list will also be NULL
        for data in data_list:
            self.insert_at_end(data)

    # checking the length of the linked list
    def get_length(self):
        count = 0
        itr=self.head
        while itr:
            count=count+1
            itr=itr.next

    # finding last node
    def get_last_node(self):
        itr=self.head
        if itr==None:
            return None
        while itr.next:
            itr=itr.next
        return itr

    # print linked list in forward direction
    def print_forward(self):
        if self.head == None:
            print("Linked list is empty.")
            return
        else:
            itr=self.head
            while itr:
                print(itr.data, end=" ")
                itr=itr.next
            print()
            

    # print linked list in backward direction
    def print_backward(self):
        itr=self.get_last_node()
        if itr==None:
            print("Linked list is empty.")
        while itr:
            print(itr.data, end=" ")
            itr=itr.prev
        


# main function
if __name__=="__main__":
    # dll1=DoublyLinkedList()
    # dll1.insert_at_beginning(1)
    # dll1.insert_at_beginning(2)
    # dll1.insert_at_beginning(3)
    # dll1.print_forward()
    # dll1.print_backward()

    dll2=DoublyLinkedList()
    dll2.insert_values([10,20,30,40,50,60,70,80])
    # dll2.insert_after_value(70,86)
    # dll2.remove_by_value(50)
    # dll2.remove_from_beginning()
    # dll2.remove_from_end()
    # dll2.remove_from_end()
    # dll2.remove_at(8)
    dll2.print_forward()
    dll2.print_backward()