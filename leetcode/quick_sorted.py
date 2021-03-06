def quick_sort(lists,left,right):
	if left >= right:
		return

	low = left
	high = right
	key = lists[left]
	while left < right:
		while left < right and lists[right] >= key:
			right -= 1
		lists[left] = lists[right]
		while left < right and lists[left] <= key:
			left += 1
		lists[right] = lists[left]
	lists[right] = key
	
	print lists
	quick_sort(lists,low,left-1)
	quick_sort(lists,left+1,high)

