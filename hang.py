from random import randint

def checkme(num,filmname):
  ret=[]
  print filmname.count(num)
  if(filmname.count(num)>0):
   for i,n in enumerate(filmname):
    if(n==num):
     ret.append(i)  
  
   return ret
  else:
   return -1
ans=[]
randnum= randint(1,16000)
f=open('film.txt','r')
for i in range(randnum):
 f.readline()

name=f.readline()
copy=name
f.close()
name=name.replace('\n','').lower()
name= list(name)


for item in name:
 if(not(item==" ")):
  
  ans.append('_')
 else:
  ans.append(" ")

count=0
while(count<9):
 user=raw_input().lower()
 res=checkme(user,name)
 
 if(res==-1):
 #kill
  count=count+1
 
 else:
  for i in res:
   ans[i]=user

 print ans
 if(count>=9):
  print 
  print "killed","\n",copy
  exit(0)
 elif(not(ans.count('_'))):
  print "Success","\n",copy



