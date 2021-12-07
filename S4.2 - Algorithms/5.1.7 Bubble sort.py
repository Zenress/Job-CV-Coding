#list(range(1,1000))
#[12,6,14,9,2,21,15,4,20,8,13,5,17,10,11,7,18,1,16,3,19]
import random
unsorted_data = [random.randrange(1,100,1) for i in range(100)]

#Sort inside of Unsorted_data list
def Sort_list(list, sorted_area = 0):
  while sorted_area < len(list):
    #Swap the first index in sorted area until it is in it's sorted place
    min_index = sorted_area
    for i in range(0,len(list)):
      if list[i] > list[min_index]:    
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp
        print(list)
    sorted_area +=1
    

Sort_list(unsorted_data)