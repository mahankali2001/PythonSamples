from datetime import datetime
import time

class ratelimiter:
    def __init__(self, max_req, time_window):
        self.max_req = max_req
        self.time_win = time_window
        self.requests = {}
    
    def rateLimit(self, customerId) -> bool:
        count, mydt = 0, datetime.now()
        
        if customerId not in self.requests:
            self.requests[customerId] = (1, mydt)
            return True
    
        count, dt = self.requests[customerId] # tuple of count & timestamp
        # count, dt = val
        time_diff = (datetime.now() - dt).total_seconds()
        
        print(time_diff)
        if time_diff > self.time_win:
            count, dt = 1, mydt
        else:
            count += 1

        if count > self.max_req and time_diff < self.time_win:
            return False
        else:
            self.requests[customerId] = (count, dt)
            return True

if __name__ == "__main__":
    s = ratelimiter(5, 30)
    for i in range(10):
        print(s.rateLimit("vijay"))
        time.sleep(5)