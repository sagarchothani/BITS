import threading
import time
import random

class Node:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.clock = 0
        self.request_queue = []
        self.num_nodes = num_nodes
        self.cs_lock = threading.Lock()

    def request_critical_section(self):
        self.clock += 1
        timestamp = (self.clock, self.node_id)
        self.request_queue.append(timestamp)
        print(f"Node {self.node_id} requesting critical section with timestamp {timestamp}")

        # Broadcast request to all other nodes
        for node in nodes:
            if node != self:
                node.receive_request(timestamp)

        # Wait for all other nodes to reply
        while self.request_queue[0] != timestamp:
            time.sleep(0.1)

        # Enter critical section
        self.cs_lock.acquire()
        print(f"Node {self.node_id} entering critical section")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate critical section work
        print(f"Node {self.node_id} exiting critical section")
        self.cs_lock.release()

        # Remove the fulfilled request from the queue
        self.request_queue.pop(0)

    def receive_request(self, timestamp):
        self.clock = max(self.clock, timestamp[0]) + 1
        self.request_queue.append(timestamp)
        print(f"Node {self.node_id} received request from Node {timestamp[1]} with timestamp {timestamp}")

def node_thread(node):
    while True:
        time.sleep(random.uniform(1, 5))  # Simulate non-critical section work
        node.request_critical_section()

# Example usage
num_nodes = 3
nodes = [Node(i, num_nodes) for i in range(num_nodes)]

# Create and start threads for each node
threads = []
for node in nodes:
    thread = threading.Thread(target=node_thread, args=(node,))
    thread.start()
    threads.append(thread)

# Wait for threads to complete (optional)
for thread in threads:
    thread.join()