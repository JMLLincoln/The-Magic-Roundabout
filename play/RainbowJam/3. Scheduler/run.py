import os
import sys
import subprocess
from datetime import datetime

timeList = {
    "11:15" : "Chrome",
    "12:10" : "lol.launcher",
    "12:15" : "Notepad",
    "12:30" : "GitHub",
    "13:00" : "Spotify"
    }
completedList = []

currentTime = datetime.now().strftime("%H:%M")
future = False
for time in timeList:
    if time > currentTime:
        future = True

if future == False:
    print ("Warning: All scheduled applications will not open today,")
    print ("         The selected times are in the past.")
    
# For manual input use:
# "exe_name" : "path_to_exe"
# Make sure to add a path for each application
pathList = {}

def find_exes():
    exes = []
    for time in timeList:
        exes.append("%s.exe" % timeList[time].lower())
        
    for root, dirs, files in os.walk(r'C:\\'):
        if exes != []:
            for name in files:
                name = name.lower()
                if name in exes:
                    item = name.replace(".exe", "")
                    path = os.path.abspath(os.path.join(root, name))
                    pathList[item] = path
                    exes.remove(name)
                    print("\nFile: %s.exe\nPath: '%s'" % (item, path))
        else:
            break

if not bool(pathList):
    print("\nFinding paths...")
    find_exes()

running = True
print("\nRunning...")
while running:
    currentTime = datetime.now().strftime("%H:%M")

    if currentTime in timeList and currentTime not in completedList:
        exe = timeList[currentTime].lower()
        path = pathList[exe]
        
        print ("\nTime:\t '%s'" % currentTime)
        print ("Opening: '%s.exe'" % exe)
        print ("Path:\t '%s'" % path)

        os.system(path)
        completedList.append(currentTime)

    if len(timeList) == len(completedList):
        running = False

print ("Times exhausted")
print ("Closing...")
