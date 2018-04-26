#!/usr/bin/python

launch = ""

print("Super Nova mission setup")
destination = raw_input("what is the destination: ")
launchTime = raw_input("what is the launch time: ")
missionName = raw_input("what is the mission name: ")
payload = raw_input("what is the payload: ")
launchSite = raw_input("what is the launch site: ")

while not launch == 'y':
  launch = raw_input("ready for launch? (y/n) ")



print("Starting Super Nova " + missionName +" launch sequence ")
print("destination is " + destination )
print("launchTime is " + launchTime)
print("missionName is " + missionName)
print("payload is " + payload)
print("launchSite is " + launchSite    )

