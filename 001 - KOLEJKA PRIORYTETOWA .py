tup_example_queue = [('element1', 1), ('element2', 2), ('element3', 3), ('element4', 5), ('element5', 5)]
# tup_example_queue = []


class Queue:
    def __init__(self, queue):
        self.queue = queue

    def add_element(self, new_element):
        self.queue.append(new_element)

    def take_and_remove_first_element(self):
        if self.is_queue_empty():
            return print(f'Queue is empty')
        else:
            self.queue.pop(0)

    def take_and_show_first_element(self):
        if self.is_queue_empty():
            return print(f'Queue is empty')
        else:
            return self.queue[0]

    def is_queue_empty(self):
        return len(self.queue) == 0

    def show_length_of_queue(self):
        return len(self.queue)


class PriorityQueue(Queue):
    def __init__(self, queue):
        super().__init__(queue)

    def take_and_remove_high_priority_element(self):
        if self.is_queue_empty():
            return print(f'Queue is empty')
        else:
            highest_priority_element = max(self.queue, key=lambda x: x[1])
            self.queue.remove(highest_priority_element)


print(f'Show original queue: {tup_example_queue}')
highprior_queue = PriorityQueue(tup_example_queue)
print(f"Show length of org queue: {highprior_queue.show_length_of_queue()}")

print(f"Add element {('element6', 3)} to queue")
highprior_queue.add_element(('element6', 3))
print(f'Show queue after add element: {highprior_queue.queue}')
print("="*150)
print(f"Show length of queue after adding element: {highprior_queue.show_length_of_queue()}")
print(f"Show first element of queue: {highprior_queue.take_and_show_first_element()}")
print(f"Remove high priority element)")
highprior_queue.take_and_remove_high_priority_element()
print(f"Show length of queue after removing: {highprior_queue.show_length_of_queue()}")
highprior_queue.take_and_show_first_element()
print(f"Queue after remove high priority element = {highprior_queue.queue}")
highprior_queue.take_and_remove_high_priority_element()

# print("*"*120)
#
# print(f'Show original queue: {tup_example_queue}')
# queue = PriorityQueue(tup_example_queue)
# for element in list(queue.queue):
#     print(f"Queue = {queue.queue}")
#     print(f"Element = {element}")
#     print(f"Show length of queue: {queue.show_length_of_queue()}")
#     print(f"Show queue's first element: {queue.take_and_show_first_element()}")
#     queue.take_and_remove_first_element()
#     print(f'Show queue after remove first element: {queue.queue}')
#     print("-"*63)
#
#     if queue.is_queue_empty():
#         print(f"Queue is empty")
#         break
