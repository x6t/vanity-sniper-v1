import requests
import os
import threading
from colorama import Fore
import time
r1 = Fore.RED
g = Fore.GREEN

os.system('title Made By ~ otg dari')
time.sleep(.5)
os.system('title otg Vanity sniper ~ V1.0')
Codes = open('Vanitys.txt', 'r').read().split('\n')
proxies = open('proxies.txt', 'r').read().split('\n')
available = open('Available.txt', 'w')

def vanity():
    for x in Codes:
        r = requests.get(f'https://discord.com/api/v9/invites/{x}',proxies={'http' : 'http://' + 'proxy'})
        if r.status_code == 200:
            print(f'{r1}Vanity Taken | {x}')
        if r.status_code == 404:
            print(f'{g}Vanity Available | {x}')
            available.write(f'{x}\n')
  
thread = threading.Thread(target=vanity)
thread.start()



