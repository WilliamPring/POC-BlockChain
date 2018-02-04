import hashlib
import Block

class BlockChain: 
    chain = []

    def __init__(self):
        #creating a genisis block when initing the BlockChain most of the time its hard coded that the reason
        #we provide a prev hash
        self.chain = [Block.Block("0", "04/02/2018", "0")]
    
    #add a new block to the blockchain
    def addingBlock(self, block): 
        block.prevHash = self.chain[-1].hashBlock()
        #print("The previous hash: " + block.prevHash)
        block.curHash = block.hashBlock()
        
        #print("The current hash:  " + block.hash)
        self.chain.append(block)
    
    def validateBlockChain(self):
        previousValue = nextValue = None
        lengthOfChain = len(self.chain)
        for index, block in enumerate(self.chain):
            if(index>0):
                previousValue = self.chain[index - 1]
            if(index < lengthOfChain -1):
                nextValue = self.chain[index]
            if(previousValue is not None) and (nextValue is not None):
                print(block.getCurrentHash())
                print(nextValue.getCurrentHash())
                print(block.getPreviousHash())
                print(previousValue.getCurrentHash())
                if(block.hashBlock() != nextValue.getCurrentHash()):
                    return False
                if(block.getPreviousHash() != previousValue.getCurrentHash()):
                    return False
                previousValue = nextValue = None
        return True

    #display the whole blockchain
    def displayBlockChain(self):
        for block in self.chain:
            print("Time: " + str(block.getTimeStamp()))
            print("The Previous Hash: " + block.getPreviousHash())
            print("The Current Hash: " + block.getCurrentHash())
            print("The Amount Trans: " + str(block.getTransaction()))
            print("**************************************************")