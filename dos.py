import pyfiglet
import time
import os

from datetime import datetime
now = datetime.now()



hour = now.hour
second = now.second
minite = now.minute


x = 0
time.sleep(5)
print ("[========= ]80%")

time.sleep(3)
print("[========== ]85%")

time.sleep(3)
print(("[=========== ]90%"))

time.sleep(3)
print("[========== ]95%")

time.sleep(2)
print("[================]100%")

#time.sleep(1)



print("\n")

print(pyfiglet.figlet_format("Ddos Tool"))

print

art = '''

           ___           _,.---,---.,_
            |         ,;~'             '~;, 
            |       ,;                     ;,      
   Frontal  |      ;                         ; ,--- Raj Rahman
    Bone    |     ,'                         /'
            |    ,;                        /' ;,
            |    ; ;      .           . <-'  ; |
            |__  | ;   ______       ______   ;<----- Ddos Powerfull Tool
           ___   |  '/~"     ~" . "~     "~\'  |
           |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 Maxilla,  |      |   |        }:{        | <------ Orbit
Nasal and  |      |   l       / | \       !   |
Zygomatic  |      .~  (__,.--" .^. "--.,__)  ~. 
  Bones    |      |    ----;' / | \ `;-<--------- Infraorbital Foramen
           |__     \__.       \/^\/       .__/  
              ___   V| \                 / |V <--- Mastoid Process 
              |      | |T~\___!___!___/~T| |  
              |      | |`IIII_I_I_I_IIII'| |  
     Mandible |      |  \,III I I I III,/  | 
              |       \   `~~~~~~~~~~'    /
              |         \   .       . <-x---- Mental Foramen
              |__         \.    ^    ./   
                            ^~~~^~~~^



'''
print(art)

print("-------------(-_-)-----------------")
#print("|                                 |")
print("|Another   :  Raj Rahman(Hunter)  |")
print("|Youtube   :  www.youtube.com     |")
print("|Facebook  :  www.facebook.com    |")
print("|Google    :  www.google.com      |")
print("-------------(The End)-------------")
print

ip = input("Ip Address: ")
port = input("Port: " )

print("\n")
print("------(Your Details)--------")
print("\tEnter Your Ip",ip)
print("\tEnter Your Port",port)

a = ip,port


#



for x in a:
    for y in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
     m = ("Sent to {} packet to {} throught port: {}")
     print(m.format(y,ip,port))
