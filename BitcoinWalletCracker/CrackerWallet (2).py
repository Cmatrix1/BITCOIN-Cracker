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
if (platform.uname()[0]) == "Windows":
    init()
if (platform.uname()[0]) == "Linux":
    True

try:
    from requests import ConnectionError
    import requests
except ModuleNotFoundError:
    PackageInstaller("requests")

try:
    from bitcoinaddress import Wallet
except ModuleNotFoundError:
    PackageInstaller("bitcoinaddress")


cw = "\033[0;m"
cwh = "\033[29;1m"
cg = "\033[32;1m"
cy = "\033[33;1m"
cb = "\033[34;1m"
cc = "\033[36;1m"
cm = "\033[35;1m"


class WalletCracker:
    def __init__(self, modes, formats, out_file):
        self.modes = modes
        self.formats = formats
        self.out_file = out_file

    def __WalletGenerator__(self):
         HashData = HashCypher()
         HashGen = HashData.HashGenerator()
         PBK_BASE58 = HashGen["PublicKey"]
         PVK = HashGen["PrivateKey"]
         return {"BASE58_PUBLIC_KEY" : PBK_BASE58, "PRIVATE_KEY" : PVK}
    
    def __BalanceCheck__(self, PUBLICK_KEY):
        URL = "https://www.blockonomics.co/api/balance"
        api_key_list = ["ej5GLbuzQezYLz8qmRovvnO5IMRDbLYdhbb0aWLVTuw", "RRVYcLM1gXYEOcS7B1uqzRwvcjyoy3xtbnmcZnCRfnQ", "bVH9WgZw7HlZP9GanvFzDH1L90KImjAsieA3vZ5RsAg"]
        api_key = random.choice(api_key_list)
        data_rest = {"addr": PUBLICK_KEY}
        data_rest = json.dumps(data_rest)
        header = {"Authorization": (f"Bearer {api_key}")}
        try:
            response = requests.post(URL, headers=header, data=data_rest)
        except ConnectionError:
            try:
                response = requests.post(URL, headers=header, data=data_rest)
            except ConnectionError:
                try:
                    response = requests.post(URL, headers=header, data=data_rest)
                except ConnectionError:
                    try:
                        response = requests.post(URL, headers=header, data=data_rest)
                    except ConnectionError:
                        return {"SUCCESS" : False, "BALANCE" : None}
                    else:
                        time.sleep(1)
                        response = response.json()
                        response = response["response"][0]["confirmed"]
                        return {"SUCCESS" : True, "BALANCE" : response}
                else:
                    time.sleep(1)
                    response = response.json()
                    response = response["response"][0]["confirmed"]
                    return {"SUCCESS" : True, "BALANCE" : response}
            else:
                time.sleep(1)
                response = response.json()
                response = response["response"][0]["confirmed"]
                return {"SUCCESS" : True, "BALANCE" : response}
        else:
            time.sleep(1)
            response = response.json()
            response = response["response"][0]["confirmed"]
            return {"SUCCESS" : True, "BALANCE" : response}
    
    def __GenerateBech32Address__(self, PRIVATE_KEY):
        wl = Wallet(PRIVATE_KEY)
        wl = wl.address.__dict__['mainnet'].__dict__
        wl = wl["pubaddrbc1_P2WPKH"]
        return {"BECH32_PUBLIC_KEY" : wl}

    def __Printer__(self, modes, formats):
        if modes == 1:
            if formats == 1:
                now_time = datetime.datetime.now().strftime("%H : %M : %S")
                prvk = self.private_key
                pbk_base58 = self.publick_key_base58
                blc = self.balance_base58
                print(f"\n{cc}============================================{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Private Key{cw}{cwh} : {cw}{cy}{prvk}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Public Key (Base58){cw}{cwh} : {cw}{cy}{pbk_base58}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Balance{cw}{cwh} : {cw}{cy}{blc}{cw}")
                print(f"{cc}============================================{cw}")
            if formats == 2:
                now_time = datetime.datetime.now().strftime("%H : %M : %S")
                prvk = self.private_key
                pbk_bech32 = self.publick_key_bech32
                blc = self.balance_bech32
                print(f"\n{cc}============================================{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Private Key{cw}{cwh} : {cw}{cy}{prvk}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Public Key (Bech32){cw}{cwh} : {cw}{cy}{pbk_bech32}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Balance{cw}{cwh} : {cw}{cy}{blc}{cw}")
                print(f"{cc}============================================{cw}")
            if formats == 3:
                now_time = datetime.datetime.now().strftime("%H : %M : %S")
                prvk = self.private_key
                pbk_base58 = self.publick_key_base58
                pbk_bech32 = self.publick_key_bech32
                blc_base58 = self.balance_base58
                blc_bech32 = self.balance_bech32
                print(f"\n{cc}============================================{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Private Key{cw}{cwh} : {cw}{cy}{prvk}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Public Key (Base58){cw}{cwh} : {cw}{cy}{pbk_base58}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Balance (Base58){cw}{cwh} : {cw}{cy}{blc_base58}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Public Key (Bech32){cw}{cwh} : {cw}{cy}{pbk_bech32}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Balance (Bech32){cw}{cwh} : {cw}{cy}{blc_bech32}{cw}")
                print(f"{cc}============================================{cw}")
        if modes == 2:
            if formats == 1:
                now_time = datetime.datetime.now().strftime("%H : %M : %S")
                prvk = self.private_key
                check_res = self.checked_base58
                print(f"\n{cc}============================================{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Private Key (Base58){cw}{cwh} : {cw}{cy}{prvk}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Checked{cw}{cwh} : {cw}{cy}{check_res}{cw}")
                print(f"{cc}============================================{cw}")
            if formats == 2:
                now_time = datetime.datetime.now().strftime("%H : %M : %S")
                prvk = self.private_key
                check_res = self.checked_bech32
                print(f"\n{cc}============================================{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Private Key (Bech32){cw}{cwh} : {cw}{cy}{prvk}{cw}")
                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Checked{cw}{cwh} : {cw}{cy}{check_res}{cw}")
                print(f"{cc}============================================{cw}")
    
    def __CrackerMachine__(self, target_wallet=""):
        mode = self.modes
        format_crack = self.formats
        if mode == 1:
            if format_crack == 1:
                data_wallet = self.__WalletGenerator__()
                PVK = data_wallet["PRIVATE_KEY"]
                PBK = data_wallet["BASE58_PUBLIC_KEY"]
                Balance = self.__BalanceCheck__(PBK)
                if Balance["SUCCESS"] == False:
                    Balance = self.__BalanceCheck__(PBK)
                    if Balance["SUCCESS"] == False:
                        print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                        return {"Balance" : False}

                    if Balance["SUCCESS"] == True:
                        self.private_key = PVK
                        self.publick_key_base58 = PBK
                        self.balance_base58 = Balance["BALANCE"]
                        self.__Printer__(mode, format_crack)
                        return {"Balance" : True, "BalanceBase58" : Balance["BALANCE"], "PublicKeyBase58" : PBK, "PrivateKey" : PVK}
                
                if Balance["SUCCESS"] == True:
                    self.private_key = PVK
                    self.publick_key_base58 = PBK
                    self.balance_base58 = Balance["BALANCE"]
                    self.__Printer__(mode, format_crack)
                    return {"Balance" : True, "BalanceBase58" : Balance["BALANCE"], "PublicKeyBase58" : PBK, "PrivateKey" : PVK}
            if format_crack == 2:
                data_wallet = self.__WalletGenerator__()
                PVK = data_wallet["PRIVATE_KEY"]
                PBK = self.__GenerateBech32Address__(PVK)
                PBK = PBK["BECH32_PUBLIC_KEY"]
                Balance = self.__BalanceCheck__(PBK)
                if Balance["SUCCESS"] == False:
                    Balance = self.__BalanceCheck__(PBK)
                    if Balance["SUCCESS"] == False:
                        print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                        return {"Balance" : False}
                    if Balance["SUCCESS"] == True:
                        self.private_key = PVK
                        self.publick_key_bech32 = PBK
                        self.balance_bech32 = Balance["BALANCE"]
                        self.__Printer__(mode, format_crack)
                        return {"Balance" : True, "BalanceBech32" : Balance["BALANCE"], "PublicKeyBech32" : PBK, "PrivateKey" : PVK}
                if Balance["SUCCESS"] == True:
                    self.private_key = PVK
                    self.publick_key_bech32 = PBK
                    self.balance_bech32 = Balance["BALANCE"]
                    self.__Printer__(mode, format_crack)
                    return {"Balance" : True, "BalanceBech32" : Balance["BALANCE"], "PublicKeyBech32" : PBK, "PrivateKey" : PVK}
            if format_crack == 3:
                data_wallet = self.__WalletGenerator__()
                PVK = data_wallet["PRIVATE_KEY"]
                PBK_Base58 = data_wallet["BASE58_PUBLIC_KEY"]
                PBK_Bech32 = self.__GenerateBech32Address__(PVK)
                PBK_Bech32 = PBK_Bech32["BECH32_PUBLIC_KEY"]
                Balance_Base58 = self.__BalanceCheck__(PBK_Base58)
                if Balance_Base58["SUCCESS"] == True:
                    Balance_Bech32 = self.__BalanceCheck__(PBK_Bech32)
                    if Balance_Bech32["SUCCESS"] == True:
                        self.private_key = PVK
                        self.publick_key_base58 = PBK_Base58
                        self.publick_key_bech32 = PBK_Bech32
                        self.balance_base58 = Balance_Base58["BALANCE"]
                        self.balance_bech32 = Balance_Bech32["BALANCE"]
                        self.__Printer__(mode, format_crack)
                        return {"Balance" : True, "BalanceBase58" : Balance_Base58["BALANCE"], "BalanceBech32" : Balance_Bech32["BALANCE"], "PublicKeyBase58" : PBK_Base58, "PublicKeyBech32" : PBK_Bech32, "PrivateKey" : PVK}
                    if Balance_Bech32["SUCCESS"] == False:
                        print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                        return {"Balance" : False}
                if Balance_Base58["SUCCESS"] == False:
                    print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                    return {"Balance" : False}
        if mode == 2:
            if format_crack == 1:
                data_wallet = self.__WalletGenerator__()
                PVK = data_wallet["PRIVATE_KEY"]
                PBK = data_wallet["BASE58_PUBLIC_KEY"]
                if PBK == target_wallet:
                    self.private_key = PVK
                    self.checked_base58 = "True"
                    self.__Printer__(mode, format_crack)
                    return {"CheckResponse" : True, "PrivateKey" : PVK}
                if PBK != target_wallet:
                    self.private_key = PVK
                    self.checked_base58 = "False"
                    self.__Printer__(mode, format_crack)
                    return {"CheckResponse" : False}
            if format_crack == 2:
                data_wallet = self.__WalletGenerator__()
                PVK = data_wallet["PRIVATE_KEY"]
                PBK = self.__GenerateBech32Address__(PVK)
                PBK = PBK["BECH32_PUBLIC_KEY"]
                if PBK == target_wallet:
                    self.private_key = PVK
                    self.checked_bech32 = "True"
                    self.__Printer__(mode, format_crack)
                    return {"CheckResponse" : True, "PrivateKey" : PVK}
                if PBK != target_wallet:
                    self.private_key = PVK
                    self.checked_bech32 = "False"
                    self.__Printer__(mode, format_crack)
                    return {"CheckResponse" : False}
    
    def Cracker(self, tgwl=""):
        out_file = self.out_file
        if self.modes == 1:
            if self.formats == 1:
                res_crack = self.__CrackerMachine__()
                if res_crack["Balance"] == True:
                    balance = res_crack["BalanceBase58"]
                    if balance != 0:
                        pubkey = res_crack["PublicKeyBase58"]
                        prvkey = res_crack["PrivateKey"]
                        with open(out_file, "a") as f:
                            f.write("\n")
                            f.write(f"Wallet(Base58-P2PKH) : {pubkey} | PrivateKey : {prvkey} | Balance : {balance}")
                return {"Mode" : 1}
            if self.formats == 2:
                res_crack = self.__CrackerMachine__()
                if res_crack["Balance"] == True:
                    balance = res_crack["BalanceBech32"]
                    if balance != 0:
                        pubkey = res_crack["PublicKeyBech32"]
                        prvkey = res_crack["PrivateKey"]
                        with open(out_file, "a") as f:
                            f.write("\n")
                            f.write(f"Wallet(Bech32-P2WPKH) : {pubkey} | PrivateKey : {prvkey} | Balance : {balance}")
                return {"Mode" : 1}
            if self.formats == 3:
                res_crack = self.__CrackerMachine__()
                if res_crack["Balance"] == True:
                    balance_base58 = res_crack["BalanceBase58"]
                    balance_bech32 = res_crack["BalanceBech32"]
                    if balance_base58 != 0:
                        if balance_bech32 != 0:
                            pubkey_base58 = res_crack["PublicKeyBase58"]
                            pubkey_bech32 = res_crack["PublicKeyBech32"]
                            prvkey = res_crack["PrivateKey"]
                            with open(out_file, "a") as f:
                                f.write("\n")
                                f.write(f"Wallet(Base58-P2PKH) : {pubkey_base58} | Wallet(Bech32-P2WPKH) : {pubkey_bech32} | PrivateKey : {prvkey} | Balance (Base58-P2PKH) : {balance_base58} | Balance (Bech32-P2WPKH) : {balance_bech32}")
                return {"Mode" : 1}
        if self.modes == 2:
            if self.formats == 1:
                res_crack = self.__CrackerMachine__(tgwl)
                if res_crack["CheckResponse"] == True:
                    with open(out_file, "a") as f:
                        f.write("\n")
                        f.write(res_crack["PrivateKey"])
                    return {"Mode" : 2, "Res" : True}
                if res_crack["CheckResponse"] == False:
                    return {"Mode" : 2, "Res" : False}
            if self.formats == 2:
                res_crack = self.__CrackerMachine__(tgwl)
                if res_crack["CheckResponse"] == True:
                    with open(out_file, "a") as f:
                        f.write("\n")
                        f.write(res_crack["PrivateKey"])
                    return {"Mode" : 2, "Res" : True}
                if res_crack["CheckResponse"] == False:
                    return {"Mode" : 2, "Res" : False}


