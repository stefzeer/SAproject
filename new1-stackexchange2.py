import paramiko
import os

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
command=input("Enter a command to run on the remote server(s): ")
servers=input("Enter the path of your file: ")
if os.path.exists(servers):

 with open(servers, 'r') as fp:
    for ip in [line.strip() for line in fp.readlines()]:
        ssh.connect(ip, 22, "root", "Stefan9010")
        stdin, stdout, stderr = ssh.exec_command(command)
        print (ip, stdout.readline())
        ssh.close()

else:
    print("The file does not exist")
