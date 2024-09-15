class Task:
    """
    Class representing a task in the priority queue.
    
    Attributes:
    - task_id: Unique identifier for the task.
    - priority: Priority of the task (lower values represent higher priority in a min-heap).
    - arrival_time: Time the task arrives in the system.
    - deadline: Deadline by which the task must be completed.
    """
    
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
    
    def __lt__(self, other):
        """Comparison method for priority, enabling min-heap behavior."""
        return self.priority < other.priority
    
    def __repr__(self):
        """Representation of the task for easier debugging and display."""
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"


class PriorityQueue:
    """
    A class implementing a priority queue using a binary heap.
    This implementation uses a min-heap, meaning tasks with lower priority values are extracted first.
    
    Methods:
    - insert(task): Adds a new task to the heap.
    - extract_min(): Removes and returns the task with the lowest priority.
    - decrease_key(index, new_priority): Decreases the priority of a task and restores heap property.
    - increase_key(index, new_priority): Increases the priority of a task and restores heap property.
    - is_empty(): Checks if the heap is empty.
    - heapify_up(index): Restores the heap property by bubbling up the task at a given index.
    - heapify_down(index): Restores the heap property by bubbling down the task at a given index.
    """
    
    def __init__(self):
        """Initialize an empty priority queue."""
        self.heap = []
    
    def insert(self, task):
        """
        Insert a new task into the heap and maintain the min-heap property. 
        """
        self.heap.append(task)  # Add task to the end of the array
        self.heapify_up(len(self.heap) - 1)  # Restore the heap property by heapifying up
    
    def extract_min(self):
        """
        Remove and return the task with the lowest priority (min-heap).
        """
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # Only one task, no need to heapify
        
        root = self.heap[0]  # Save the root (min task)
        self.heap[0] = self.heap.pop()  # Move the last task to the root
        self.heapify_down(0)  # Restore the heap property by heapifying down
        return root
    
    def decrease_key(self, index, new_priority):
        """
        Decrease the priority of a task at the given index. 
        Perform heapify-up to restore heap property.
        """
        self.heap[index].priority = new_priority
        self.heapify_up(index)
    
    def increase_key(self, index, new_priority):
        """
        Increase the priority of a task at the given index.
        Perform heapify-down to restore heap property.
        """
        self.heap[index].priority = new_priority
        self.heapify_down(index)
    
    def is_empty(self):
        """Return True if the heap is empty, otherwise False."""
        return len(self.heap) == 0
    
    def heapify_up(self, index):
        """
        Restore the heap property by bubbling the task at the given index up.
        """
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:  # Min-heap property
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    def heapify_down(self, index):
        """
        Restore the heap property by bubbling the task at the given index down.
        """
        while index < len(self.heap):
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index
            
            if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
                
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


# Example Scheduler Simulation

def schedule_tasks(tasks):
    """
    A simple scheduler simulation that processes tasks using a priority queue.
    
    Arguments:
    - tasks: A list of Task objects to be scheduled.
    
    The tasks with the lowest priority are processed first.
    """
    pq = PriorityQueue()
    
    # Insert tasks into the priority queue
    for task in tasks:
        pq.insert(task)
    
    # Process tasks in the order of their priority
    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Processing {task}")


# Example usage of the scheduler
if __name__ == "__main__":
    tasks = [
        Task(task_id=1, priority=5, arrival_time=10, deadline=20),
        Task(task_id=2, priority=2, arrival_time=12, deadline=25),
        Task(task_id=3, priority=8, arrival_time=15, deadline=30)
    ]
    
    print("Scheduling tasks based on priority:")
    schedule_tasks(tasks)