if (platform.uname()[0]) == "Windows":
    os.system("cls")
if (platform.uname()[0]) == "Linux":
    os.system("clear")

print(f"""

               {cwh}Choose Your One :

               {cwh}1{cy}. {cb}Generating Wallet And Checking Balance .{cw}

               {cwh}2{cy}. {cg}Cracking Private Key . {cw}""")

mode_inp = input(f"\n  {cm}What's Your Number {cw}{cwh}(1 or 2) {cm}? {cw}")
num_list = [1,2]
try:
    mode_inp = int(mode_inp)
    num_list.index(mode_inp)
except ValueError:
    if (platform.uname()[0]) == "Windows":
        os.system("cls")
    if (platform.uname()[0]) == "Linux":
        os.system("clear")
    print("Please Try Again !!!")
    time.sleep(3)
    os._exit(1)
else:
    if mode_inp == 1:
        if (platform.uname()[0]) == "Windows":
            os.system("cls")
        if (platform.uname()[0]) == "Linux":
            os.system("clear")
        print(f"""

               {cwh}Choose Your Wallet Format For Generate :

               {cwh}1{cy}. {cg}Generating [Base58(P2PKH)] Wallet And Checking Balance .{cw}

               {cwh}2{cy}. {cg}Generating [Bech32(P2WPKH)] Wallet And Checking Balance .{cw}
               
               {cwh}3{cy}. {cg}Generating [Base58(P2PKH)] And [Bech32(P2WPKH)] Wallet And Checking Balance .{cw}""")
        format_inp = input(f"\n  {cm}What's Your Number {cw}{cwh}(1 or 2 or 3) {cm}? {cw}")
        num_list = [1, 2, 3]
        try:
            format_inp = int(format_inp)
            num_list.index(format_inp)
        except ValueError:
            if (platform.uname()[0]) == "Windows":
                os.system("cls")
            if (platform.uname()[0]) == "Linux":
                os.system("clear")
            print("Please Try Again !!!")
            time.sleep(3)
            os._exit(1)
        else:
            try:
                range_inp = int(input(f"  {cwh}Range For Generating : {cw}"))
            except ValueError:
                if (platform.uname()[0]) == "Windows":
                    os.system("cls")
                if (platform.uname()[0]) == "Linux":
                    os.system("clear")
                print("Please Try Again !!!")
                time.sleep(3)
                os._exit(1)
            else:
                out_file_inp = input(f"  {cwh}Your Output File Name : {cw}")
                out_file_inp = out_file_inp + ".txt"
                open(out_file_inp, "w").close()

    if mode_inp == 2:
        if (platform.uname()[0]) == "Windows":
            os.system("cls")
        if (platform.uname()[0]) == "Linux":
            os.system("clear")
        print(f"""

               {cwh}Choose Your Wallet Format For Crack :

               {cwh}1{cy}. {cg}Crack [Base58(P2PKH)] Wallet .{cw}

               {cwh}2{cy}. {cg}Crack [Bech32(P2WPKH)] Wallet .{cw}""")
        format_inp = input(f"\n  {cm}What's Your Number {cw}{cwh}(1 or 2) {cm}? {cw}")
        num_list = [1, 2]
        try:
            format_inp = int(format_inp)
            num_list.index(format_inp)
        except ValueError:
            if (platform.uname()[0]) == "Windows":
                os.system("cls")
            if (platform.uname()[0]) == "Linux":
                os.system("clear")
            print("Please Try Again !!!")
            time.sleep(3)
            os._exit(1)
        else:
            try:
                range_inp = int(input(f"  {cwh}Range For Generating : {cw}"))
            except ValueError:
                if (platform.uname()[0]) == "Windows":
                    os.system("cls")
                if (platform.uname()[0]) == "Linux":
                    os.system("clear")
                print("Please Try Again !!!")
                time.sleep(3)
                os._exit(1)
            else:
                if format_inp == 1:
                    wallet_inp = input(f"  {cwh}Your Base58(P2PKH) Wallet For Crack : {cw}")
                if format_inp == 2:
                    wallet_inp = input(f"  {cwh}Your Bech32(P2WPKH) Wallet For Crack : {cw}")
                out_file_inp = input(f"  {cwh}Your Output File Name : {cw}")
                out_file_inp = out_file_inp + ".txt"
                open(out_file_inp, "w").close()

wlcr = WalletCracker(mode_inp, format_inp, out_file_inp)
for i in range(range_inp):
    if mode_inp == 1:
        res_cr = wlcr.Cracker()
    if mode_inp == 2:
        res_cr = wlcr.Cracker(wallet_inp)
        if res_cr["Res"] == True:
            break
