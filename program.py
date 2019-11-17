import re
N=input("enter email:")
regex=r"\w+@domain.com"
res=re.findall(regex,N)
for r in res:
   print(r)