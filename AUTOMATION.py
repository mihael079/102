import os
import shutil

source=""
listOfFiles = os.listdir("A")

for file in listOfFiles: 
   name,ext=os.path.splitext(file)
   if (ext==""):
      continue
   if ext in [".gif",'.png','.jpg','.jpeg','jfif','.pdf','.xlsx']:
      #path =source +"/"+file 
      path ="A/"+file
      path2="b/images/"
      path3="b/images/"+file
      if (os.path.exists(path2)):
         shutil.move(path,path3)
      else:
         os.mkdir(path2)
         shutil.move(path,path3)