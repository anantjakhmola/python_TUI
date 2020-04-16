import os
name = input(os.system("whoami"))
os.system("touch /etc/yum.repos.d/base1.repo")
file = open("/etc/yum.repos.d/base1.repo","w")
file.write(""" 
[dvd1]
baseurl=file:///run/media/{0}/RHEL-8-0-0-BaseOS-x86_64/AppStream
gpgcheck=0

[dvd2]
baseurl=file:///run/media/{0}/RHEL-8-0-0-BaseOS-x86_64/BaseOS
gpgcheck=0

""").format(name)
file.close()
os.system("yum update")