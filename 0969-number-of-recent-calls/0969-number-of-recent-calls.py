class RecentCounter:

    def __init__(self):
        #Make self.n a deque so that we can insert or delete from the queue from both side
        self.n=collections.deque()
        

    def ping(self, t: int) -> int:
        #Add the t into the queue
        self.n.append(t)
        #if self.n index 0 element is smaller then t-3000 then remove the element which is present at index 0.
        while self.n[0]<t-3000:
            self.n.popleft()
        #At last return the length of the self.n
        return len(self.n)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)