# Printing the linked list to verify insertion at the end
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

# Inserting a node at the end
new_node_data = 50  # Data for the new node to be inserted

current = head
while current.next is not None:
    current = current.next

new_node = Node(new_node_data)
current.next = new_node

# Printing the linked list to verify insertion at the end
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
