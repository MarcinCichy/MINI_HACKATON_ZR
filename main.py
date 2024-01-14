tup_example_queue = [('element1', 1), ('element2', 2), ('element3', 3), ('element4', 5), ('element5', 5)]


class Queue:
    def __init__(self, queue):
        self.queue = queue

    def add_element(self, new_element):
        self.queue.append(new_element)

    def take_and_remove_first_element(self):
        self.queue.pop(0)

    def take_and_show_first_element(self):
        return self.queue[0]

    def is_queue_empty(self):
        if len(self.queue) == 0:
            return print(f"Queue is empty")

    def show_length_of_queue(self):
        return len(self.queue)


class PriorityQueue(Queue):
    def __init__(self, queue):
        super().__init__(queue)

    def take_and_remove_high_priority_element(self):
        highest_priority_element = max(self.queue, key=lambda x: x[1])
        self.queue.remove(highest_priority_element)


print(f'Show org queue: {tup_example_queue}')
queue = Queue(tup_example_queue)
print(f"Show length of org queue: {queue.show_length_of_queue()}")

print(f"Add element to queue")
# queue.add_element({'element6': 3})
queue.add_element(('element6', 3))
print(f'Show queue after add element: {queue.queue}')
print("="*63)
#
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
#         break

highpr_queue = PriorityQueue(tup_example_queue)
highpr_queue.take_and_remove_high_priority_element()
highpr_queue.show_length_of_queue()
highpr_queue.take_and_show_first_element()
print(f"Queue after remove highpriority element = {highpr_queue.queue}")