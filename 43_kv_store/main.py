#!/usr/bin/env python
# main.py
import socket
from .storage import KVStore
from .protocol import KVServer
from .hashing import HashRing

def run():
    store = KVStore(aof_path="43_kv_store/aof.log")
    server = KVServer(store, port=6381); server.start()
    ring = HashRing(["nodeA","nodeB","nodeC"])
    print("Hash ring node for 'user:1':", ring.get_node("user:1"))
    with socket.create_connection(("127.0.0.1",6381)) as c:
        c.sendall(b"SET foo bar 5\n"); print(c.recv(64))
        c.sendall(b"GET foo\n"); print(c.recv(64))

if __name__ == "__main__":
    run()
