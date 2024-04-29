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

# Deleting the node from end
if head is None:
    print("List is empty")
elif head.next is None:
    # If there's only one node in the list
    head = None
else:
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None

# Printing the linked list to verify deletion
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
