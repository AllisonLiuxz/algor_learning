#-*- coding:utf-8 -*-
# insert
def insertSort(messList):
    length = len(messList)
    for count in range(1, length):
        for script in range(count):
            if messList[count] < messList[script]:
                messList.insert(script, messList[count])
                del messList[count+1]
                break
    return messList

def halfInsertSort(messList):
    length = len(messList)
    for count in range(1, length):
        low = 0
        high = count - 1
        while low <= high:
            mid = (low + high)/2
            if (messList[mid] >= messList[count] and messList[mid-1] < messList[count] and mid != 0) or (mid == 0 and messList[mid] >= messList[count]):#不是小于就可以
                messList.insert(mid, messList[count])
                print messList
                del messList[count+1] #important
                break
            elif messList[mid] < messList[count]:
                low = mid + 1
            else:
                high = mid - 1
    return messList

def shellInsertSort(messList, n):
    length = n
    delta = n / 2
    while delta >= 1:
        waitToInsert = delta
        while waitToInsert < length:
            compareNode = delta
            while compareNode <= waitToInsert:
                if messList[waitToInsert] < messList[compareNode - delta]:#希尔排序的内部仍然是插入排序，所以思路不能变
                    temp = messList[waitToInsert]
                    insertPos = compareNode - delta
                    countTemp = waitToInsert - delta
                    while countTemp >= insertPos:
                        messList[countTemp+delta] = messList[countTemp]
                        countTemp -= delta
                    messList[insertPos] = temp
                    print messList
                    break
                compareNode += delta
                
            waitToInsert += delta
        delta = delta / 2
    return messList

# exchange
def bubbleSort(messList):
    length = len(messList)
    swap = 0# 提高算法性能
    for count in range(length):
        swap = 0
        for script in range(length-1-count):
            if messList[script] > messList[script+1]:
                temp = messList[script]
                messList[script] = messList[script+1]
                messList[script+1] = temp
                swap = 1
        if swap == 0:
            break
    return messList

def fastSort(messList, low, high):
    temp = messList[low]
    while low < high:
        while low < high and messList[high] > temp:
            high -=1
        if low < high:
            messList[low] = messList[high]
            low +=1
        while low < high and messList[low] < temp:
            low +=1
        if low < high:
            messList[high] = messList[low]
            high -=1
    messList[low] = temp
    return low
def fsort(messList, low, high):
    if low < high:
        i = fastSort(messList, low, high)
        fsort(messList, low, i-1)
        fsort(messList, i+1, high)
        return messList

def bubSort(messList):
    length = len(messList)
    for count in range(length):
        for script in range(count+1, length):
            if messList[script] < messList[count]:
                temp = messList[count]
                messList[count] = messList[script]
                messList[script] = temp
    return messList

# choice sort
def simpleChoiceSort(messList):
    length = len(messList)
    for current in range(length-1):
        for comparePos in range(current+1, length):
            if messList[comparePos] < messList[current]:
                temp = messList[current]
                messList[current] = messList[comparePos]
                messList[comparePos] = temp
    return messList

def heapAdjust(mess, roof, end):
    temp = mess[roof]
    child = roof*2 + 1
    current = roof
    while child <= end:
        if child != end and (mess[child] < mess[child+1]):
            child += 1
        if temp > mess[child]:
            break
        mess[current] = mess[child]
        current = child
        child = current*2 + 1
    mess[current] = temp

def heapSort(mess):
    length = len(mess)
    count = (length - 2)/2
    while count >= 0:
        heapAdjust(mess, count, length-1)
        count = count - 1
    for count in range(length):
        temp = mess[0]
        mess[0] = mess[length-count-1]
        mess[length-count-1] = temp
        heapAdjust(mess, 0, length-count-2)
    return mess


# merge sort
def mergeSort(temp1, temp2):
    length1 = len(temp1)
    length2 = len(temp2)
    count1, count2 = 0, 0
    temp = list()
    while count1 < length1 and count2 < length2:
        if temp1[count1] < temp2[count2]:
            temp.append(temp1[count1])
            count1 += 1
        else:
            temp.append(temp2[count2])
            count2 += 1
    if count1 < length1:
        temp.extend(temp1[count1:])
    if count2 < length2:
        temp.extend(temp2[count2:])
    return temp

def twoRoadMerge(mess, order, start, mid, end):
    count1 = start
    count2 = mid + 1
    countOrder = start
    while count1 <= mid and count2 <= end:
        if mess[count1] < mess[count2]:
            order[countOrder] = mess[count1]
            count1 += 1
        else:
            order[countOrder] = mess[count2]
            count2 += 1
        countOrder += 1
    while count1 <= mid:
        order[countOrder] = mess[count1]
        count1 += 1
        countOrder += 1
    while count2 <= end:
        order[countOrder] = mess[count2]
        count2 += 1
        countOrder += 1

def onceTwoRoadMerge(mess, order, length, end):
    pos = 0
    while pos + length*2 - 1 <= end:
        twoRoadMerge(mess, order, pos, pos+length-1, pos+length*2-1)
        pos += length*2
    if pos + length - 1 < end:
        twoRoadMerge(mess, order, pos, pos+length-1, end)
    elif pos <= end:# 存在pos大于end的情况
        while pos <= end:
            order[pos] = mess[pos]
            pos += 1
    print order

def twoRoadMergeSort(mess, order):
    end = len(mess) - 1
    length = 1
    while True:
        onceTwoRoadMerge(mess, order, length, end)
        length *= 2
        if length > end + 1:
            break
        onceTwoRoadMerge(order, mess, length, end)
        length *= 2
        if length > end + 1:
            order = mess# 为了让最后结果出现在order中
            break
    return order
'''
count = 20
mess = []
for item in range(count):
    mess.insert(0, item)

import time
'''
'''
print time.time()
half = halfInsertSort(mess)
print half
print "half is ok"
print time.time()


count = 10
mess = []
for item in range(count):
    mess.insert(0, item)
inse = insertSort(mess)
print "shell is ok"
print time.time()
if half == inse:
    print "Half is right"
'''

order = [1,2,5,5,8,1,3,5,4,6,9,10,0,11,12,55,66,9,5,88,6,8,9]
print shellInsertSort(order, len(order))