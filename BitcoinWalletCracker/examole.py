from BitcoinWalletScraper import HashCypher
import datetime
import functools





def make_hash():
    HashData = HashCypher()
    HashGen = HashData.HashGenerator()
    return HashGen

def make2_hash():
    HashData = HashCypher()
    HashGen = HashData.HashGenerator()
    return HashGen 


wallets = ["1GNgwA8JfG7Kc8akJ8opdNWJUihqUztfPe"]
def read_wallet():
    cnt_find = 4
    
    target_wl = list(map(lambda x: x[:cnt_find], wallets))
    yield target_wl[0]

def crack_hash(target_wallets, HashGen):
    cnt_find = 4
    private_key = HashGen["PrivateKey"]
    publick_key = "1GNgwA8JfG7Kc8akJ8opdNWJUihqUztfPe"
    yield publick_key[:cnt_find]

    # if publick_key[:cnt_find] in target_wl:
    #     print("find wallet", private_key, publick_key)
        
    # else:
    #     print(publick_key[:cnt_find], target_wl)

# while True:
#     # crack_hash(wallets, make2_hash())
#     print(crack_hash(wallets, make2_hash()), read_wallet())
#     if next(crack_hash(wallets, make2_hash())) in next(read_wallet()):
#         print("find")
#         break
#     else:
#         print("not found")

def s():
    yield 2668546

def a():
    yield 2

print(s(), a())
# while True:

#     old = datetime.datetime.now()
#     w = next(make2_hash())

#     # print(w)

#     print(datetime.datetime.now())