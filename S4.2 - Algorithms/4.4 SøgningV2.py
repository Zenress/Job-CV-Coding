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
  #It searches by checking if the given search number is smaller or bigger than the median
  #If it is bigger than the median number then the median is used as the start index and we recalculate the median(median)
  #If it is smaller than the median then the median is used as the end index and we recalculate the median(median) 
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

  #Insert method, used for inserting into a sorted array
  def Insert(self, insert_nr, array):
    #Starts by adding the insert_nr to the end of the list
    i = -1
    array.append(insert_nr)
    print(array)
    #Then we run a for loop that compares the insert_nr to the second last element in the list (Since the last element is the one we inserted)
    #If the number is smaller than the second last element then it swaps the 2. It does this by assigning the second last element with the last one's value
    #While holding the second lasts value in a seperate variable (since you can't just swap them as is)
    for x in range(len(array)):
      if insert_nr < array[i-1]:   
        print(array)
        temp_nr = array[i]             
        array[i] = array[i-1]
        array[i-1] = temp_nr             
        i=i-1
      if insert_nr == array[i-1]:
        print(array)
        break

#Creating an "Array" list with a certain range
sorted_array = list(range(1,1000))

#Search algorithm part
number = int(input("Enter a number: "))
print(sorted_array)
print(type(sorted_array))
array = SortedArray()
array.Search_Array(sorted_array, number, 0, sorted_array[-1]) 

#Insert part
insert_nr = int(input("Enter a number to insert into the SortedArray: "))
array.Insert(insert_nr, sorted_array)