import hashlib
import datetime

class Block: 
    prevHash = ""
    transactions = ""
    blockHash = ""
    timeStamp = ""
    #Default Constructor to inti values


    def hashBlock(self):
        return hashlib.sha256(str(self.prevHash + str(self.timeStamp) + str(self.transactions)).encode('utf-8')).hexdigest()
    #Getter
    def getPreviousHash(self):
        return self.prevHash
    #getter
    def getTransaction(self):
        return self.transactions

    def getTimeStamp(self):
        return self.timeStamp 

    def __init__(self, transactions, timeStamp=None, prevHash=None):
        self.prevHash = prevHash
        self.transactions = transactions
        if(timeStamp is None):
            self.timeStamp = datetime.datetime.now()
        else:
            self.timeStamp = timeStamp
