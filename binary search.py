#binary search

def binarysearch(coll,x):
	first = 0
	last = len(coll)-1
	
	while(first<=last):
		mid = (first+last)//2
		if(x>coll[mid]):
			first = mid+1
		elif(x<coll[mid]):
			last = mid-1
		else:
			return (True,mid)
	
	return (False,-1)

data = [2,4,5,6,8,55,2,3,7]
data.sort()
x = int(input("Search: "))
(isFound,index) = binarysearch(data,x);
if(isFound):
	print("List = ",data,"\nFound At position ",index+1);
else:
	print("List = ",data,"\nNot in the list");


