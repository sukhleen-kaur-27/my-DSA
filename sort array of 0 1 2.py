from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr, n):

	# Write your code here
	# arr.sort(reverse = False)
	i, j, k = 0, 0 ,n-1
	while (j<=k and i<=k):
		if(arr[j]==1):
			j+=1
		elif arr[j]==0:
			arr[j]=arr[i]
			j+=1
			arr[i]=0
			i+=1
		else :
			arr[j] = arr[k]
			arr[k]=2
			k-=1