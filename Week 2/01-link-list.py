# a link list may have multiple nodes
#first node
class Node: 
    #when we call Node class and pass values to it (store as state which functions dont)
    #takes self and next arg that needs to be pass to it 
    def __init__(self,value):
        self.value = value
        self.next = None #pointer to next node?

#head and null value to tell when the linklist is at the start or end
class Linkedlist:
    def __init__(self,head=None):
        self.head = head
        #creation of new node for linklist
        def append(self, new_node):
            current = self.head
            #if current has node header (means its not a single node)
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                #if current empty. we create a new node
                self.head = new_node

        #self.head = head 
       # def insert(self , new_node):







