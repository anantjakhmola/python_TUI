import os
import subprocess
os.system("tput setaf 1")
print("\t\t\t Hi welcome to my TUI for some small tasks")
os.system("tput setaf 7")

print("\t\t\t-----------------------------------------")
print("which machine you want to use local/remote: ",end="")
location = input()
print(location)
if location == "remote":
    remoteIp = input("Enter ur Ip: ")
while True:
    print("""
    Press 1: to see date
    Press 2: to check Calendar
    Press 3: conf web browser
    press 4: to create user
    press 5: to start docker server with a site hosted
    print 6: to install a package
    print 7: to check about server?
    press 8: to exit 
    """)
    print("Enter your choice: " , end="")
    ch=input()
    print(ch)

    if location == "local":
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
        elif int(ch) == 6:
            os.system("write a package name lets see if its available: ", end="")
            pack_name = input()
            os.system("dnf install {0}".format(pack_name))
        elif int(ch) == 7:
            os.system("systemctl restart httpd")
        elif int(ch) == 8:
            exit()
        else:
            print("option not found")
        os.system(input("Press Enter to continue........"))
        os.system("clear")
    elif location == "remote":
        if int(ch) == 1:
            os.system("ssh {0} date".format(remoteIp))
        elif int(ch) == 2:
            os.system("ssh {0} cal".format(remoteIp))
        elif int(ch) == 3:
            os.system("ssh {0} yum install httpd".format(remoteIp))
        elif int(ch) == 4:
            print("can you give me name for user: ",end="")
            create_user = input()
            os.system("ssh {0} useradd {1}".format(remoteIp,create_user))   ##this is called place holder  or interpolation
        elif int(ch) == 5:
            print("gimme name of the server",end="")
            docker_server = input()
            os.system("ssh {0} docker container run -itd --name {1} --network-alias site --network webnet phpser:v1".format(remoteIp,docker_server))
        elif int(ch) == 6:
            os.system("write a package name lets see if its available: ", end="")
            pack_name = input()
            os.system("ssh {0} dnf install {1}".format(remoteIp,pack_name))
        elif int(ch) == 7:
            os.system("ssh {0}systemctl restart httpd".format(remoteIp))
        elif int(ch) == 8:
            exit()
        else:
            print("option not found")
            
    else:
        print("sorry wrong input")
        
