class Node:
    def __init__(self, data, nxt): 
        self.data = data
        self.nxt = nxt

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return

        itr = self.head
        while itr.nxt:
            itr = itr.nxt
        
        itr.nxt = Node(data,None)

    def print(self):
        if self.head is None:
            print("Linked List is empty")
        llstr = ''
        itr = self.head

        while itr:
            llstr += str(itr.data)+"-->"
            itr = itr.nxt
        
        print(llstr)

    def insert_values(self, datalist):
        self.head = None
        for i in datalist:
            self.insert_at_end(i)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.nxt
        return count

    def remove_at(self,pos):
        if pos<0 or pos>self.get_length():
            raise Exception("Invalid Exception")

        if pos == 0: 
            self.head = self.head.nxt
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == pos-1:
                itr.nxt = itr.nxt.nxt
                break
            itr = itr.nxt
            count+=1

    def insert_at(self,pos,data):
        if pos<0 or pos>self.get_length():
            raise Exception("Invalid Exception")

        if pos == 0: 
            self.insert_at_start(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == pos-1:
                node = Node(data,itr.nxt)
                itr.nxt = node
                break
            itr = itr.nxt
            count+=1
    
    def remove_by_value(self,data):
        itr = self.head
        while itr:
            if itr.nxt.data == data:
                itr.nxt = itr.nxt.nxt
                break
            else:
                return "Not Found"

            itr = itr.nxt
            
    def insert_after_value(self,val,data):
        itr = self.head
        while itr:
            if itr.data == val:
                node = Node(data,itr.nxt)
                itr.nxt = node
                break
            itr = itr.nxt        
if __name__ == '__main__':
    ll = Linkedlist()
    """ll.insert_at_start(44)
    ll.insert_at_start(90)
    ll.insert_at_end(111)
    ll.insert_values([1,2,3,4,5])
    ll.print()
    ll.get_length()
    ll.remove_at(2)
    ll.print()
    ll.insert_at(1,1000)
    ll.print()"""
    ll.insert_values([1,2,3,4,5])
    ll.print()
    ll.insert_after_value(2,10000)
    ll.print()