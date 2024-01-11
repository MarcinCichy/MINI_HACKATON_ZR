basic_example_queue = ['element1', 'element2', 'element3', 'element4', 'element5']
tup_example_queue = [(1, 'element1'), (2, 'element2'), (3, 'element3'), (5, 'element4'), (5, 'element5')]
dic_example_queue = [{'element1': 1}, {'element2': 2}, {'element3': 3}, {'element4': 5}, {'element5': 5}]


class Queue:
    def __init__(self, queue):
        self.queue = queue

    def add_element(self, new_element):
        self.queue.append(new_element)

    def take_and_remove_first_element(self):
        element = self.queue.pop(0)
        return element

    def take_and_show_first_element(self):
        element_to_show = self.queue[0]
        return element_to_show

    def is_queue_empty(self):
        len_of_queue = self.show_length_of_queue()
        if len_of_queue == 0:
            print(f'Queue is empty')
        else:
            print(f'Queue is not empty')

    def show_length_of_queue(self):
        len_of_queue = len(self.queue)
        return len_of_queue


class PriorityQueue(Queue):
    def __init__(self):
        super().__init__(queue)

    def take_and_remove_high_priority_element(self):
        pass


# dic_example_queue
# tup_example_queue
print(f'Show org queue: {dic_example_queue}')
queue = Queue(dic_example_queue)

print(f"Show length of queue: {queue.show_length_of_queue()}")
queue.is_queue_empty()

queue.add_element({'element6': 3})
# queue.add_element((5, 'element6'))
print(f'Show queue after add element: {dic_example_queue}')
print(f"Show queue's first element: {queue.take_and_show_first_element()}")


print(f"Show length of queue: {queue.show_length_of_queue()}")

queue.take_and_remove_first_element()
print(f'Show queue after remove first element: {dic_example_queue}')


print(f"Show queue's first element: {queue.take_and_show_first_element()}")

dic_example_queue.clear()
# tup_example_queue.clear()
queue.is_queue_empty()
