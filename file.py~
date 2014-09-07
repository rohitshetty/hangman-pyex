import random

count=0
ans=[]

def check(inp,filmtup):
 arg=[]
 for n,i in enumerate(filmtup):
  if(inp==i):
   arg.append(n)
 if(len(arg)==0):
  return -1
 else:
  return arg

f=open('film.txt','r')
x=random.randint(1,16100)
for line in range(x):
 s=f.readline()

print s,"fv"
s=s.lower()
s=s.replace('\n','')
filmtup=list(s)
for i in filmtup:
 if(i==' '):
  ans.append(" ")
 else:
  ans.append('_')


while(count<8):

 inp=raw_input().lower()
 ret=check(inp,filmtup)
 print ret
 if(ret<0):
  print "kill"
  count=count+1
  print count
  pass
 else:
  for i in ret:
   ans[int(i)]=filmtup[int(i)]
  print ans
 if(ans.count('_')>0):
  pass
 else:
  print "win"
  exit(0)
  


