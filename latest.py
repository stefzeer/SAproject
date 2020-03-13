import paramiko
import os
import getpass

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
command=input("Enter a command to run on the remote server(s): ")
username=input("Enter your username: ")
password=getpass.getpass(prompt= 'Enter your password: ')

while True:

   servers=input("Enter the full path of your servers file: ")
   if not os.path.exists(servers):
       print("The provided file does not exist")
       continue

   else:
    break

with open(servers, 'r') as fp:
     for ip in [line.strip() for line in fp.readlines()]:
        ssh.connect(ip, 22, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        print (ip, stdout.readline())
        ssh.close()

input()
