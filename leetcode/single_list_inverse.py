class Node:
	def __init__(self,x):
		self.val = x
		self.next = None

def inverse(head):
	if head == None or head.next == None:
		return head

	cur = head
	pre = None

	while cur:
		i_h = cur
		temp = cur.next
		cur.next = pre
		pre = cur
		cur = temp
	return i_h

h = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
h.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None
# p = h
# while p:
# 	print "-",p.val
# 	p = p.next
q = inverse(h)
while q:
	print q.val
	q = q.next