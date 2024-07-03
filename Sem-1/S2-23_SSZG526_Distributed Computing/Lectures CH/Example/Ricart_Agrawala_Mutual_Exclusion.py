import threading
import time
import random

class Node:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.reply_count = 0
        self.request_queue = []
        self.cs_lock = threading.Lock()

    def request_critical_section(self):
        # Send request to all other nodes
        for node in nodes:
            if node != self:
                node.receive_request(self.node_id)

        # Wait for replies from all other nodes
        while self.reply_count < self.num_nodes - 1:
            time.sleep(0.1)

        # Enter critical section
        self.cs_lock.acquire()
        print(f"Node {self.node_id} entering critical section")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate critical section work
        print(f"Node {self.node_id} exiting critical section")
        self.cs_lock.release()

        # Send release message to all other nodes
        for node in nodes:
            if node != self:
                node.receive_release(self.node_id)

        # Reset reply count
        self.reply_count = 0

    def receive_request(self, requesting_node_id):
        self.request_queue.append(requesting_node_id)
        self.send_reply(requesting_node_id)

    def send_reply(self, requesting_node_id):
        nodes[requesting_node_id].receive_reply()

    def receive_reply(self):
        self.reply_count += 1

    def receive_release(self, releasing_node_id):
        self.request_queue.remove(releasing_node_id)

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