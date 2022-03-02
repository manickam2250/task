import os
from os import walk
for root,dir,files in walk("/home/manikam/projects"):
    # print(root,"--------->",dir,"------>",files)
    for j in files:

      
          if j[-1:-4:-1] == "txt":

            if dir==[]:  
              with open (f"{root}/{j}","r") as file1:
                  data=file1.read()
                  print(data)
                  break