import hashlib
import os


class HashPoints:
    def __init__(self,
        x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
        p=2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1):
        self.x = x
        self.y = y
        self.p = p

    def __add__(self, other):
        return self.__radd__(other)

    def __mul__(self, other):
        return self.__rmul__(other)

    def __rmul__(self, other):
        n = self
        q = None

        for i in range(256):
            if other & (1 << i):
                q = q + n
            n = n + n

        return q

    def __radd__(self, other):
        if other is None:
            return self
        x1 = other.x
        y1 = other.y
        x2 = self.x
        y2 = self.y
        p = self.p

        if self == other:
            l = pow(2 * y2 % p, p-2, p) * (3 * x2 * x2) % p
        else:
            l = pow(x1 - x2, p-2, p) * (y1 - y2) % p

        newX = (l ** 2 - x2 - x1) % p
        newY = (l * x2 - l * newX - y2) % p

        return HashPoints(newX, newY)

    def __ConvertBytes__(self):
        x = self.x.to_bytes(32, "big")
        y = self.y.to_bytes(32, "big")
        return b"\x04" + x + y


class HashCypher:
    
    def __init__(self):
        True
    
    def __SHA256__(self, datas):
        digest_data = hashlib.new("sha256")
        digest_data.update(datas)
        yield digest_data.digest()
    
    def __RIPEMD160__(self, n):
        digest_data = hashlib.new("ripemd160")
        digest_data.update(n)
        yield digest_data.digest()
    
    def __Base58__(self, data):
        B58_data = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        if data[0] == 0:
            yield "1" + next(self.__Base58__(data[1:]))
        x = sum([v * (256 ** i) for i, v in enumerate(data[::-1])])
  
        datas = ""
        while x > 0: 
            datas = B58_data[x % 58] + datas
            x = x // 58
    
        yield datas

    def __PublicKeyGenerator__(self, PrivateKey):
        SPEC256k1 = HashPoints()
        pk = int.from_bytes(PrivateKey, "big")
        hash160 = next(self.__RIPEMD160__(next(self.__SHA256__((SPEC256k1 * pk).__ConvertBytes__()))))
        address = b"\x00" + hash160
    
        address = next(self.__Base58__(address + next(self.__SHA256__(next(self.__SHA256__(address))))[:4]))
        yield address
    
    def __PrivateKeyWIFGenerator__(self, PrivateKey):
        wif = b"\x80" + PrivateKey
        wif = next(self.__Base58__(wif + next(self.__SHA256__(next(self.__SHA256__(wif))))[:4]))
        yield wif
    
    def HashGenerator(self):
        # RandomBytes = os.urandom(32)
        # PBK = self.__PublicKeyGenerator__(RandomBytes)
        # PVK = self.__PrivateKeyWIFGenerator__(RandomBytes)

        RandomBytes = os.urandom(32)
        PBK = next(self.__PublicKeyGenerator__(RandomBytes))
        PVK = next(self.__PrivateKeyWIFGenerator__(RandomBytes))
        return {"PublicKey" : PBK, "PrivateKey" : PVK}

