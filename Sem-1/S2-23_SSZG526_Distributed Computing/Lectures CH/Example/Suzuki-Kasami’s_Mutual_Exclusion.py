import threading
import time
import random

class Node:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.token = None
        self.request_queue = []
        self.cs_lock = threading.Lock()

    def request_critical_section(self):
        # Send request to all other nodes
        for node in nodes:
            if node != self:
                node.receive_request(self.node_id)

        # Wait for token
        while self.token is None or self.token[0] != self.node_id:
            time.sleep(0.1)

        # Enter critical section
        self.cs_lock.acquire()
        print(f"Node {self.node_id} entering critical section")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate critical section work
        print(f"Node {self.node_id} exiting critical section")
        self.cs_lock.release()

        # Release token and send to next requesting node
        self.release_token()

    def receive_request(self, requesting_node_id):
        self.request_queue.append(requesting_node_id)
        if self.token is not None and self.token[0] == self.node_id:
            self.release_token()

    def receive_token(self, token):
        self.token = token
        if self.node_id in self.request_queue:
            self.request_queue.remove(self.node_id)

    def release_token(self):
        if len(self.request_queue) > 0:
            next_node_id = self.request_queue.pop(0)
            self.token = (next_node_id, self.token[1] + 1)
            nodes[next_node_id].receive_token(self.token)
        else:
            self.token = (self.node_id, self.token[1])

def node_thread(node):
    while True:
        time.sleep(random.uniform(1, 5))  # Simulate non-critical section work
        node.request_critical_section()

# Example usage
num_nodes = 5
nodes = [Node(i, num_nodes) for i in range(num_nodes)]

# Assign initial token to the first node
nodes[0].token = (0, 0)

# Create and start threads for each node
threads = []
for node in nodes:
    thread = threading.Thread(target=node_thread, args=(node,))
    thread.start()
    threads.append(thread)

# Wait for threads to complete (optional)
for thread in threads:
    thread.join()