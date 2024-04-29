class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating Nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connecting nodes to form a linkedlist
head.next = node2
node2.next = node3
node3.next = node4

# Deleting the particular node
current = head
while current.next is not None and current.next.data != 30:
    current = current.next

if current.next is None:
    print("Node not found")
else:
    current.next = current.next.next

# Printing the linked list to verify deletion
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
