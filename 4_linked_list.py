# Topics > 
    # 1. issues with arrays that linked list solves
    # 2. doubly linked list
    # 3. big O analysis(array vs linked list)
    # 4. python implementation
    # 5. exercise

# array insertion => O(n) and allocating new memory and copying elements from one location to another
# linked list insertion=> beginning-O(1), end-O(n)
# linked list deletion=> beginning-O(1), end-O(n)

# Linked list has two main benifits over an array:
    # 1. you don't need to preallocate space
    # 2. insertion is easier

# linked list traversal => O(n)
# accessing element by value => O(n)

# Big-O analysis
'''
                                Array           Linked list
                                -----           ------------
Indexing                        O(1)            O(n)
Insert/delete element at start  O(n)            O(1)
Insert/delete element at end    O(n)-amortized  O(n)
Insert element in middle        O(n)            O(n)
'''

# protoyype of nodes
class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

# prototype of linked list
class LinkedList:
    def __init__(self):
        self.head=None

    # inserting element at the beginning
    def insert_at_beginning(self, data):
        node=Node(data, self.head)
        self.head=node

    # inserting element at the end
    def insert_at_end(self, data):
        if self.head == None:
            self.head=Node(data, None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)

    # inserting element at a particular index
    def insert_at(self, index, data):
        if index>self.get_length():
            raise Exception("Invalid index")
            return
        elif index==0:
            self.insert_at_beginning(data)
            return
        elif index==self.get_length():
            self.insert_at_end(data)
        else:
            count=0
            itr=self.head
            while itr:
                if count==index-1:
                    node=Node(data, itr.next)
                    itr.next=node
                    break
                itr=itr.next
                count=count+1

    # inserting data after a particular value
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        itr=self.head
        while itr and itr.data!=data_after:
            itr=itr.next
        # Now insert data_to_insert after data_after node
        if itr == None:
            raise Exception("Invalid data")
        node=Node(data_to_insert, itr.next)
        itr.next=node

    # inserting data after a particular value
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count=count+1

    # removing element by value
    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            raise Exception("empty list")
        elif self.head.data==data:
            self.head=self.head.next
        else:
            itr=self.head
            while itr.next:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    return
                itr = itr.next

            if itr.next is None:
                raise Exception("invalid value")


    # creating a new linked list with a few values
    def insert_values(self, data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        while itr:
            print(itr.data, end=" ")
            itr=itr.next
        print()

    # checking the length of the linked list
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count=count+1
            itr=itr.next
        # print("length of the list is", count)
        return count

if __name__=="__main__":
    # ll1=LinkedList()
    # ll1.insert_at_beginning(10)
    # ll1.insert_at_beginning(20)
    # ll1.insert_at_beginning(30)
    # ll1.insert_at_end(70)
    # ll1.print()
    # ll1.get_length()

    data_list=["arunabha", "samrat", "kittu", "kushal", "babai"]
    ll2=LinkedList()
    ll2.insert_values(data_list)
    ll2.print()
    # ll2.remove_at(2)
    # ll2.insert_at(4, "mandal")
    # ll2.insert_after_value("sam", "aru")
    ll2.remove_by_value("baba")
    # ll2.insert_at_end("mjfnsjfsnejks")
    ll2.print()
    # ll2.get_length()

    # ll1.insert_at_beginning(200)
    # ll1.print()


# exercise due