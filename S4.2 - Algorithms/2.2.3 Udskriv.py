from pathlib import Path
import os
from os import listdir
from os.path import isfile, join

path = input("Please type a path: f.x. users/shano/downloads ")
def Print_Folders(path, level = 0):
  Print_Files(path)
  folders = Get_Folders(path)
  for x in folders:
    Print_Folders(x,level+1)


def Print_Files(path):
  onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
  for x in onlyfiles:
    print(x + " Path:  " + path)

def Get_Folders(path):    
  subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
  return subfolders


Print_Folders(path)

"""void PrintFolder(string path, int level = 0)
{
  PrintFiles(path);
  string[] folders = GetFolders(path);
  foreach (string foldername in folders) {
    PrintFolders(path+"/"+foldername, Level+1);
  }
}"""


