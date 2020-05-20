class Queue:

    #----------------------------------------------------------------------

    def __init__(self):

        '''create an empty FIFO queue'''

        self.q = []

    #----------------------------------------------------------------------

    def size(self):

        '''return number of items in the queue

        pre: none

        post: returns number of items in the queue'''

        return len(self.q)

    #----------------------------------------------------------------------

    def enqueue(self, x):

        '''insert x at end of queue

        pre: none

        post: x is added to the queue'''

        self.q.append(x)

    #----------------------------------------------------------------------

    def front(self):

        '''return first item in queue

        pre: queue is not empty; IndexError is raised if empty

        post: returns first item in the queue'''

        return self.q[0]

    #----------------------------------------------------------------------

    def dequeue(self):

        '''remove and return first item in queue

        pre: queue is not empty; IndexError is raised if empty

        post: removes and returns first item in the queue'''

        return self.q.pop(0)

#----------------------------------------------------------------------
