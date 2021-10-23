import socket
import threading
from queue import Queue


target=input("Please input the IP adress that you want to scan:")
queue=Queue()
open_ports=[]


def portscan(port):
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False

    
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port=queue.get()
        if portscan(port):
            print("Port {} is open! Scanning for other ports...".format(port))
            open_ports.append(port)
        

print("Scanning port between port 1-1024")
port_list = range(1,1024)
fill_queue(port_list)

thread_list=[]

for t in range(500):
    thread=threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("List of open ports: ",open_ports)


