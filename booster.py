from requests import get
from os import system
system("color 9")
r = """ ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗     ██████╗  ██████╗  ██████╗ ███████╗████████╗
██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝
██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██████╔╝██║   ██║██║   ██║███████╗   ██║   
██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██╔══██╗██║   ██║██║   ██║╚════██║   ██║   
╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   """
print("\n\n" + r)
print("                                  Made by Toto'#1337 <3 \n")
i = int(input("Nombre de vues que tu souhaites : "))
n = 0
github_username = str(input("Github pseudo : "))
while n<i:
    n += 1
    print(f"Nombre de vues envoyées ", n)
    get(f'https://profile-counter.glitch.me/{github_username}/count.svg') 
