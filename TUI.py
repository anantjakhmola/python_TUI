import os
import subprocess
os.system("tput setaf 1")
print("\t\t\t\Het welcome to my TUI for some small tasks")
os.system("tput setaf 7")

print("\t\t\t-----------------------------------------")

print("""Press 1: to see date
Press 2: to check Calendar
Press 3: conf web browser
press 4: to create user
press 5: to start docker server
press 7: to exit 
""")
print("Enter your choice: " , end="")

ch=input()
print(ch)

if int(ch) == 1:
    os.system("date")
elif int(ch) == 2:
    os.system("cal")
elif int(ch) == 3:
    os.system("yum install httpd")
elif int(ch) == 4:
    print("can you give me name for user: ",end="")
    create_user = input()
    os.system("useradd {0}".format(create_user))   ##this is called place holder  or interpolation
elif int(ch) == 5:
    print("gimme name of the server",end="")
    docker_server = input()
    os.system("docker container run -itd --name {0} --network-alias site --network webnet phpser:v1".format(docker_server))
else:
    print("option not found")
