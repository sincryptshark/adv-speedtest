


try:

   import sys
   from os import system,name
   from time import sleep
   import speedtest
   

except Exception as samay:
    _ = system('pip install speedtest-cli')

import os

#colours ------------code's--- 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r
#-----------------------------f

def banner():
    print(y+y+"               ) ")
    print(w+y+"              (( ")
    print(w+y+"              ) \ ")
    print(w+y+"            (   ) ") 
    print(w+y+"            (  )  ) ") 
    print(w+y+"            ) (  ( \ ")
    print(w+y+"          (   )$ )  ) ")
    print(w+y+"          ($$  ( \   )           ")
    print(w+b+"    ^^^^^"+w+g+",r@@@@@@@@@@e,"+w+b+"^^^^^^   ──────────────────────────────────────────────/")
    print(w+b+"      ^^^"+w+g+"@@@@@@@@@@@@@@@@"+w+b+"^^^    "+w+b+"Ping ( Pro ) - version 1.0                   /")
    print(w+g+"      \@@/"+r+",:::,"+w+g+"\/"+r+",:::,"+w+g+"\@@       "+w+"────────────────────────────────────────────/")
    print(w+g+"     /@@@|"+r+":::::"+w+g+"||"+r+":::::"+w+g+"|@@@\\     "+w+"Author : "+y+"Pranshu Pathak  @sincryptshark    /")
    print(w+g+"    / @@@\\"+r+"':::'"+w+g+"/\\"+r+"':::'"+w+g+"/@@@ \\    "+w+"The author is not responsible             /")
    print(w+g+"   /  /@@@@@@@//\\\@@@@@@@\  \\   "+w+"for any issues or damage                 /")
    print(w+g+"  (  /  '@@@@@====@@@@@'  \  )  "+w+"caused by this program                  /")
    print(w+g+"   \(     /          \     )/ "+"\033[1;33m  ───────────────────────────────────────/")
    print(w+g+"     \   (            )   /")
    print(w+g+"          \          /"+w)


def clearfun():
    system('cls' if name=='nt' else 'clear')
def optionsfunc():
    print(r+"└─"+w+"\033[1;37m[ 1 ] Download Speed : ")
    print(r+"└─"+w+"\033[1;37m[ 2 ] Upload Speed : ")
    print(r+"└─"+w+"\033[1;37m[ 3 ] Exit : ")

clearfun()
banner()
print('\n')
optionsfunc()
print('\n')
class Samay:
    def __init__(self,self_user):
        self.user = self_user
    def functions(self):
        self.yam_guru = speedtest.Speedtest()
        if self.user==1:
           print(r+"└─"+w+"\033[1;37mPlease Wait..")
           print('\n')
           print(r+"└─"+w+f"\033[1;37mYour Download Speed is "+r+f"{self.yam_guru.download()}")
           print('\n')
           e = input(r+"└─"+w+"\033[1;37mTest Again [y/n] : "+r)
           if e=='y' or e=='Y':
               clearfun()
               banner()
               print('\n')
               fg = True
               i = Samay(fg)
               i.functions()

           else:
               os.system('python main.py')


       
        elif self.user ==2:
            print('\n')
            print(r+"└─"+w+f"\033[1;37mYour Upload Speed is "+r+f"{self.yam_guru.upload()}")
            print('\n')

        else:
            print('\n')
            print(r+"└─"+w+"\033[1;37mExiting ...")
            print('\n')
            sys.exit()
       

try:
    user_input = int(input(r+"└─"+w+"\033[1;37mEnter the Desire Option : "+r))
except:
    sys.exit()

samay = Samay(user_input)
samay.functions()
