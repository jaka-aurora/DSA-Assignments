import queue
import time

order_queue = queue.Queue()

def add_order(order):
    order_queue.put(order)
    print(f"Order added: {order}")

def process_order():
    while not order_queue.empty():
        order = order_queue.get()
        print(f"\nProcessing order: {order}")
        time.sleep(2)
        print(f"Completed order: {order}")

add_order("Pasta Bolognese")
add_order("Pizza")
add_order("Buritto")

print("\nStarting order processing...")
process_order()

print("\nAll orders processed!")
