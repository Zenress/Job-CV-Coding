from typing import List
import random

class Pointers:
  def __init__(self,list):
    self.Left = 0
    self.Right = len(list)-1
    self.PV = None

#L = Left, R = Right, PV = PiVot
# First til Last er den el af arrayet vi skal sortere
  def Quicksort(self,First,Last,list):
    print(list)
    Right = Last  #len(list)-1
    Left = First
    PV = list[Left] 
    if First >= Last:
      return 
    #While loop that sorts numbers smaller than PV to the left and bigger than to the right
    while Right >= Left:  
      if list[Left] < PV:
        Left+=1
      elif list[Right] > PV:
        Right-=1
      else:
        list[Left], list[Right] = list[Right], list[Left]
        Left+=1
        Right-=1
      
    #Left side
    self.Quicksort(First,Right,list)
    #Right side
    self.Quicksort(Left,Last,list)

#mylist = [12,6,14,9,2,21,15,4,20,8,13,5,7,17,10,11,7,18,1,16,3,19,21] 
mylist = [random.randrange(1,100,1) for i in range(100)]
qs = Pointers(mylist)
qs.Quicksort(qs.Left,qs.Right,mylist)