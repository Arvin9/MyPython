from threading import Thread, Condition
import time
import random
 
queue = []
MAX_NUM = 10
condition = Condition()
 
class ProducerThread(Thread):
    def run(self):
        #nums = range(5)
        num = 1
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print "Queue full, producer is waiting"
                condition.wait()
                print "Space in queue, Consumer notified the producer"
            #num = random.choice(nums)
            queue.append(num)
            print "Produced", num

            num = num + 1
            
            condition.notify()
            condition.release()
            time.sleep(random.random()*10)
 
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print "Nothing in queue, consumer is waiting"
                condition.wait()
                print "Producer added something to queue and notified the consumer"
            num = queue.pop(0)
            print "Consumed", num
            condition.notify()
            condition.release()
            time.sleep(random.random()*10)
 
ProducerThread().start()
ConsumerThread().start()
