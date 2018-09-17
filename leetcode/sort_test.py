def maopao(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A
                
def insert(A):
    for i in range(1,len(A)):
        temp = A[i]
        j=i
        while (j > 0):
            if temp < A[j-1]:
                A[j] = A[j-1]
                j -= 1
            else:
                A[j] = temp
                break
        A[j] = temp
    return A



            
def guibing(A,B):
    i = 0
    j = 0
    #flag = 0
    C = list()
    while 1:
        print 2
        '''
        if A[i] < B[j]:
            C.append(A[i])
            i = i + 1
        else:
            C.append(B[j])
            j = j + 1
        if(A[i] == None):
            C = C + B[j:]
            #flag = 1
        if(B[j] == None):
            C = C + A[i:]
            #flag = 1'''
	return C

input1=[6,2,4,1,9,45,23,43]
input2=[3,67,34,56,22,10]
#guibing(input1,input2)
#print insert(input1)
print guibing(input1,input2)
            