from itertools import groupby
import re

N=int(input())
entr = [ input()  for i in range(N) ]


def counts(i):
     return max([len(list(g)) for k, g in groupby(i)])

for i in entr:
    pattn = re.compile(r"^[4,5,6]([0-9]{15}$)")
    pattn2 = re.compile(r"^[4,5,6]\d{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$")


    if re.search(pattn, i) or re.search(pattn2, i) :
        if counts(i.replace('-',""))>=4 :
           print('Invalid')
        else:
           print('Valid')
    else:
         print("Invalid")

