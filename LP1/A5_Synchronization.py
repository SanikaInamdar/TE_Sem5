import threading
import time

# Shared Memory variables
CAPACITY = 10
buffer = [-1 for i in range(CAPACITY)]
#buffer = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
in_index = 0
out_index = 0

# Declaring Semaphores
#1 means semaphore is free. 0 means acquired
mutex = threading.Semaphore()

# stores number of slots free in buffer.
empty = threading.Semaphore(CAPACITY)
# number of slots full in buffer.
full = threading.Semaphore(0)

# Producer Thread Class
#The acquire() function is used to decrease the count of the semaphore in case 
# the count is greater than zero. Else it blocks till the count is greater than zero.

#The release() function is used for increasing the count of the semaphore 
# and waking up one of the threads waiting on the semaphore.

class Producer(threading.Thread):
    def run(self):

        global CAPACITY, buffer, in_index, out_index,mutex, empty, full

        items_produced = 0
        counter = 0

        while (items_produced < 15):
            empty.acquire()     #turn 0
            mutex.acquire()     #decrement count

            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1) % CAPACITY
            print("Producer produced : ", counter)

            mutex.release()     # turn 1
            full.release()      #increment count

            time.sleep(1)

            items_produced += 1

# Consumer Thread Class


class Consumer(threading.Thread):
    def run(self):

        global CAPACITY, buffer, in_index, out_index
        global mutex, empty, full

        items_consumed = 0

        while items_consumed < 15:
            full.acquire()  # decrement count
            mutex.acquire() # turn 0

            item = buffer[out_index]
            out_index = (out_index + 1) % CAPACITY
            print("Consumer consumed item : ", item)

            mutex.release()     # turn 1
            empty.release()     # increment count

            time.sleep(2.5)

            items_consumed += 1


# Creating Threads
producer = Producer()
consumer = Consumer()

# Starting Threads
consumer.start()
producer.start()

# Waiting for threads to complete
producer.join()
consumer.join()