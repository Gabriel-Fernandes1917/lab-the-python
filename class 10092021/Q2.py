from posix import listdir
import sys
import os


x =os.system("ls -d")


print(x)

# list_dir = os.listdir(sys.argv[1])

# for file in list_dir:
#     arq=open(sys.argv[1]+"/"+file,"r")
#     text=arq.read()
#     print(text)
#     arq.close()