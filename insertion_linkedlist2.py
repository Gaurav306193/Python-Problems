
# Printing the linked list to verify insertion after a particular element

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

# Inserting a node after a particular element
new_node_data = 25  # Data for the new node to be inserted
target_data = 20  # Data of the node after which insertion should happen

current = head
while current is not None:
    if current.data == target_data: # cureent == 20
        new_node = Node(new_node_data) # new_node = 25
        new_node.next = current.next
        current.next = new_node
        break
    current = current.next

# Printing the linked list to verify insertion after a particular element
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
