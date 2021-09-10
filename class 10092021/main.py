import os 
import sys
from typing import Text


# sys.argv[0] --> Return the name the program python in exeing
# sys.argv[1] --> Return the first arg by user for pass
# sys.argv[2] --> Return the second arg by user for pass
# sys.argv[n] --> Return the n arg by user for pass


if os.path.exists(sys.argv[1]):
    print(" O diretorio ja existe")
else:
    os.mkdir(sys.argv[1])
    arq=open(sys.argv[1]+"/"+sys.argv[2,"w"])
    texto=sys.argv[3]
    arg.write(texto)
    arq.close()