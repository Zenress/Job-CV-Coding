#Step 1. Recursive Method Msort takes a list as a parameter. It calls itself recursively until there is only one element left. 
def MSort(list):
  if len(list) <= 1:
    return list
  else:
    list1,list2 = Splitting(list)
    list1 = MSort(list1)
    list2 = MSort(list2)
  return  Merging(list1, list2)

#Step 2. Split method for splitting a list into 2 lists
def Splitting(list):
  half = len(list)//2  
  return list[:half],list[half:]

#Step 3. Merge method takes 2 lists and returns a new list which is a sorted version of the 2 lists put together
def Merging(list1,list2):
  returnlist = []
  l1_index = 0
  l2_index = 0
  while l1_index != len(list1) and l2_index != len(list2):
    if list1[l1_index] < list2[l2_index]:
      returnlist.append(list1[l1_index])
      l1_index+=1
    else:
      returnlist.append(list2[l2_index])
      l2_index+=1
  #Adding the left over element(s)
  for x in range(l1_index,len(list1)):
    returnlist.append(list1[x])
  #Adding the left over element(s)
  for x in range(l2_index,len(list2)):
    returnlist.append(list2[x])
  print(returnlist)
  return returnlist

#Step 4.
list = [12,6,14,9,2,21,15,4,20,8,13,5,17,10,11,7,18,1,16,3,19]
print(MSort(list))