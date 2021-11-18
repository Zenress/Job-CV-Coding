import numpy as np
from numpy.core.defchararray import array

class SortedArray:
  #Method for calculating the median index of an array
  def MedianSearch(self, arr):
    #This method works by taking the index of the value at 0 and the index of the value at the end of the given array
    final_length = (arr.index(arr[0]) + arr.index(arr[-1])) // 2
    print(final_length)
    if type(final_length) == float:
      return final_length
    else:
      return round(final_length)

  #Binary search method
  def Search_Array(self,arr,number, original_array):
    #Running the median search method
    median = self.MedianSearch(arr)
    if number == arr[int(median)]:
      print("The number is found: "+str(number))
      print("The numbers index is: "+str(original_array.index(number)))
    if number > arr[int(median)]:
      new_array = arr[len(arr)//2:]
      print(new_array)
      self.Search_Array(new_array, number, original_array)
    if number < arr[int(median)]:
      new_array = arr[:len(arr)//2]
      print(new_array)
      self.Search_Array(new_array, number, original_array)

number = int(input("Enter a number: "))
sorted_array = [1,2,3,4,5,6,7,8,9,10]
print(sorted_array)
print(type(sorted_array))
array = SortedArray()
array.Search_Array(sorted_array, number, sorted_array) 

