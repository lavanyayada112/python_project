
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  def insert_at_position(self, position, data):
    if position < 0:
      print("Invalid position.")
      return

    new_node = Node(data)

    if position == 0:
      self.insert_at_beginning(data)
      return

    current = self.head
    count = 0
    while current and count < position - 1:
      current = current.next
      count += 1

    if current is None:
      print("Position out of bounds.")
      return

    new_node.next = current.next
    current.next = new_node

  def delete_from_beginning(self):
    if self.head is None:
      print("List is empty.Cannot delete.")
      return
    self.head = self.head.next

  def delete_from_end(self):
    if self.head is None:
      print("List is empty. Cannot delete.")
      return
    if self.head.next is None:
      self.head = None
      return
    current = self.head
    while current.next.next:
      current = current.next
    current.next = None

  def search_element(self, data):
    current = self.head
    position = 0
    while current:
      if current.data == data:
        return position
      current = current.next
      position += 1
    return -1  # Element not found

  def display_list(self):
    current = self.head
    if current is None:
      print("List is empty.")
      return
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

# Example Usage:
my_list = LinkedList()
my_list.insert_at_beginning(10)
my_list.insert_at_end(20)
my_list.insert_at_end(30)
my_list.insert_at_beginning(5)
my_list.insert_at_position(2, 15)

my_list.display_list()

my_list.delete_from_beginning()
my_list.delete_from_end()

my_list.display_list()

search_data = 15
position = my_list.search_element(search_data)
if position != -1:
    print(f"{search_data} found at position {position}")
else:
    print(f"{search_data} not found in the list")

search_data = 100
position = my_list.search_element(search_data)
if position != -1:
   print(f"{search_data} found at position {position}")
else:
   print(f"{search_data} not found in the list")
