capacity = 100
array = [None]*capacitysize = 0
size = 0

def isEmpty():
    if size == 0 : return True
    else : return False

def isFull():
    return size == capacity

def getEntry(pos) :
    if 0 <= pos < size:
        return array[pos]
    else : return None

def insert(pos, e) :
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else:
        print("List overflow or invalid insertion position")
        exit()

def delete(pos) :
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size-1):
            array[i] = array[i+1]
        size -= 1
        return e
    else:
        print("List underflow or invalid deletion position")
        exit()
