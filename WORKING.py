import getpass
import os
import subprocess
import sys
import paramiko


def run_remote():
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
            input("Press any key to continue...")
            main_menu()


def ip_scan():
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
            continue
    input("Press any key to continue...")
    main_menu()


def main_menu():
    print("""
     M A I N - M E N U
     *****************
     1. Run a command on a remote server(s).
     2. IP scanning
     3. Quit
     """)
    global choice
    choice = input('Enter your choice [1-3] : ')
    choice = int(choice)

    if choice == 1:
        run_remote()

    if choice == 2:
        ip_scan()

    elif choice == 3:
        sys.exit()


print("""
                                                                *************************
                                                                *          SAproject            *
                                                                *************************

     SAproject is a "System Administration python project" for developing a tool for performing various system
     administration tasks on remote hosts. I've created this project for two main purposes - to develop my
     python skills and eventually use the tool to perform some tasks of my daily job as Linux system administrator.

     Contacts : stefzeer90@gmail.com
     ============================================================================================================== """)
main_menu()
