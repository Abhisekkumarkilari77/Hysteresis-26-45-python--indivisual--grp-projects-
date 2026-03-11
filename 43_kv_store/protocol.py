# protocol.py
import socket
import threading
from .storage import KVStore

class KVServer(threading.Thread):
    def __init__(self, store: KVStore, host="127.0.0.1", port=6380):
        super().__init__(daemon=True)
        self.store = store; self.host=host; self.port=port
    def run(self):
        with socket.socket() as s:
            s.bind((self.host,self.port)); s.listen()
            while True:
                conn, _ = s.accept()
                threading.Thread(target=self.handle, args=(conn,), daemon=True).start()
    def handle(self, conn):
        with conn:
            for line in conn.makefile():
                parts = line.strip().split()
                if not parts: continue
                cmd = parts[0].upper()
                if cmd == "SET" and len(parts)>=3:
                    ttl = float(parts[3]) if len(parts)>3 else None
                    self.store.set(parts[1], " ".join(parts[2:3]), ttl)
                    conn.sendall(b"OK\n")
                elif cmd == "GET" and len(parts)==2:
                    val = self.store.get(parts[1]); conn.sendall((str(val)+"\n").encode())
                elif cmd == "DEL" and len(parts)==2:
                    self.store.delete(parts[1]); conn.sendall(b"OK\n")
                else:
                    conn.sendall(b"ERR\n")
