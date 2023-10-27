import hashlib
import os
import pyfiglet
from datetime import datetime
from colorama import Fore

#5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def title(args):
    if os.name == "nt":
        if args:
            os.system(f"title SHA256 bruteforcer [~] Made  with love by HannahHaven [~] {args}")
        else:
            os.system("title SHA256 bruteforcer [~] Made with love by HannahHaven")
    else:
        pass



ascii_art = pyfiglet.figlet_format("Hash craacker", font="graffiti")



line_count = 0
cracked = "False"



clear()
title(None)
print(ascii_art)
original_hash = input(f"{Fore.YELLOW}[!]{Fore.RESET} Hashed password: ")
wordlist = input(f"{Fore.YELLOW}[!]{Fore.RESET} Wordlist: ")


with open(wordlist, 'r') as f:
    start = datetime.now()
    file_content = f.read()
    lines = file_content.splitlines()
    for line in lines:
        title_content = "Status: Cracking hash"
        title(title_content)
        line_count += 1
        bytes_line = line.encode('utf-8')
        hashed_line = hashlib.sha256(bytes_line).hexdigest()

        if hashed_line == original_hash:
            clear()
            title_content = "Status: Cracked"
            title(title_content)
            cracked = "True"
            print(pyfiglet.figlet_format("Cracked!", font="graffiti"))
            print(f"{Fore.YELLOW}[!]{Fore.RESET} Cracked by Hannah codes SHA256 cracker\n")
            print("[-]~~~~~~~~~~~~~~~~~~~~~~~[-]\n")
            print(f"{Fore.GREEN}[+]{Fore.RESET} Hash found on line: {line_count}")
            print(f"{Fore.GREEN}[+]{Fore.RESET} Original Hash: {original_hash}")
            print(f"{Fore.GREEN}[+]{Fore.RESET} Cracked hash: {line}")
            print(f"{Fore.GREEN}[+]{Fore.RESET} Cracked in: {datetime.now() - start}")
            print("\n[-]~~~~~~~~~~~~~~~~~~~~~~~[-]")
            input("\nPress enter to exit...")
            break
            
        else:
            pass
    if cracked != "True":
        clear()
        title_content = "Status: Failed to crack"
        title(title_content)
        print(pyfiglet.figlet_format("Failed", font="graffiti"))
        print("[-]~~~~~~~~~~~~~~~~~~~~~~~[-]\n")
        print(f"{Fore.RED}[-]{Fore.RESET} Failed to find hash")
        print(f"{Fore.RED}[-]{Fore.RESET} Original Hash: {original_hash}")
        print(f"{Fore.RED}[-]{Fore.RESET} Cracked hash: NONE")
        print(f"{Fore.RED}[-]{Fore.RESET} Failed to crack in: {datetime.now() - start}")
        print("\n[-]~~~~~~~~~~~~~~~~~~~~~~~[-]")
        input("\nPress enter to exit...")