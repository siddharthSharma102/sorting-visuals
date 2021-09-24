import time
from colors import *

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

def insertion_sort(list1):  
  
        # Outer loop to traverse through 1 to len(list1)  
        for i in range(1, len(list1)):  
  
            value = list1[i]  
  
            # Move elements of list1[0..i-1], that are  
            # greater than value, to one position ahead  
            # of their current position  
            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
            list1[j + 1] = value  
        return list1  
            # Driver code to test above  

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

def merge_sort(data, start, end, drawData, timeTick):
        if start < end:
            mid = int((start + end) / 2)
            merge_sort(data, start, mid, drawData, timeTick)
            merge_sort(data, mid+1, end, drawData, timeTick)

            merge(data, start, mid, end, drawData, timeTick)

            drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid else BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
            time.sleep(timeTick)

        drawData(data, [BLUE for x in range(len(data))])

# class Algo:
#     def __init__(self):
#         self.name = "Sorting Algo Visualiser"
    
#     def bubble_sort(self, data, drawData, timeTick):
#         size = len(data)
#         for i in range(size-1):
#             for j in range(size-i-1):
#                 if data[j] > data[j+1]:
#                     data[j], data[j+1] = data[j+1], data[j]
#                     drawData(data, ["yellow" if x == j or x == j+1 else "blue" for x in range(len(data))] )
#                     time.sleep(timeTick)
                    
#         drawData(data, ["blue" for x in range(len(data))])
    
#     def merge(self, data, start, mid, end, drawData, timeTick):
#         p = start
#         q = mid + 1
#         tempArray = []

#         for i in range(start, end+1):
#             if p > mid:
#                 tempArray.append(data[q])
#                 q+=1
#             elif q > end:
#                 tempArray.append(data[p])
#                 p+=1
#             elif data[p] < data[q]:
#                 tempArray.append(data[p])
#                 p+=1
#             else:
#                 tempArray.append(data[q])
#                 q+=1

#         for p in range(len(tempArray)):
#             data[start] = tempArray[p]
#             start += 1

#     def merge_sort(self, data, start, end, drawData, timeTick):
#         if start < end:
#             mid = int((start + end) / 2)
#             self.merge_sort(data, start, mid, drawData, timeTick)
#             self.merge_sort(data, mid+1, end, drawData, timeTick)

#             self.merge(data, start, mid, end, drawData, timeTick)

#             drawData(data, ["purple" if x >= start and x < mid else "yellow" if x == mid else "dark blue" if x > mid and x <=end else "blue" for x in range(len(data))])
#             time.sleep(timeTick)

#         drawData(data, ["blue" for x in range(len(data))])

