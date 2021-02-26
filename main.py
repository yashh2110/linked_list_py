class Node:
    def __init__(self,data=None):
        self.data =data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = Node()
    def append(self,data):
        cur = self.head
        new_node = Node(data)
        while cur.next!=None:
            cur = cur.next
        cur.next=new_node
    def length(self):
        cur = self.head
        count =0
        while cur.next!=None:
            count+=1
            cur=cur.next
        return count
    def dispaly(self):
        cur = self.head
        arr= []
        while cur.next!=None:
            cur=cur.next
            arr.append(cur.data)
        return print(arr)
    def get(self,index):
        if index>=self.length():
            return print("exded length");
        cur = self.head
        pos=0
        while True:
            cur=cur.next
            if pos == index:
                return print(cur.data)
            pos += 1

    def delete(self,index):
        if index >= self.length():
            return print("exeded length")
        cur = self.head
        pos=0
        while True:
            last = cur
            cur = cur.next
            if pos == index:
                last.next=cur.next
                return
            pos += 1


my = Linked_list()
my.append(10)
my.append(17)
my.append(5)
my.append(4)
my.append(2)
my.dispaly()
my.get(5)
