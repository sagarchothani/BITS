
import threading
import time

# Define the critical section
critical_section = threading.Lock()

# Function representing the critical section
def critical_function(node_id):
    global critical_section
    
    # Acquire the lock (enter critical section)
    critical_section.acquire()
    
    print(f"Node {node_id} entered critical section")
    
    # Critical section code
    time.sleep(2)  # Simulating some work inside the critical section
    
    print(f"Node {node_id} exited critical section")
    
    # Release the lock (exit critical section)
    critical_section.release()

# Function to simulate node behavior
def node_behavior(node_id):
    while True:
        print(f"Node {node_id} wants to enter critical section")
        
        # Call the critical function to acquire lock and execute critical section
        critical_function(node_id)
        
        time.sleep(3)  # Simulating other tasks outside the critical section

# Create threads representing nodes
node1 = threading.Thread(target=node_behavior, args=(1,))
node2 = threading.Thread(target=node_behavior, args=(2,))
node3 = threading.Thread(target=node_behavior, args=(3,))

# Start the node threads
node1.start()
node2.start()
node3.start()

# Wait for node threads to finish
node1.join()
node2.join()
node3.join()

print("All nodes finished")
