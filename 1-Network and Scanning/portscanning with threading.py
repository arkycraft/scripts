# scanning with threading

import threading
from queue import Queue
import socket

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
       s.connect((target, port))
       print(f'Port {port} is open')
    except:
       pass
    finally:
       s.close()

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

target = '192.168.103.127'  # Replace with your target IP
q = Queue()

#Create threads
for x in range(100): # Number of threads
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

# Add ports to the queue
for port in range(1, 65536):
    q.put(port)

q.join() # Wait for all threads to finish
