import hashlib
import datetime

class Block: 
    prevHash = ""
    transactions = ""
    blockHash = ""
    timeStamp = ""
    curHash = ""
    nonce = 0
    #Default Constructor to inti values
    def hashBlock(self):
        return hashlib.sha256(str(self.prevHash + str(self.timeStamp) + str(self.transactions)+ str(self.nonce)).encode('utf-8')).hexdigest()
    #Getter
    def getPreviousHash(self):
        return self.prevHash
    #getter
    def getTransaction(self):
        return self.transactions

    def getTimeStamp(self):
        return self.timeStamp 

    def getCurrentHash(self):
        return self.curHash

    def miningBlock(self, difficutly):
        while(self.curHash[:difficutly]!= "0" * difficutly):
            print(self.curHash[:difficutly])
            self.nonce +=1
            self.curHash = self.hashBlock()

    def __init__(self, transactions, timeStamp=None, prevHash=""):    
        self.prevHash = prevHash
        self.transactions = transactions
        if(timeStamp is None):
            self.timeStamp = datetime.datetime.now()
        else:
            self.timeStamp = timeStamp
        self.curHash = self.hashBlock()