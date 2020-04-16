import os

os.system("rpm -i epel-release-latest-8.noarch.rpm")
os.system("touch /etc/yum.repos.d/docker.repo")
file = open("/etc/yum.repos.d/docker.repo","w")
file.write(""" 
[docker]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
""")
file.close()
os.system("yum update")
os.system("yum install docker-ce --nobest")