import numpy as np
from numpy.core.defchararray import array

class SortedArray:
  #Method for calculating the median index of an array
  def MedianSearch(self, start_index, end_index):
    final_length = (start_index + end_index) // 2
    print(final_length)
    if type(final_length) == float:
      return final_length
    else:
      return round(final_length)

  #Binary search method
  def Search_Array(self,arr,number,start_index, end_index):
    median = self.MedianSearch(start_index, end_index)
    if number == median:
      print("The number is found: "+str(number))
      print("The numbers index is: "+str(arr.index(number)))
      return
    if number > int(median):
      start_index = median
      print(start_index)
      self.Search_Array(arr, number, start_index, end_index)
    if number < arr[int(median)]:
      end_index = median
      print(end_index)
      self.Search_Array(arr, number, start_index, end_index)


number = int(input("Enter a number: "))
sorted_array = [1,2,3,4,5,6,7,8,9,10]
print(sorted_array)
print(type(sorted_array))
array = SortedArray()
array.Search_Array(sorted_array, number, 0, sorted_array[-1]) 