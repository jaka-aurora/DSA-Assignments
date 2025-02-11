# ## 04-03. Reflection task
# How do you implement priority for the orders?
# How orders can be prepared in parallel in the order of their arrival, but they have a separate completion time, i.e. the final order can be different.
# Can a data structure other than a queue be used to build the restaurant's ordering system?

# For priority orders, we use queue.PriorityQueue() instead of Queue().
# Each order is stored as (priority, order_name).
# Lower values mean higher priority that is, order with priority 1 is processed before order with priority 3.
# Orders with the same priority use FIFO.

import queue
import time

order_queue = queue.PriorityQueue()

def add_order(order, priority):
    order_queue.put((priority, order))
    print(f"Order added: {order} (Priority: {priority})")

def process_orders():
    while not order_queue.empty():
        priority, order = order_queue.get()
        print(f"\nProcessing order: {order} (Priority: {priority})")
        time.sleep(2)
        print(f"Completed order: {order} (Priority: {priority})")

add_order("Burger", 2)
add_order("VIP Steak", 1)  # Higher priority
add_order("Pizza", 3)   # Lower priority
add_order("Salad", 2)
print("\nProcessing orders...")
process_orders()

# To prepare orders in parallel, but with different completion times, we can use multithreading (threading.Thread).
# In that example, we would have different chefs preparing orders and each chef picks the next available order from the queue.
# Some orders take longer to complete, but new orders can come in.

import queue
import threading
import time
import random

order_queue = queue.Queue()

def add_order(order):
    order_queue.put(order)
    print(f"Order added: {order}")

def process_order():
    while not order_queue.empty():
        order = order_queue.get()
        prep_time = random.randint(2, 6)  # Simulating different cooking times
        print(f"Started processing: {order} (Time: {prep_time}s)")
        time.sleep(prep_time)
        print(f"Completed order: {order}")

add_order("Burger")
add_order("Pizza")
add_order("Pasta")
add_order("Salad")

threads = []
for _ in range(3):  # 3 chefs
    t = threading.Thread(target=process_order)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\nAll orders processed!")

# We can organize it in LIFO way as well, using stack, if that makes sense for the business model.
# We can use dictionary to store order information: order and arrival time. Then use that to process the orders in the order they arrived.


