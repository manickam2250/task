from os import walk
for root,dir,files in walk("/home/manikam/projects"):
    # print(root,"--------->",dir,"------>",files)
    for j in files:

      
          if j[-1:-4:-1] == "txt":
              print(j)
