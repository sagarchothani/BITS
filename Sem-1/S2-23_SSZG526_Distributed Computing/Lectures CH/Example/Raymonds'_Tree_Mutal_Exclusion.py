import threading
import time
import random

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.parent = None
        self.children = []
        self.requesting_cs = False
        self.token = False
        self.cs_lock = threading.Lock()

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def request_critical_section(self):
        self.requesting_cs = True
        if self.token:
            self.enter_critical_section()
        else:
            self.send_request_to_parent()

    def send_request_to_parent(self):
        if self.parent is not None and not self.token:
            self.parent.receive_request(self)

    def receive_request(self, child):
        if self.token:
            self.send_token_to_child(child)
        else:
            self.requesting_cs = True

    def send_token_to_child(self, child):
        self.token = False
        child.receive_token()

    def receive_token(self):
        self.token = True
        if self.requesting_cs:
            self.enter_critical_section()
        else:
            self.send_token_to_requesting_child()

    def send_token_to_requesting_child(self):
        for child in self.children:
            if child.requesting_cs:
                self.send_token_to_child(child)
                break

    def enter_critical_section(self):
        self.cs_lock.acquire()
        print(f"Node {self.node_id} entering critical section")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate critical section work
        print(f"Node {self.node_id} exiting critical section")
        self.cs_lock.release()
        self.requesting_cs = False
        self.send_token_to_requesting_child()

def node_thread(node):
    while True:
        time.sleep(random.uniform(1, 5))  # Simulate non-critical section work
        node.request_critical_section()

# Example usage
num_nodes = 5
nodes = [Node(i) for i in range(num_nodes)]

# Create tree structure
nodes[0].set_parent(None)  # Root node
nodes[0].add_child(nodes[1])
nodes[0].add_child(nodes[2])
nodes[1].set_parent(nodes[0])
nodes[1].add_child(nodes[3])
nodes[1].add_child(nodes[4])
nodes[2].set_parent(nodes[0])
nodes[3].set_parent(nodes[1])
nodes[4].set_parent(nodes[1])

# Assign initial token to the root node
nodes[0].token = True

# Create and start threads for each node
threads = []
for node in nodes:
    thread = threading.Thread(target=node_thread, args=(node,))
    thread.start()
    threads.append(thread)

# Wait for threads to complete (optional)
for thread in threads:
    thread.join()