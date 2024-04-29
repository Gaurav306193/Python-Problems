# insertion at beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating Nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connecting nodes to form a linked list
head.next = node2
node2.next = node3
node3.next = node4

# Inserting a node at the beginning
new_head = Node(5)  # New node to be inserted
new_head.next = head
head = new_head  # Updating the head of the list

# Printing the linked list to verify insertion at the beginning
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
