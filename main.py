import requests
import os
import colorama
from colorama import Fore , Back , Style
colorama.init (autoreset = True)

with open('list.txt','r') as handle:
        list = handle.readlines()
        for x in list:
            listnames = x.rstrip()
            ck= requests.get(f"https://discord.com/api/v9/invites/{listnames}")
            if ck.status_code ==404:
             print(f"{Fore.GREEN} {listnames} Vaild")
             with open("vaild.txt","a+") as file:
              file.write(listnames)
              file.write("\n")
              Vaild =+ 1
              
            else:
             print(f"{Fore.RED} {listnames} invaild")
             with open("invaild.txt","a+") as file:
              file.write(listnames)
              file.write("\n")
              invaild =+ 1


              

