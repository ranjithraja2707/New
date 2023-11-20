from collections import Counter
my_list = [1, 2, 3, 1, 2, 1, 3, 4, 5]
counter = Counter(my_list)
print(counter)
print("//Counter operations//")
print(counter[1])
# Updating counts using another iterable
another_list = [1, 2, 3, 4]
counter.update(another_list)
print(counter)
another_counter = Counter([1, 2, 3, 1, 2])
counter.update(another_counter)
print(counter)
print(list(counter.elements()))






