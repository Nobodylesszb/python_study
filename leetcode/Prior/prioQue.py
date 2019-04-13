import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index +=1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

if __name__ == "__main__":
    q = PriorityQueue()
    q.push('foo',1)
    q.push('yun',5)
    q.push('bar',6)
    print(q.pop())
    print(q.pop())

