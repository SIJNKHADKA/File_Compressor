

#swapping elements for making the heap invariant after operations
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

# define a function to shift up an element in a min heap
def shift_up(heapqueue, i):
    while i > 0 and heapqueue[i] < heapqueue[(i - 1) // 2]:
        # swap heap[i] with its parent
        swap(heapqueue, i, (i - 1) // 2)
        # update i to be its parent's index
        i = (i - 1) // 2

# define a function to shift down an element in a min heap
def shift_down(heapqueue, i):
    while 2 * i + 1 < len(heapqueue):
        # get the index of left child
        left = 2 * i + 1
        # get the index of right child 
        right = left + 1 if left + 1 < len(heapqueue) else left
        # get the index of the smaller child
        smaller = left if heapqueue[left] < heapqueue[right] else right
        if heapqueue[i] < heapqueue[smaller]:
            break
        swap(heapqueue,i ,smaller)
        # update i to small child index
        i = smaller

# define a function to push an element into a min heap 
def heappush(heapqueue,item):
    heapqueue.append(item)
    shift_up(heapqueue,len(heapqueue)-1)

# define a function to pop an element from a min heaap 
def heappop(heapqueue):
    # if heap is empty return None 
    if not heapqueue:
       return None 
    # swap first and last
    swap(heapqueue ,0 ,len(heapqueue)-1)
    item =heapqueue.pop() 
    shift_down (heapqueue ,0 )
    return item 





    

    





        
        



    
    
