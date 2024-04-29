class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Creating Nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connecting nodes to form a linkedlist

node1.next=node2
node2.next=node3
node3.next=node4

# print the linkedlist

current = node1
while current is not None:
    print(current.data,end="-->")
    current = current.next
print("None")