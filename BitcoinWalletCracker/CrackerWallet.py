from BitcoinWalletScraper import HashCypher
import os
import time
import datetime
import platform
import pip
import sys
import subprocess
import json
import random


def PackageInstaller(PackageName):
    try:
        pip.main(["install",  PackageName])
    except AttributeError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', PackageName])
    os.execl(sys.executable, sys.executable, *sys.argv)


try:
    from colorama import init
except ModuleNotFoundError:
    PackageInstaller("colorama")
init()


try:
    from requests import ConnectionError
    import requests
except ModuleNotFoundError:
    PackageInstaller("requests")


cw = "\033[0;m"
cwh = "\033[29;1m"
cg = "\033[32;1m"
cy = "\033[33;1m"
cb = "\033[34;1m"
cc = "\033[36;1m"
cm = "\033[35;1m"


def clear_scr():

    if (platform.uname()[0]) == "Windows":
        os.system("cls")
    if (platform.uname()[0]) == "Linux":
        os.system("clear")

def error_pr():
    print("Please Try Again !!!")
    time.sleep(3)
    os._exit(1)

def print_Balance_inf(balance):
    now_time = datetime.datetime.now().strftime("%H : %M : %S")
    print(f"\n{cc}============================================{cw}")
    print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Public Key{cw}{cwh} : {cw}{cy}{PBK}{cw}")
    print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Private Key{cw}{cwh} : {cw}{cy}{PVK}{cw}")
    print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Balance{cw}{cwh} : {cw}{cy}{balance}{cw}")
    print(f"{cc}============================================{cw}")

def print_Cracker_inf(stu):
    now_time = datetime.datetime.now().strftime("%H : %M : %S")
    print(f"\n{cc}============================================{cw}")
    print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Private Key{cw}{cwh} : {cw}{cy}{PVK}{cw}")
    print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Checked{cw}{cwh} : {cw}{cy}{stu}{cw}")
    print(f"{cc}============================================{cw}")

def write_file(PBK, PVK, Check_Balance_Res):
    with open(out_file, "a") as f:
        f.write("\n")
        f.write(f"Bitcoin Wallet : {PBK} | Private Key : {PVK} | Balance : {Check_Balance_Res}")


print(f"""

               {cwh}Choose Your One :

               {cwh}1{cy}. {cb}Generating Wallet And Checking Balance .{cw}

               {cwh}2{cy}. {cg}Cracking Private Key . {cw}""")

try:
    ch_num = int(input(f"\n  {cm}What's Your Number {cw}{cwh}(1 or 2) {cm}? {cw}"))
except ValueError:
    clear_scr() 
    error_pr()

else:
    num_list = [1,2]
    try:
        num_list.index(ch_num)
    except ValueError:
        clear_scr()
        error_pr()

    else:
        if ch_num == 1:
            range_gen = input(f"  {cwh}Range For Generating : {cw}")
            try:
                range_gen = int(range_gen)
            except ValueError:
                clear_scr()
                error_pr()

            else:

                out_file = input(f"  {cwh}Output File Name : {cw}")
                out_file = out_file + ".txt"
                open(out_file, "w").close()

                for i in range(range_gen):
                    HashData = HashCypher()
                    HashGen = HashData.HashGenerator()
                    PBK = HashGen["PublicKey"]
                    PVK = HashGen["PrivateKey"]
                    URL = "https://www.blockonomics.co/api/balance"
                    api_key_list = ["ej5GLbuzQezYLz8qmRovvnO5IMRDbLYdhbb0aWLVTuw", "RRVYcLM1gXYEOcS7B1uqzRwvcjyoy3xtbnmcZnCRfnQ", "bVH9WgZw7HlZP9GanvFzDH1L90KImjAsieA3vZ5RsAg"]
                    api_key = random.choice(api_key_list)
                    data_rest = {"addr": PBK}
                    data_rest = json.dumps(data_rest)
                    header = {"Authorization": (f"Bearer {api_key}")}

                    try:
                        Check_Balance_Res = requests.post(URL, headers=header, data=data_rest)
                    except ConnectionError:
                        try:
                            Check_Balance_Res = requests.post(URL, headers=header, data=data_rest)
                        except ConnectionError:
                            try:
                                Check_Balance_Res = requests.post(URL, headers=header, data=data_rest)
                            except ConnectionError:
                                try:
                                    Check_Balance_Res = requests.post(URL, headers=header, data=data_rest)
                                except ConnectionError:
                                    print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                                else:
                                    Check_Balance_Res = Check_Balance_Res.json()
                                    Check_Balance_Res = Check_Balance_Res["response"][0]["confirmed"]

                                    if Check_Balance_Res == 0:
                                        print_Balance_inf("0")

                                    if Check_Balance_Res != 0:
                                        write_file(PBK, PVK, Check_Balance_Res)
                                        print_Balance_inf(Check_Balance_Res)
                            else:
                                Check_Balance_Res = Check_Balance_Res.json()
                                Check_Balance_Res = Check_Balance_Res["response"][0]["confirmed"]

                                if Check_Balance_Res == 0:
                                    print_Balance_inf("0")

                                if Check_Balance_Res != 0:
                                    write_file(PBK, PVK, Check_Balance_Res)
                                    print_Balance_inf(Check_Balance_Res)
                        else:
                            Check_Balance_Res = Check_Balance_Res.json()
                            Check_Balance_Res = Check_Balance_Res["response"][0]["confirmed"]
                            if Check_Balance_Res == 0:
                                print_Balance_inf("0")
                            if Check_Balance_Res != 0:
                                write_file(PBK, PVK, Check_Balance_Res)
                                print_Balance_inf(Check_Balance_Res)
                    else:
                        Check_Balance_Res = Check_Balance_Res.json()
                        Check_Balance_Res = Check_Balance_Res["response"][0]["confirmed"]
                        if Check_Balance_Res == 0:
                            print_Balance_inf("0")
                        if Check_Balance_Res != 0:
                            write_file(PBK, PVK, Check_Balance_Res)
                            pprint_Balance_inf(Check_Balance_Res)
                            
        if ch_num == 2:
            range_check = input(f"  {cwh}Range For Cracking : {cw}")
            try:
                range_check = int(range_check)
            except ValueError:
                clear_scr()
                error_pr()
            else:
                target_wallet = input(f"  {cwh}Your Wallet For Crack : {cw}")
                for i in range(range_check):
                    HashData = HashCypher()
                    HashGen = HashData.HashGenerator()
                    PBK = HashGen["PublicKey"]
                    PVK = HashGen["PrivateKey"]
                    if target_wallet == PBK:
                        print_Cracker_inf("True")
                        break
                    if target_wallet != PBK:
                        print_Cracker_inf("False")