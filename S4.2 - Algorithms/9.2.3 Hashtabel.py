class HashTable:
  class Hash:
    def __init__(self, key, value):
      self.key = str(key)
      self.value = value

  listLength = 20
  itemList = [None] * listLength
  itemCount = 0

  def InsertHash(self,key,value):
    """
    Linear Indexing Solution
    """
    if self.itemCount == self.listLength:
      self.Rehash()
    index = self.HashFunction(key)
    while self.itemList[index] != None:
      print("Collision at " + str(index) + " - " + self.itemList[index].key + " With " + key)
      index = (index + 1) % self.listLength
    self.itemList[index] = self.Hash(key,value)
    self.itemCount += 1
    """
    Linked list solution
    """
  def SearchHash(self,key):
    index = self.HashFunction(key)
    while self.itemList[index] != None and self.itemList[index].key != key:
      index = (index + 1) % self.listLength
    return self.itemList[index].key

  def HashFunction(self,key):
    #Convert each character in key to ascii, add together and divide by list items
    sum = 0
    for x in list(key.encode('ascii')):
      sum += x
    sum = sum % self.listLength
    return sum
  
  def Rehash(self):
    self.listLength *= 2
    tmp = self.itemList
    self.itemList = [None] * self.listLength
    for x in tmp:
      if x != None:
        self.InsertHash(x.key,x.value)
  
hashList = HashTable()
hashList.InsertHash("Mia",18)
hashList.InsertHash("Liam",21)
hashList.InsertHash("Hassib",19)
hashList.InsertHash("William",21)
hashList.InsertHash("Maks",18)
hashList.InsertHash("Shano",21)
hashList.InsertHash("Leon",19)
hashList.InsertHash("Claus",21)
hashList.InsertHash("Lucas",18)
hashList.InsertHash("Christian",21)
hashList.InsertHash("Gustav",19)
hashList.InsertHash("Frederik",21)
hashList.InsertHash("Emma",18)
hashList.InsertHash("Naia",21)
hashList.InsertHash("Skye",19)
hashList.InsertHash("Rikke",21)
hashList.InsertHash("Peter",18)
hashList.InsertHash("Patrick",21)
hashList.InsertHash("Hassib2",19)
hashList.InsertHash("William2",21)
for x in hashList.itemList:
  if x != None:
    print(x.key,x.value)
  else:
    print(x)
print("Done -----------------")
hashList.InsertHash("ToRehash",32)
for x in hashList.itemList:
  if x != None:
    print(x.key,x.value)
  else:
    print(x)

print(hashList.SearchHash("Mia"))


