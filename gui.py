import pygame,sys
import pygame.locals
from time import sleep

def updatimage(count):
 dicts={0:"hangman8.jpg",1:"hangman7.jpg",2:"hangman6.jpg",3:"hangman5.jpg",4:"hangman4.jpg",5:"hangman3.jpg",6:"hangman2.jpg",7:"hangman1.jpg",8:"hangman.jpg",}
 return pygame.image.load(dicts[count])

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
size = (800,600)
pygame.init()
l=pygame.image.load('hangman.jpg')
lo=pygame.image.load('hangman-1.jpg')
from random import randint
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))

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
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))








while (1):
 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   exit(0)
 user=raw_input().lower()
 res=checkme(user,name)
 
 if(res==-1):
 #kill
  screen.blit(updatimage(count),(0,0))
  count=count+1
  pygame.display.update()
 else:
  for i in res:
   ans[i]=user

 print ans
 if(count>=9):
   
  print "killed","\n",copy
  while(1):
   screen.blit(pygame.image.load("hangman.jpg"),(0,0))
   pygame.display.update()
   sleep(0.5)
   screen.fill((255,255,255))
   screen.blit(pygame.image.load("hangman-1.jpg"),(0,0))
   pygame.display.update()
   sleep(0.5)
  
 elif(not(ans.count('_'))):
  print "Success","\n",copy

 
 
 pygame.display.update()

 
