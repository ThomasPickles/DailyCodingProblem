address_map = dict()

class Node:
    
    def __init__(self, data: str):
        # implement using "pointers" to memory
        self.address = id(data)
        self.prev = 0
        self.next = 0
        address_map[self.address] = data

    def __repr__(self):
        return self.address
    
    def append_to_end(self, data) -> None:
        tail = Node(data)
        n = self
        while n.next != 0:
            n = n.next
        n.next = tail.address
        tail.prev = n.address
    
    def delete(self, address: int):
        n = self
        if address == n.address: # delete head
            if n.next: # if it's got more nodes
                n = n.next
                n.prev = None
                return self
            return None
        while n.next:
            if n.next == address:
                n.next = n.next.next
                n.next.next.prev = n
                return self
            n = n.next
        return None
            
            

    def get(self, targetIndex):
        index = 0
        node = self
        while index < targetIndex:
            node = node.next
            index = index + 1
        return node

n = Node("this") # 0
n.append_to_end("is") #1
# n.delete(n)
n.append_to_end("a") #2
n.append_to_end("sentence") #3
# print(n.get(2).data)


def dereference_pointer(id: int) -> str:
    return address_map[id]
#    return ctypes.cast(id, ctypes.py_object).value



