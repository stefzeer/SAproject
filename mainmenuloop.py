import getpass
import os
import subprocess
import sys

import paramiko

print("""
                                     *************************
                                     *       SAproject       *
                                     *************************

     SAproject is a "System Administration python project" for developing a tool for performing various system
     administration tasks on remote hosts. I've created this project for two main purposes - to develop my
     python skills and eventually use the tool to perform some tasks of my daily job as Linux system administrator.

     Contacts : stefzeer90@gmail.com
     ==============================================================================================================
     M A I N - M E N U
     *****************


     1. Run a command on a remote server(s).
     2. IP scanning
     3. Quit
    """)


def main_menu():
    print("""
 M A I N - M E N U
 *****************


 1. Run a command on a remote server(s).
 2. IP Scanning
 3. Quit
 """)


## Get input ###
choice = input('Enter your choice [1-3] : ')

### Convert string to int type ##
choice = int(choice)

### Take action as per selected menu-option ###
if choice == 1:

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    command = input("Enter a command to run on the remote server(s): ")
    username = input("Enter your username: ")
    password = getpass.getpass(prompt='Enter your password: ')

    while True:

        servers = input("Enter the full path of your servers file: ")
        if not os.path.exists(servers):
            print("The provided file does not exist")
            continue

        else:
            break

    with open(servers, 'r') as fp:
        for ip in [line.strip() for line in fp.readlines()]:
            ssh.connect(ip, 22, username, password)
            stdin, stdout, stderr = ssh.exec_command(command)
            print(ip, stdout.readline())
            ssh.close()
        main_menu()

elif choice == 2:

    subnet = input("Enter a subnet to scan (up to the third octet). Example 127.0.0 : ")
    dot = "."
    for ping in range(1, 5):
        address = subnet + dot + str(ping)
        res = subprocess.call(['ping', '-c', '3', address], stdout=open(os.devnull, 'wb'))
        if res == 0:
            print("ping to", address, "OK!")
        elif res == 2:
            print("no response from", address)
        else:
            print("ping to", address, "FAILED!")

    main_menu()


elif choice == 3:
    sys.exit()
