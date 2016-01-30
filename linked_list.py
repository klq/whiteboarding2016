import node

def class LinkedList():
  def __init__(self):
    self.head = None

  def append(self, value = None):
    pass

  def prepend(self, value = None):
    pass

  def delete(self, value):
    if not self.head:
      return None

    if self.head.value == value:
      p = self.head
      self.head = p.next
      return p

    current = self.head
    while current.next:
      if current.next.value == value:
        p = current.next
        current.next = current.next.next
        return p
      else:
        current = current.next
    return None

