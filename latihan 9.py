# Program Binary Search
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print('Cari nilai 6: ', binary_search([1,2,3,5,8], 6))
print('Cari nilai 5: ', binary_search([1,2,3,5,8], 5))


# Program Bubble Sort
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]<nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
print('Data sebelum di sort', nlist)
bubbleSort(nlist)
print('Data setelah di sort', nlist)


# Program Selection Sort
def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxpos]:
               maxpos = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxpos]
       nlist[maxpos] = temp

nlist = [14,46,43,27,57,41,45,21,70]
print('data sebelum di sort: ', nlist)
selectionSort(nlist)
print('data setelah di sort: ', nlist)


# Program Sequential Search
def Sequential_Search(dlist, item):

    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos

print('cari angka 31: ',Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))
print('cari angka 99: ',Sequential_Search([11,23,58,31,56,77,43,12,65,19],1))