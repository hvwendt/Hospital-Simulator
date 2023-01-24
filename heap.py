#Harrison Wendt
#30353351
#Created: 11/28/2022
#Last modified: 11/28/2022
#heap.py
class MaxHeap():
    def __init__(self):
        self.heap = []

    def add(self,entry):
        self.heap.append(entry)
        self._upheap(len(self.heap)-1)

    def remove(self):
        self.heap.pop(0)
        self._downheap(0)
       
    def _upheap(self,index):
        if len(self.heap) == 1:
            return self.heap

        if self.heap[index] < self.heap[index//2]:
            return self.heap

        if self.heap[index] > self.heap[index//2]:
            temp = self.heap[index//2]
            self.heap[index//2] = self.heap[index]
            self.heap[index] = temp
            self._upheap(index//2)
        
    def return_length(self):
        return len(self.heap)

    def return_next(self):
        return self.heap[0]

    def _downheap(self,index):

        if len(self.heap) == 1:
            return self.heap

        if len(self.heap) == 2:
            if self.heap[0] > self.heap[1]:
                return self.heap
            else:
                temp = self.heap[0]
                self.heap[0] = self.heap[1]
                self.heap[1] = temp
                return self.heap

        if self.heap[(index*2)+1] > self.heap[(index*2)+2]:
            max = self.heap[(index*2)+1]
            index = (index*2)+1
        else:
            max = self.heap[(index*2)+2]
            index = (index*2)+2
        self.heap[0] = self.heap[len(self.heap)-1]
        if self.heap[0] < max:
            temp = self.heap[0]
            self.heap[0] = max
            self.heap[index] = temp
            self._downheap(index)