import threading
import time
import random

class Node:
    def __init__(self, node_id, voting_set):
        self.node_id = node_id
        self.voting_set = voting_set
        self.voted = set()
        self.cs_lock = threading.Lock()

    def request_critical_section(self):
        # Send request to nodes in the voting set
        for node_id in self.voting_set:
            nodes[node_id].receive_request(self.node_id)

        # Wait for votes from the majority of nodes in the voting set
        while len(self.voted) < len(self.voting_set) // 2 + 1:
            time.sleep(0.1)

        # Enter critical section
        self.cs_lock.acquire()
        print(f"Node {self.node_id} entering critical section")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate critical section work
        print(f"Node {self.node_id} exiting critical section")
        self.cs_lock.release()

        # Reset votes and send release message to nodes in the voting set
        self.voted.clear()
        for node_id in self.voting_set:
            nodes[node_id].receive_release(self.node_id)

    def receive_request(self, requesting_node_id):
        if requesting_node_id not in self.voted:
            self.voted.add(requesting_node_id)
            nodes[requesting_node_id].receive_vote(self.node_id)

    def receive_vote(self, voting_node_id):
        self.voted.add(voting_node_id)

    def receive_release(self, releasing_node_id):
        if releasing_node_id in self.voted:
            self.voted.remove(releasing_node_id)

def node_thread(node):
    while True:
        time.sleep(random.uniform(1, 5))  # Simulate non-critical section work
        node.request_critical_section()

# Example usage
num_nodes = 5
voting_sets = [
    {1, 2},  # Voting set for node 0
    {0, 2, 3},  # Voting set for node 1
    {0, 1, 4},  # Voting set for node 2
    {1, 4},  # Voting set for node 3
    {2, 3}   # Voting set for node 4
]

nodes = [Node(i, voting_sets[i]) for i in range(num_nodes)]

# Create and start threads for each node
threads = []
for node in nodes:
    thread = threading.Thread(target=node_thread, args=(node,))
    thread.start()
    threads.append(thread)

# Wait for threads to complete (optional)
for thread in threads:
    thread.join()