# 선형 큐
front = -1
rear = -1
Q = [0] * 3
qsize = len(Q)


def enqueue(data):
    global rear
    if rear == len(Q)-1:
        print("Queue full")
    else:
        rear += 1
        Q[rear] = data


def dequeue(data):
    global front
    if front == rear:
        print("Queue empty")
    else:
        front += 1
        return Q[front]

enqueue(1)
enqueue(2)
enqueue(3)
print(dequeue(1))
print(dequeue(2))
print(dequeue(3))