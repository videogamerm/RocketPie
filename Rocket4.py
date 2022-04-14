import time
import random

from colored import *
launch = ""
color = fg('chartreuse_1')
color1 = fg('red_3a')
res = attr('reset')
x = random.randint(1,10)
print(color+"Super Nova mission setup")
destination = input(color+"what is the destination: ")
launchTime = input(color+"what is the launch time: ")
missionName = input(color+"what is the mission name: ")
payload = input(color+"what is the payload: ")
launchSite = input(color+"what is the launch site: ")
payloaddestination = input(color+"what is the payload destination: ")
while not launch == 'y':
  launch = input(color+"ready for launch? (y/n) ")
  time.sleep(2.5)


print(color+"Starting Super Nova " + missionName +" launch sequence ")
if x == 1:
  print(color1+"Rocket exploded")
else:
  print("destination is " + destination )
  print("launchTime is " + launchTime)
  print("missionName is " + missionName)
  print("payload is " + payload)
  print("launchSite is " + launchSite    )
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  print("liftoff")
  time.sleep(5)
  print("reached "+ destination ) 
  print( payload +" got to "  + payloaddestination   )
