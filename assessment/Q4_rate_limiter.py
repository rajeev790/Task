import time
from collections import defaultdict
from threading import Lock

class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)
        self.lock = Lock()

    def allow_request(self, user_id):
        with self.lock:
            now = time.time()
            window_start = now - 60
            if len(self.requests[user_id]) >= 5 and self.requests[user_id][0] > window_start:
                return False
            self.requests[user_id].append(now)
            if len(self.requests[user_id]) > 5:
                self.requests[user_id].pop(0)
            return True

if __name__ == "__main__":
    rate_limiter = RateLimiter()
    print(rate_limiter.allow_request('user1'))  # Example usage
