import time
import random
launch = ""
x = random.randint(1,100)



Rocketname = raw_input("what is the Rocket called: ")

print( Rocketname + " mission setup")
destination = raw_input("what is the destination: ")
launchTime = raw_input("what is the launch time: ")
missionName = raw_input("what is the mission name: ")
payload = raw_input("what is the payload: ")
launchSite = raw_input("what is the launch site: ")
payloaddestination = raw_input("what is the payload destination: ")

while not launch == 'y':
  launch = raw_input("ready for launch? (y/n) ")
  time.sleep(2.5)


print(" Starting " + Rocketname +  missionName + " launch sequence ")
if x <= 10:
  print("Rocket exploded")
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

