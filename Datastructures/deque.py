from collections import deque
my_deque = deque()
my_deque = deque([1, 2, 3, 4, 5])
print(my_deque)

print("//operations in deque//")
my_deque.append(6)
my_deque.appendleft(0)
rightmost_element = my_deque.pop()
leftmost_element = my_deque.popleft()
print(my_deque[0])
length = len(my_deque)
if len(my_deque) == 0:
    print("Deque is empty")
for item in my_deque:
    print(item)
my_deque.clear()


