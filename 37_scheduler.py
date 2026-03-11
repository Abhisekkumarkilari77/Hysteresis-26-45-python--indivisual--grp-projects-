# 37. Task Scheduler
import heapq, time, threading, uuid

class TaskScheduler:
    def __init__(self):
        self.q = []
        self.cv = threading.Condition()

    def schedule(self, func, delay=0, priority=0):
        run_at = time.time() + delay
        task_id = str(uuid.uuid4())[:8]
        with self.cv:
            heapq.heappush(self.q, (run_at, priority, task_id, func))
            self.cv.notify()
        return task_id

    def run(self):
        while True:
            with self.cv:
                if not self.q:
                    self.cv.wait(); continue
                run_at, priority, tid, func = self.q[0]
                now = time.time()
                if now < run_at:
                    self.cv.wait(run_at - now); continue
                heapq.heappop(self.q)
            func()

if __name__ == "__main__":
    s = TaskScheduler()
    threading.Thread(target=s.run, daemon=True).start()
    s.schedule(lambda: print("hello"), delay=1)
    time.sleep(2)
