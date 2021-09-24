import time
from colors import *

# function to perform BUBBLE SORT
def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(0,size-1):  
        for j in range(size-1):  
            if(data[j]>data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                colorData = [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))]
                drawData(data, colorData )
                time.sleep(timeTick)
    else:
        colorData = [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))]
        drawData(data, colorData)

#function to perform ISERTiON SORT
def insertion_sort(data, drawData, timeTick): 
    size = len(data)
    for i in range(1, size):  
        value = data[i]
        j = i - 1  
        while j >= 0 and value < data[j]:  
            data[j + 1] = data[j]  
            j -= 1  
            colorData = [PURPLE if x == i else YELLOW if x == j or x == j + 1 else BLUE for x in range(size) ]
            drawData(data, colorData)
            time.sleep(timeTick)
        data[j + 1] = value

# function to perform SELECTION SORT
def selection_sort(data, drawData, timeTick):
    size = len(data)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if data[i] < data[min_idx]:
                min_idx = i
                colorData = [YELLOW if x == step or x == min_idx else BLUE for x in range(size)]
                drawData(data, colorData)
                time.sleep(timeTick)
        else:
            (data[step], data[min_idx]) = (data[min_idx], data[step])
            colorData = [YELLOW if x == step or x == min_idx else BLUE for x in range(size)]
            drawData(data, colorData)
            time.sleep(timeTick)

# function to perform MERGE in merge sort.
def merge(data, start, mid, end, drawData, timeTick):
        p = start
        q = mid + 1
        tempArray = []

        for i in range(start, end+1):
            if p > mid:
                tempArray.append(data[q])
                q+=1
            elif q > end:
                tempArray.append(data[p])
                p+=1
            elif data[p] < data[q]:
                tempArray.append(data[p])
                p+=1
            else:
                tempArray.append(data[q])
                q+=1

        for p in range(len(tempArray)):
            data[start] = tempArray[p]
            start += 1

# function to perform MERGER SORT
def merge_sort(data, start, end, drawData, timeTick):
        if start < end:
            mid = int((start + end) / 2)
            merge_sort(data, start, mid, drawData, timeTick)
            merge_sort(data, mid+1, end, drawData, timeTick)

            merge(data, start, mid, end, drawData, timeTick)

            drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid else BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
            time.sleep(timeTick)

        drawData(data, [BLUE for x in range(len(data))])

# function to perform partition in QUICK SORT
def partition(data, drawData, timeTick, low, high):
    size = len(data)
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            (data[i], data[j]) = (data[j], data[i])
            colorData = [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))]
            drawData(data, colorData )
            time.sleep(timeTick)
    else:
        (data[i + 1], data[high]) = (data[high], data[i + 1])
        colorData = [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))]
        drawData(data, colorData)
    return i + 1

# function to perform QUICK SORT
def quick_sort(data, drawData, timeTick, low, high):
    if low < high:
        size = len(data)
        pi = partition(data, drawData, timeTick, low, high)
        colorData = [PURPLE if x == pi else BLUE for x in range(len(data))]
        drawData(data, colorData)
        time.sleep(timeTick)

        quick_sort(data, drawData, timeTick, low, pi - 1)
        colorData = [PURPLE if x == pi else YELLOW if x < pi and x >= low else BLUE for x in range(len(data))]
        drawData(data, colorData)
        time.sleep(timeTick)

        quick_sort(data, drawData, timeTick, pi + 1, high)
        colorData = [PURPLE if x == pi else BLUE if x > pi and x <= high else BLUE for x in range(len(data))]
        drawData(data, colorData)
        time.sleep(timeTick)
