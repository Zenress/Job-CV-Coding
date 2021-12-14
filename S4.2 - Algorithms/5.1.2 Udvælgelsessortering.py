#list(range(1,1000))
unsorted_data = [12,6,14,9,2,21,15,4,20,8,13,5,17,10,11,7,18,1,16,3,19,19,69,91,23,34,7,123,54,128,456,23,4,6,13]

def min_value(list,start_index):
  min_element = start_index
  for i in range(start_index,len(list)):
    if list[i] < list[min_element]:
      min_element = i
  return min_element

#Sort inside of Unsorted_data list
def Sort_list(list, sorted_area = 0):
  for x in list:
    lowest_index = min_value(list,sorted_area)
    print(lowest_index)
    print(list[lowest_index])
    temp = list[sorted_area]
    list[sorted_area] = list[lowest_index]
    list[lowest_index] = temp
    sorted_area +=1
    print(list)

Sort_list(unsorted_data)
#Old solution
"""
def Sort_list():
  while len(unsorted_data) != 0:
    lowest_index = min_value(unsorted_data,sorted_area)
    print(lowest_index)
    temp = unsorted_data[0]
    unsorted_data[0] = unsorted_data[lowest_index]
    unsorted_data[lowest_index] = temp
    print(unsorted_data)
    sorted_data.append(unsorted_data[0])
    sorted_area=+1
    unsorted_data = unsorted_data[sorted_area:len(unsorted_data)]
    print(unsorted_data)
    print(sorted_data)
"""

