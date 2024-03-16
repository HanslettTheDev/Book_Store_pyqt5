import sys
import os
import random
import time

from getmac import get_mac_address

sys.setrecursionlimit(5000)

DIR_PATH = os.getenv('LOCALAPPDATA')
FILE = "yagamie.key"
prr = os.path.join(DIR_PATH, FILE)

def verify(key):
    score = 0

    check_digit = key[2] 
    check_digit_2 = key[8]
    count_1 = 0 
    count_2 = 0

    chunks = key.split("-")
    for chunk in chunks:
        if len(chunk) != 5:
            return False
        
        for char in chunk:
            if char == check_digit:
                count_1 += 1
            if char == check_digit_2:
                count_2 += 1
            score += ord(char) 
            
    if score > 2200 and score < 2300 and count_1 == 4 and count_2 == 2:
        return True
    else:
        return False

def the_key():
    # default credentials
    key = ""
    section = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"

    # Key = aaaaa-bbbbb-ccccc-ddddd-12345 or 25 char
    while len(key) < 30:
        # Randomly pick from the alphabet variable
        char = random.choice(alphabet) # add the random choice to the key
        key += char # add the random choice to the section
        section += char # Add in the dashes and hyphens
        if len(section) == 5:
            key += '-' # add a hyphen
            section = "" # reset the section variable
    # get the key but remove the last digit
    key = key[:-1] 

    if verify(key):
        return key
    else: 
        return the_key()


def get_hardware_id():
    return get_mac_address()


def copy_to_store():
    print("Please wait.....")
    time.sleep(2)
    print(".....")
    time.sleep(2)
    print(".............")
    time.sleep(4)
    print("......................")
    if os.path.isfile(prr):
        print("License already exists for this computer!")
        print("")
        time.sleep(2)
        input("Press any key to exit ")
        return sys.exit(1)
    full_license = str(get_hardware_id() + "+=" + the_key())
    with open(prr, "w") as file:
        file.write(full_license)
        file.close() 

copy_to_store()
print("License successfully generated!")
print("")
time.sleep(2)
input("Press any key to exit ")