from subprocess import *
#
#Node.js is not going to release the port it listens to, so I have to kill it with python
#Biao Chen 2/13/2020

targetPort = "3000"

#command that find all the process PID that are listening to the target port
cmd = "netstat -ano | findstr :" + targetPort
pipe =Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)


#loop through the result return by the console, and store the PIDs to the set
foundProcessesList = set()
while True:
    currentLine = pipe.stdout.readline().decode('utf-8')
    if currentLine:
        foundProcessesList.add(str(currentLine.strip().split(" ")[-1]))
        print("currrent line: " , currentLine)
    else:
        break

#if set is empty, then, there is no process listening to the target port, it is current free
if not len(foundProcessesList):
    print("FAILED: the target port is already FREE!!!")

else:
    for pid in foundProcessesList:
        #sometimes the PID of 0 will show up, since the PID is so small, I don't want to kill it, what if it has something to do
        #with the kernel
        if pid == '0':
            continue
        else:

            #kill the process with the pid
            cmd = "taskkill /F /PID " + pid
            pipe = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
            killResult = pipe.stdout.readline().decode('utf-8')
            print("Process: " , pid + " : ", killResult)




