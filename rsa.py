import random
import math
class RSA:
    def __init__(self, bits=12):
        self.bits = bits
            
    def generateKey(self):
        p = self.generatePrimeNumber()
        q = self.generatePrimeNumber()

        n = p * q
        totient = (p - 1) * (q - 1)

        e = self.getPublicKey(totient)
        d = self.modInverse(e, totient)

        print(f"p: {p}")
        print(f"q: {q}")
        print(f"n: {n}")
        print(f"e: {e}")
        print(f"d: {d}")

        return ((n, e), (n, d))

    def generatePrimeNumber(self):
        while True:
            num = random.getrandbits(self.bits)
            if self.checkPrime(num):
                return num

    def checkPrime(self,num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def getPublicKey(self,totient):
        while True:
            e = random.randint(2, totient - 1)
            if math.gcd(e, totient) == 1:
                return e

    def modInverse(self,a, m):
        m0, x0, x1 = m, 0, 1

        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0

        return x1 + m0 if x1 < 0 else x1

    def encrypt(self,message, publicKey):
        n, e = publicKey
        cipherText = [pow(ord(char), e, n) for char in message]
        return cipherText

    def decrypt(self,cipherText, privateKey):
        n, d = privateKey
        decrypted_integers = [pow(char,d,n) for char in cipherText]
        decrypted_message = ''.join([chr(dec) if dec < 1114112 else chr((dec // 1114112) + 0x0800) for dec in decrypted_integers])
        #decrypted_message = ''.join([chr(pow(char, d, n)) for char in cipherText])
        return decrypted_message

